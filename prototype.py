"""This is a protoype script for extracting data from a single
aricle. The real script will loop through multiple articles"""

from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.environ["GROQ_API_KEY"]