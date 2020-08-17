from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    transactions = db.relationship('Transaction', back_populates='store')

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(12), unique=True, nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    store = db.relationship('Store', back_populates='transactions')
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship('Client')
    description = db.Column(db.String(120))
