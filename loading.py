from langchain_community.document_loaders import TextLoader

file_path = "data/data1.txt" ; 


try : 
      loader = TextLoader(file_path , encoding="utf-8")

      documents = loader.load()

      print(documents[0].page_content)

except Exception as e: 
      print(f"An error occured : {e}")


