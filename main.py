from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
#from lanchain_anthropic import ChatAnthropic 

load_dotenv() #método p carregar as info do env c credenciais

#objeto que define a llm e a versão
llm = ChatOpenAI(model="gpt-4o-mini")

#método p testar o funcionamento do objeto
response = llm.invoke("What is the meaning of Karma?")

print(response)