from flask import request
from flask_restful import Resource, reqparse

from validate_docbr import CPF, CNPJ

from ..models import db, Transaction, Store, Client

parser = reqparse.RequestParser()
parser.add_argument('cnpj', required=True)

class TransactionsApi(Resource):

    def get(self):
        args = parser.parse_args()
        cnpj = args['cnpj']

        if not CNPJ().validate(cnpj):
            return {'mensagem': 'CNPJ é inválido'}, 202

        store = Store.query.filter_by(cnpj=cnpj).first()
        if not store:
            return {'mensagem': 'Estabelecimento com esse CNPJ não encontrado'}, 202

        return {
                'estabelecimento': {
                    'nome': store.name,
                    'cnpj': store.cnpj,
                    'dono': store.owner,
                    'telefone': store.phone
                },
                'recebimentos':
                [{
                    'cliente': transaction.client.cpf,
                    'valor': transaction.value,
                    'descricao': transaction.description
                } for transaction in store.transactions
                ],
                'total_recebido': sum(transaction.value for transaction in store.transactions)
                }, 201
