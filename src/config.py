import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
IG_USER_ID = os.getenv("IG_USER_ID")

BASE_URL = "https://graph.facebook.com/v18.0"

if not ACCESS_TOKEN:
    raise ValueError("META_ACCESS_TOKEN não encontrado no .env")

if not IG_USER_ID:
    raise ValueError("IG_USER_ID não encontrado no .env")