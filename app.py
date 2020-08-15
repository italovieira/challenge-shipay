from os import getenv
from os.path import dirname, isfile, join

from dotenv import load_dotenv


# add to the path .env file
_ENV_FILE = join(dirname(__file__), '.env')

# if .env exists read it
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)


from app import create_app

app = create_app(getenv('FLASK_ENV') or 'default')

if __name__ == '__main__':
    ip = '0.0.0.0'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    # run flask web server
    app.run(
        host=ip, debug=debug, port=port, use_reloader=debug
    )
