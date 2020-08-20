from flask import Flask, json

from app.api import configure_api
from app.models import configure as configure_db, Store, Transaction, Client

app = Flask(__name__)
db = configure_db(app)
configure_api(app)
c = app.test_client()

store = Store(name='Nosso Restaurante de Todo Dia LTDA', cnpj='45283163000167', owner='Fabio I.', phone='11909000300')
transaction1 = Transaction(value=590.01, description='Almoço em restaurante chique pago via Shipay!')
transaction2 = Transaction(value=591, description='Almoço em restaurante chique pago via Shipay!')
client = Client(cpf='09421493001')
transaction1.client = client
transaction2.client = client
store.transactions.append(transaction1)
store.transactions.append(transaction2)

with app.app_context():
    db.session.add(store)
    db.session.commit()

def test_transaction_success():
    response = c.post('/transacao', json={
        'estabelecimento': '04.096.526/0001-78',
        'cliente': '810.645.920-90',
        'valor': 59.9
    })

    json_data = response.get_json()

    assert response.status_code == 201
    assert json_data['aceito']

def test_invalid_cnpj():
    response = c.post('/transacao', json={
        'estabelecimento': '14.116.526/0001-77',
        'cliente': '810.645.920-90',
        'valor': 59.9
    })

    json_data = response.get_json()

    assert response.status_code == 202
    assert not json_data['aceito']

def test_invalid_cpf():
    response = c.post('/transacao', json={
        'estabelecimento': '04.096.526/0001-78',
        'cliente': '810.645.920-89',
        'valor': 59.9
    })

    json_data = response.get_json()

    assert response.status_code == 202
    assert not json_data['aceito']


def test_get_transactions():
    response = c.get('/transacoes/estabelecimento?cnpj=45.283.163/0001-67')

    json_data = response.get_json()

    assert response.status_code == 201

    json_data = response.get_json()

    store_dict = json_data['estabelecimento']
    assert store_dict == {
        'nome': 'Nosso Restaurante de Todo Dia LTDA',
        'cnpj': '45.283.163/0001-67',
        'dono': 'Fabio I.',
        'telefone': '11909000300'
    }

    transactions_dict = json_data['recebimentos']

    assert transactions_dict[0] == {
        'cliente': '094.214.930-01',
        'valor': 590.01,
        'descricao': 'Almoço em restaurante chique pago via Shipay!'
    }
    assert transactions_dict[1] == {
        'cliente': '094.214.930-01',
        'valor': 591,
        'descricao': 'Almoço em restaurante chique pago via Shipay!'
    }

    assert json_data['total_recebido'] == 1181.01
