from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from pydantic import BaseModel, Field
from langchain.tools import StructuredTool
from datetime import datetime

#criando a classe que irá salvar a pesquisa feita
class SaveInput(BaseModel):
    data: str = Field(..., description="Text to write inside the file")
    filename: str = Field("pesquisa_wikipedia.txt", description="Output filename")

#função para salvar
def salva_txt(data: str, filename: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texto_formatado = f"--- Research Output ---\nTimeStamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(texto_formatado)

    return f"Data saved to {filename} successfully"

#estruturando o salvamento para evitar quebra
salva_tool = StructuredTool(
    name="save_text_to_file",
    description="Save text to a .txt file. Useful when the user wants to export results.",
    func=salva_txt,
    args_schema=SaveInput,
)
#podemos alterar essa tool e classe pra chamar uma api


#criando a tool da wikipedia
api_wrapper = WikipediaAPIWrapper(top_k_results=3, doc_content_chars_max=1000) #tres resultados da wikipedia limitados a 1000 caracteres

wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)