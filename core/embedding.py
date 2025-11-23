from llama_index.core import Settings, VectorStoreIndex
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.llms.google_genai import GoogleGenAI

from config import GEMINI_API_KEY, EMBED_MODEL_NAME, GEMINI_MODEL_NAME


def llm_model_embedding():
    # Embeddings
    Settings.embed_model = GoogleGenAIEmbedding(
        model_name=EMBED_MODEL_NAME, api_key=GEMINI_API_KEY
    )

    Settings.llm = GoogleGenAI(
        model=GEMINI_MODEL_NAME, api_key=GEMINI_API_KEY, temperature=0
    )

    return Settings
