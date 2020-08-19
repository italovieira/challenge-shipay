from flask import Flask, json

from app.api import configure_api
from app.models import configure as configure_db

app = Flask(__name__)
configure_db(app)
configure_api(app)
client = app.test_client()

def test_transaction_success():
    response = client.post('/transacao', json={
        'estabelecimento': '04.096.526/0001-78',
        'cliente': '810.645.920-90',
        'valor': '59.9'
    })

    json_data = response.get_json()

    assert response.status_code == 201
    assert json_data['aceito']

def test_invalid_cnpj():
    response = client.post('/transacao', json={
        'estabelecimento': '14.116.526/0001-77',
        'cliente': '810.645.920-90',
        'valor': '59.9'
    })

    json_data = response.get_json()

    assert response.status_code == 202
    assert not json_data['aceito']

def test_invalid_cpf():
    response = client.post('/transacao', json={
        'estabelecimento': '04.096.526/0001-78',
        'cliente': '810.645.920-89',
        'valor': '59.9'
    })

    json_data = response.get_json()

    assert response.status_code == 202
    assert not json_data['aceito']

