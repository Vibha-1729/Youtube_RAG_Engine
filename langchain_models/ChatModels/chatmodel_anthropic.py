from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chatmodel=ChatAnthropic(model='claude-sonnet-5',temperature=0, max_completion_tokens=10)
result=chatmodel.invoke("What is the capital of India")
print(result.content)