# model_loader.py
from transformers import pipeline

def load_model(model_name="google/flan-t5-small"):
    """
    Loads a text-to-text generation model and tokenizer from Hugging Face
    using the pipeline abstraction.
    """
    print(f"Loading model: {model_name} ...")
    
    # Use the pipeline for easy text-to-text generation
    generator = pipeline("text2text-generation", model=model_name)
    
    print("Model loaded successfully!")
    return generator