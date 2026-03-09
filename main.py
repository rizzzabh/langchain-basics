from loading import PromptLoader
from splitting import Splitter

if __name__ == "__main__" : 
      loader = PromptLoader()
      text = loader.load_prompt()

      print(text)
      splitter = Splitter(text) 
      splitted_text = splitter.split()

      print(splitted_text)
