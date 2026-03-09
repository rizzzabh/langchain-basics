from langchain_text_splitters import RecursiveCharacterTextSplitter 

class Splitter : 
   text = "nothing"
   def __init__(self , text = "Hello") : 
      self.text = text 

   def split(self) : 

      try : 
      
            splitter = RecursiveCharacterTextSplitter(chunk_size = 100 , chunk_overlap=20)

            chunks = splitter.split_text(self.text) 

            return chunks 

      except Exception as e :       
            print (f"an error occured : {e}")
