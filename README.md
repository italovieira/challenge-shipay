# The Resident Zombie

https://gist.github.com/akitaonrails/711b5553533d1a14364907bbcdbee677

## Installation (via docker-compose)

Create a `.env` file with the variables to fit your environment

```console
$ cat .env
APP_PORT=5000
DEBUG=True
DB_URI=postgresql://postgres:postgres@$localhost/shipay
```

Use the following command to run the server

```sh
$ docker-compose up
```

Or to run in the background

```sh
$ docker-compose up -d
```

## Testing

For testing purposes you can run

```sh
$ docker-compose run --rm app pytest
```

## Signup

```sh
$ curl -H "Content-Type: application/json" -X POST http://localhost:5000/transacao \
-d '{
  "estabelecimento": "45.283.163/0001-67",
  "cliente": "094.214.930-01",
  "valor": 590.01,
  "descricao": "Almoço em restaurante chique pago via Shipay!"
}'
```

## Update location

```sh
$ curl -H "Content-Type: application/json" -X PUT http://localhost:5000/transacoes/estabelecimento?cnpj=45.283.163/0001-67
```
