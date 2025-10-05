# interface.py
from model_loader import load_model
from chat_memory import ChatMemory

def main():
    generator = load_model("google/flan-t5-small")
    memory = ChatMemory(max_turns=5)

    print("\n Local Chatbot (Flan-T5-Small) Ready! Type '/exit' to quit.\n")

    # Basic factual lookup (for capital questions)
    facts = {
        "france": "Paris",
        "italy": "Rome",
        "india": "New Delhi",
        "russia": "Moscow",
        "japan": "Tokyo",
        "china": "Beijing",
        "usa": "Washington, D.C.",
        "united states": "Washington, D.C."
    }

    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        # Build instruction-based prompt
        context = memory.get_context()
        if context:
            # We now properly include the conversation history in the prompt.
            prompt = f"""Based on the conversation below, answer the user's latest question factually and concisely.

Conversation History:
{context}

User's Latest Question: {user_input}
Answer:"""
        else:
            prompt = f"Answer this question factually and completely in one sentence: {user_input}"

        # Generate response
        response = generator(
            prompt,
            max_new_tokens=80,
            truncation=True,
            num_return_sequences=1
        )[0]["generated_text"]

        bot_reply = response.strip().capitalize()

        # Post-process: handle too-short or vague replies
        lower_input = user_input.lower()
        if "capital" in lower_input or ("what about" in lower_input and context):
            for country, capital in facts.items():
                if country in lower_input:
                    bot_reply = f"The capital of {country.capitalize()} is {capital}."
                    break

        # Clean and print
        print(f"Bot: {bot_reply}\n")
        memory.add(user_input, bot_reply)


if __name__ == "__main__":
    main()