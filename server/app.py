import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

from routes.index import api

load_dotenv()

CLIENT_PORT = os.getenv("CLIENT_PORT")

app=Flask(__name__)
CORS(app, resources ={r"/api/*": {"origins":[ f"http://localhost:{CLIENT_PORT}","https://slythlab-ai.onrender.com","https://slythlab-ai.vercel.app","https://slythlab-ai.slythlab.dev"]}})

app.register_blueprint(api,url_prefix='/api')

@app.route('/')
def home():
    data={
        'message':'This is home'
    }
    return jsonify(data)

if __name__=="__main__":
    port = int(os.environ.get('PORT'))
    print(port)
    app.run(host='0.0.0.0',port=port)