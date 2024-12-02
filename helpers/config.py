import os
from dotenv import load_dotenv

load_dotenv()

settings = {
    "api_key": os.environ.get("GEMINI_API_KEY"),
    "model_name": "gemini-1.5-flash",
    "some_other_config": "value"
}