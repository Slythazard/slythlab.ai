import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

from routes.index import api

load_dotenv()

PORT = os.getenv("PORT")

app=Flask(__name__)
CORS(app, resources ={r"/api/*": {"origins": f"http://localhost:{PORT}"}})

app.register_blueprint(api,url_prefix='/api')

@app.route('/')
def home():
    data={
        'message':'This is home'
    }
    return jsonify(data)

if __name__=="__main__":
    port = os.getenv('SERVER_PORT')
    app.run(host='0.0.0.0',port=port)