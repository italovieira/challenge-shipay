# Challenge 1

## Installation (via docker-compose)

Create a `.env` file with the variables to fit your environment

```console
$ cat .env
APP_PORT=5000
DEBUG=True
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_NAME=shipay
DB_URI=postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}/${DB_NAME}
```

Use the following command to run the server

```sh
$ docker-compose up -d db # to start postgres container to be ready before connect to database in app container
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

## Add transaction

```sh
$ curl -H "Content-Type: application/json" -X POST http://localhost:5000/api/v1/transacao \
-d '{
  "estabelecimento": "45.283.163/0001-67",
  "cliente": "094.214.930-01",
  "valor": 590.01,
  "descricao": "Almoço em restaurante chique pago via Shipay!"
}'
```

## Get transactions by store

```sh
$ curl -H "Content-Type: application/json" -X PUT http://localhost:5000/api/v1/transacoes/estabelecimento?cnpj=45.283.163/0001-67
```
