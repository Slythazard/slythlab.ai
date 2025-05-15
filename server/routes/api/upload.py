import os
import tempfile
from utils.loader import load_data_chunk
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
from utils.retriever import create_rag_pipe, query_rag_pipe

load_dotenv()

upload = Blueprint('upload',__name__)

@upload.route('/', methods=['POST','GET'],strict_slashes=False)
def handleUpload():
    query=request.form.get('query')
    file=request.files.get('file')
    if file:
        suffix = os.path.splitext(file.filename)[1].lower()

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            file.save(tmp.name)
            temp_path = tmp.name
            chunk_size=200
            chunk_overlap=0

            print(temp_path)

            vectorstore = load_data_chunk(file_path=temp_path,suffix=suffix,chunk_size=chunk_size,chunk_overlap=chunk_overlap)
        os.unlink(temp_path)

        if query:
            rag_pipe=create_rag_pipe(vectorstore,suffix)
            answer = query_rag_pipe(f"{query}",rag_pipe=rag_pipe)
            response={
                "answer":f"{answer}",
                "vectorstore":f"{vectorstore}"
            }
            print(response)
            return jsonify(response),200