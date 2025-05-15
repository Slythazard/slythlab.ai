from flask import Blueprint, jsonify

from .api.upload import upload

api = Blueprint('api',__name__)
api.register_blueprint(upload, url_prefix='/upload')


@api.route('/')
def handleApi():
    return jsonify('This is API')
