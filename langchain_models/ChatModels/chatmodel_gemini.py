from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatmodel=ChatGoogleGenerativeAI(model='gemini-3.6-flash')
result=chatmodel.invoke("What is the capital of India")
print(result.text)