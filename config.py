# loading central configuration for the application# central configuration for the pipeline
import os
from dotenv import load_dotenv

load_dotenv()

# Environment variables
OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")

# Model
DEFAULT_MODEL = "gpt-4.1-mini"
TEMPERATURE = 0.2
MAX_TOKENS = 512

# Cache 
CACHE_TTL_SECONDS = 1800 # 30 minutes
VECTOR_TOP_K = 2  # number of top results to retrieve