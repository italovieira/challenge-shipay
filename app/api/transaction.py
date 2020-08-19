from flask import jsonify
from flask_restful import Resource, reqparse

from validate_docbr import CPF, CNPJ

from ..models import db, Transaction, Store, Client

parser = reqparse.RequestParser()
parser.add_argument('estabelecimento', required=True)
parser.add_argument('cliente', required=True)
parser.add_argument('valor', required=True, type=float)
parser.add_argument('descricao')


class TransactionApi(Resource):

    def post(self):
        args = parser.parse_args()
        cnpj = args['estabelecimento']
        cpf = args['cliente']
        value = args['valor']
        description = args['descricao']

        if not CPF().validate(cpf) or not CNPJ().validate(cnpj):
            return {'aceito': False}, 202

        store = Store.query.filter_by(cnpj=cnpj).first()
        if not store:
            store = Store(cnpj=cnpj)
            db.session.add(store)

        client = Client.query.filter_by(cpf=cpf).first()
        if not client:
            client = Client(cpf=cpf)
            db.session.add(client)

        transaction = Transaction(value=value, description=description)
        transaction.store = store
        transaction.client = client

        db.session.add(transaction)
        db.session.commit()

        return {'aceito': True}, 201
