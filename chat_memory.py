# chat_memory.py
from collections import deque

class ChatMemory:
    """
    Manages conversation history using a deque for an efficient
    sliding window buffer.
    """
    def __init__(self, max_turns=5):
        # deque with maxlen provides an efficient sliding window
        self.history = deque(maxlen=max_turns)

    def add(self, user_input, bot_reply):
        """Adds a new user-bot exchange to the memory."""
        self.history.append({"user": user_input, "bot": bot_reply})

    def get_context(self):
        """Formats the past conversation history into a string for the prompt."""
        if not self.history:
            return ""
        
        context = ""
        for turn in self.history:
            context += f"User: {turn['user']}\nBot: {turn['bot']}\n"
        return context.strip()