import os

from dotenv import load_dotenv
from fastapi import FastAPI
from langfuse import Langfuse
from openai import AsyncOpenAI
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# Load environment variables
jai_api_key = os.getenv('JAI_API_KEY')
jai_base_url = os.getenv('CHAT_BASE_URL')

google_api_key = os.getenv('GOOGLE_API_KEY')
google_base_url = os.getenv('GOOGLE_BASE_URL')

typhoon_gemma_12b_api_key = os.getenv('TYPHOON_GEMMA_12B_API_KEY')
typhoon_gemma_12b_base_url = os.getenv('TYPHOON_GEMMA_12B_BASE_URL')

# Validate the environment variables
if not jai_api_key or not jai_base_url or not jai_base_url:
    raise ValueError('Missing required environment variables: JAI_API_KEY or CHAT_BASE_URL.')

# Initialize OpenAI client
jai_client = AsyncOpenAI(api_key=jai_api_key, base_url=jai_base_url)
typhoon_gemma_12b_client = AsyncOpenAI(api_key=typhoon_gemma_12b_api_key, base_url=typhoon_gemma_12b_base_url)


# Load Langfuse varaibles
langfuse_public_key = os.getenv('LANGFUSE_SECRET_KEY')
langfuse_secret_key = os.getenv('LANGFUSE_PUBLIC_KEY')
langfuse_host = os.getenv('LANGFUSE_HOST')

# Initialize Langfuse
langfuse = Langfuse(
    public_key=langfuse_public_key,
    secret_key=langfuse_secret_key,
    host=langfuse_host
)

# Validate Langfuse environment variables
if not langfuse_public_key or not langfuse_secret_key or not langfuse_host:
    raise ValueError('Missing required Langfuse environment variables.')

# Initialize MongoDB Client
client = MongoClient(os.getenv('MONGODB_URI'))
db = client["demo"]
collection = db["documents"]
search_index_name = 'default'

app = FastAPI()
