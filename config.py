from dotenv import load_dotenv
import os

API_KEY = os.environ.get('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set")

STORAGE_PATH = os.environ.get('STORAGE_PATH', '/tmp/')
os.makedirs(STORAGE_PATH, exist_ok=True)

GCP_SA_CREDENTIALS = os.environ.get('GCP_SA_CREDENTIALS', '')
GDRIVE_USER = os.environ.get('GDRIVE_USER', '')

# Attempt to load .env file, but don't fail if it doesn't exist
load_dotenv(verbose=True)

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set")

STORAGE_PATH = os.getenv('STORAGE_PATH', '/tmp/')
os.makedirs(STORAGE_PATH, exist_ok=True)

GCP_SA_CREDENTIALS = os.getenv('GCP_SA_CREDENTIALS', '')
GDRIVE_USER = os.getenv('GDRIVE_USER', '')
GCP_BUCKET_NAME = os.getenv('GCP_BUCKET_NAME', '')
