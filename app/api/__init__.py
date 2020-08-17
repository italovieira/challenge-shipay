from flask_restful import Api, Resource

from .index import IndexApi
from .transaction import TransactionApi

api = Api()

def configure_api(app):
    api.add_resource(IndexApi, '/')
    api.add_resource(TransactionApi, '/transacao')

    api.init_app(app)
