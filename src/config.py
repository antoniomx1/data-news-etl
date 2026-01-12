import os
from dotenv import load_dotenv

load_dotenv()

# --- GEMINI ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
if not GEMINI_API_KEY:
    raise ValueError("ERROR FATAL: Falta GEMINI_API_KEY")

# --- TELEGRAM (NUEVO) ---
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()

# Validamos para que no truene silenciosamente
if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    print("[WARN] No se configuraron las credenciales de Telegram. Solo se imprimira en consola.")

# --- FUENTES ---
RSS_FEEDS = [
    "https://realpython.com/atom.xml",
    "https://feeds.feedburner.com/TheHackerNews",
    "https://googlecloud.blogspot.com/atom.xml",
]

GENAI_MODEL = "gemini-2.5-flash"
