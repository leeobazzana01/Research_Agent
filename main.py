from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import wiki_tool, salva_tool

#from lanchain_anthropic import ChatAnthropic 

load_dotenv() #método p carregar as info do env c credenciais

#objeto que define a llm e a versão
llm = ChatOpenAI(model="gpt-4o-mini")

#método p testar o funcionamento do objeto
#response = llm.invoke("What is the meaning of Karma?")

#podemos alterar essa classe para buscar dados da maneira que quisermos à LLM desde q herdemos de baseModel
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


#criando o parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse) #podemos mudar esse parses para se comunicar via json ao invés de objeto

#setar o prompt
prompt = ChatPromptTemplate.from_messages( #o prompt é o objeto do ChatPromptTemplate com o método from_messages
    [
        (
            "system",
            """
            You are a Robotics researcher that will help generate a papper.
            Answer the user query and use necessary toools.
            Wrap the output in this format and provide no other text\n{format_instructions}
            """
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())
#basicamente, nós transformamos o objeto da classe em uma string para passar para o systema

#lista d ferrramentas
tools = [wiki_tool, salva_tool]

#criando o agente com formato da classe
agente = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools #para acessar a lista
)

#criando o executor

#criando um agente que usa o método 'AgentExecutor' para definir, por exmpl, se queremos ou nao a chain_of_thoughts
executor_agente = AgentExecutor(agent=agente, tools=tools, verbose=True)

#query p perguntar ao usuário
query = input("How can i assist on your Robotics Research? ")

#gerando uma resposta da ia com o invoke
resposta_inicial = executor_agente.invoke({"query": query}) #poderia passar outros parâmetros mudando essa query

#usando o parser para estrutuar o objeto com a resposta em formato JSON
resposta_estruturada = parser.parse(resposta_inicial.get("output", ""))
print(resposta_estruturada)




