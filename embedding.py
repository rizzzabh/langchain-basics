import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

from huggingface_hub import login
login(token = os.getenv("HF_TOKEN"))

class Transformer : 
      chunks = ["hi"]
      def __init__(self , chunks) :
            self.chunks = chunks
       

      def transform (self) : 
            
            model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            embeddings = model.encode(self.chunks)

            return embeddings
      