import os
from dotenv import load_dotenv
load_dotenv(".env")

# Config file that contains secrets values and some hard coded values

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
QUERY_RETRIEVER_MODEL = "reciprocal_rerank"
EMBED_MODEL_NAME = "models/text-embedding-004"
GEMINI_MODEL_NAME = "gemini-2.5-flash"