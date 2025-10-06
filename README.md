

````markdown
````
# Local Command-Line Chatbot

This project is a command-line chatbot developed in Python that uses the `google/flan-t5-small` model from Hugging Face for text generation. The chatbot is capable of maintaining a short-term memory to handle multi-turn conversations coherently.

## Design Decisions

### Model Selection Journey

The primary challenge of this assignment was selecting a model that could handle factual, multi-turn conversations. My development process involved evaluating several models:

1. **Initial Exploration (`microsoft/DialoGPT-small` & `gpt2`):** My first attempts used general-purpose conversational models. While good at generating human-like text, they struggled with the core task. `DialoGPT` often gave non-factual answers, and `gpt2` was prone to simply completing the user's sentence. Both models failed to reliably answer factual questions.

2. **Final Choice (`google/flan-t5-small`):** The breakthrough came from switching to an **instruction-tuned** model. `Flan-T5` is specifically trained to follow instructions and perform tasks like question-answering, making it the perfect choice for this assignment.

### Achieving Conversational Coherence: The Memory System

The ultimate goal of this assignment was to create a chatbot that is not just a question-answer machine, but a coherent conversationalist. This is achieved through the memory system, which was the central focus of the implementation.

* **The Core Challenge:** A language model has no inherent memory of past interactions. Without a robust context management system, it cannot understand follow-up questions like "and what about Italy?". Achieving this was the main objective.

* **The Solution:** I solved this by implementing a two-part memory system:

  1. **Sliding Window Buffer:** The `chat_memory.py` module uses Python's `deque` with a `maxlen`. This provides a highly efficient sliding window that stores the last few turns of the conversation.

  2. **Contextual Prompting:** The `interface.py` script then takes this stored history and dynamically builds it into the prompt sent to the AI. This explicitly provides the model with the necessary context to understand and correctly answer nuanced, multi-turn questions.

This successful implementation of the memory system is what elevates the project from a simple text generator to a functional, coherent chatbot that meets the assignment's core objective.

### Hybrid Approach and Model Scalability

The hybrid lookup mechanism (dictionary-based fact retrieval) is primarily designed to enhance factual reliability 
in smaller, CPU-friendly models such as `google/flan-t5-small`. These lightweight models occasionally generate incomplete 
or ambiguous factual responses due to their limited parameter size.

When using **more powerful instruction-tuned models**, the hybrid approach becomes  unnecessary. 
Models such as:

- `mistralai/Mistral-7B-Instruct`
- `meta-llama/Llama-2-7b-chat-hf` or `Llama-3-8B-Instruct`

are capable of generating **factually accurate, context-aware, and coherent responses** without relying on predefined lookups.

> ⚙️ **Note:**  
> The above models deliver much higher factual accuracy but require **GPU acceleration** for efficient inference.  
> On CPU setups, the hybrid approach used in this project ensures factual reliability without compromising performance.

## Setup Instructions

1. **Create a Virtual Environment:**
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`


2.  **Install Dependencies:**
    Install the required packages from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

To start the chatbot, run the `interface.py` script from your terminal:

```bash
python interface.py
```

The script will first download the model from Hugging Face, which may take a few minutes on the first run. Once loaded, you can begin the conversation. To quit, type `/exit`.

## Sample Interaction

```
$ python interface.py
Loading model: google/flan-t5-small ...
Model loaded successfully!

Local Chatbot (Flan-T5-Small) Ready! Type '/exit' to quit.

User: What is the capital of France?
Bot: The capital of France is Paris.

User: and what about Italy?
Bot: The capital of Italy is Rome.

User: /exit
Bot: Exiting chatbot. Goodbye!
```
## Demo Video: A face-cam recording explaining the working code (2–3 min).
 1.  Show code structure and walk-through
 2.  Run interaction examples
 3.  Talk about design decisions
```
 https://www.loom.com/share/208d3f7e81da41acbc830fd6d20c41dd?sid=904535f1-3287-4c6a-ad24-79dd8c84c4b2
```

## you can simple check this on google colad through this link 
```
https://colab.research.google.com/drive/1m0W3BX8_SiX-mEizZGzmFplK7OI6jt0S?usp=sharing
```
````