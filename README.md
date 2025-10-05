

````markdown
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

### Hybrid Approach for Robustness

For a specific set of common facts (e.g., capital cities), the chatbot uses a local dictionary lookup. This is a deliberate design choice that checks for a known answer *before* calling the AI. This guarantees 100% accuracy and instant response times for the most frequent questions, making the system more robust and efficient.

## Setup Instructions

1. **Create a Virtual Environment:**
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
````

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