import os
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.vectorstores import Pinecone
from config import OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_API_ENVIRONMENT
from constants import PINECONE_INDEX_NAME


os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_API_ENVIRONMENT
)
print('Pinecone API key set')
# Set Pinecone index
embeddings = OpenAIEmbeddings(client='')

docsearch = Pinecone.from_existing_index(
    index_name=PINECONE_INDEX_NAME, embedding=embeddings)

# Create the tool
retriever = docsearch.as_retriever()
retriever_tool = create_retriever_tool(
    retriever,
    name="qa_conversational_business",
    description="Searches and returns documents regarding conversational business. Input: send the user input."
)
