from loading import PromptLoader
from splitting import Splitter
from embedding import Transformer

if __name__ == "__main__" : 
      loader = PromptLoader()
      text = loader.load_prompt()

    
      splitter = Splitter(text) 
      splitted_text = splitter.split()

      transformer = Transformer(splitted_text) 

      embeddings = transformer.transform()

      print(embeddings)

      
