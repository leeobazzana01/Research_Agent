# Web Research Agent

Este projeto implementa um agente inteligente capaz de realizar pesquisas na web e salvar os resultados em arquivos de texto. Ele utiliza LangChain, ferramentas personalizadas (StructuredTools) e o modelo da OpenAI para gerar respostas estruturadas, como resumos em JSON.

O objetivo é oferecer uma base simples e extensível para criação de agentes autônomos voltados para pesquisa, coleta de dados e processamento automatizado.

## Funcionalidades

1. Realização de pesquisas na web utilizando o DuckDuckGoSearchRun.

2. Execução de ferramentas estruturadas definidas com Pydantic e LangChain.

3. Geração de respostas em formato JSON, textos processados ou análises.

4. Salvamento automático dos resultados em arquivos .txt.

5. Facilidade para adicionar novas ferramentas e fluxos personalizados.

## Estrutura do Projeto


  ├── main.py              # Arquivo principal; inicializa o agente e processa entradas
  
  ├── tools.py             # Implementação das ferramentas (search, salvar arquivo etc)
  
  ├── requirements.txt     # Dependências do projeto
  
  ├── README.md            # Este documento
  
  ├── venv/                # Ambiente virtual (não incluso no repositório)
  
  └── __pycache__/         # Arquivos de cache do Python

## Tecnologias Utilizadas

Python 3.12+

LangChain

OpenAI API

LangChain Community Tools

Pydantic

Estruturas de ferramentas com StructuredTool

## Pré-requisitos

Python 3.12 instalado

Pip instalado

Uma chave de API válida da OpenAI

## Configuração do Ambiente
1. Clonando o Repositório
git clone https://github.com/leeobazzana01/Research_Agent/tree/main
cd <seu-repositorio>

2. Criando o Ambiente Virtual
python3 -m venv venv
source venv/bin/activate     # Linux/MacOS
venv\Scripts\activate        # Windows

3. Instalando as Dependências
pip install -r requirements.txt

4. Criando o Arquivo .env

Crie um arquivo chamado .env na raiz do projeto e adicione sua chave da OpenAI:

OPENAI_API_KEY="sua_chave_aqui"


Certifique-se de não compartilhar esse arquivo nem versioná-lo no GitHub.

## Executando o Projeto

Após configurar o ambiente virtual e o .env, execute:

python3.12 main.py


O agente irá iniciar e aguardar suas instruções no terminal.
Você pode solicitar pesquisas, resumos, geração de JSON e salvamento de arquivos usando linguagem natural.

## Personalização

Novas ferramentas podem ser adicionadas editando o arquivo tools.py.
LangChain e Pydantic permitem definir facilmente schemas, validações e comportamentos avançados.

## Licença

Este projeto está disponível sob a licença MIT. 
