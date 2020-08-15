from flask_restful import Api, Resource

from .index import IndexApi

api = Api()

def configure_api(app):
    api.add_resource(IndexApi, '/')

    api.init_app(app)
