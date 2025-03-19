import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
    UNSPLASH_API_KEY = os.getenv("UNSPLASH_API_KEY")
    PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
    NAMECHEAP_API_KEY = os.getenv("NAMECHEAP_API_KEY")
    NAMECHEAP_USERNAME = os.getenv("NAMECHEAP_USERNAME")
    NAMECHEAP_CLIENT_IP = os.getenv("NAMECHEAP_CLIENT_IP")
    FTP_HOST = os.getenv("FTP_HOST")
    FTP_USERNAME = os.getenv("FTP_USERNAME")
    FTP_PASSWORD = os.getenv("FTP_PASSWORD")
    AMAZON_AFFILIATE_ID = os.getenv("AMAZON_AFFILIATE_ID")
