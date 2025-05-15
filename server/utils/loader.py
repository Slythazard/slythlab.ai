from dataclasses_json.mm import schema
from docs.conf import project
from langchain_community.document_loaders import PyMuPDFLoader, UnstructuredCSVLoader, UnstructuredExcelLoader, TextLoader
from langchain_community.document_loaders.parsers import RapidOCRBlobParser, BaseImageBlobParser,PyMuPDFParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_weaviate.vectorstores import WeaviateVectorStore
from langchain_ibm.embeddings import WatsonxEmbeddings
import weaviate
import time
from nltk.corpus.reader import documents
from weaviate.classes.init import Auth
import os
from dotenv import load_dotenv
from weaviate.collections.classes.config import Configure

load_dotenv()

weaviate_key = os.getenv("WEAVIATE_API_KEY")

# Initialize embeddings (do once at module level for reuse)
def get_embeddings():
    return WatsonxEmbeddings(
        apikey=os.getenv("WATSONX_API_KEY"),
        url=os.getenv("WATSONX_URL"),
        model_id=os.environ.get("WATSONX_EMBED_MODEL"),
        project_id=os.getenv("WATSONX_PROJECT_ID")
    )


# Initialize Weaviate client (do once at module level for reuse)
def get_weaviate_client():
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.getenv("WEAVIATE_URL"),
        auth_credentials=Auth.api_key(weaviate_key),
    )
    #
    # # Create schema if not exists
    # Define collection schema
    #     client.collections.create(
    #         name="Document",
    #         properties=[
    #             {"name": "content", "dataType": ["text"]},
    #             {"name": "source", "dataType": ["text"]},
    #             {"name": "metadata", "dataType": ["text"]}
    #         ],
    #         vectorizer_config=Configure.Vectorizer.none()  # Disable auto-vectorization
    #     )

    return client


# Get a reference to the existing vectorstore
def get_vectorstore(document):
    """Get a reference to the existing vectorstore"""
    client = get_weaviate_client()
    embeddings = get_embeddings()
    vectorstore = WeaviateVectorStore(
        client=client,
        index_name=document,
        text_key="text",
        embedding=embeddings
    )

    return vectorstore


def load_data_chunk(file_path, suffix, chunk_size, chunk_overlap):
    document=f"Document_{int(time.time())}"
    print(document)
    client = get_weaviate_client()
    embeddings = get_embeddings()

    if suffix == '.pdf':
        loader = PyMuPDFLoader(
        file_path,
        extract_images=True,
        images_parser=RapidOCRBlobParser())
    elif suffix in ['.xlsx', ".xlx"]:
        loader = UnstructuredExcelLoader(file_path)
    elif suffix == '.csv':
        loader = UnstructuredCSVLoader(file_path)
    else:
        loader = TextLoader(file_path)

    data = loader.load()
    print(f"data:{data}")
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap).split_documents(data)

    print(f"chunks:{chunks}")
# Add documents to Weaviate
    WeaviateVectorStore.from_documents(
        chunks,
        embedding=embeddings,
        client=client,
        by_text=False,  # We're providing vectors directly
        index_name=document
)
    vectorstore = get_vectorstore(document)
    print(vectorstore._index_name)
    client.close()
    return vectorstore