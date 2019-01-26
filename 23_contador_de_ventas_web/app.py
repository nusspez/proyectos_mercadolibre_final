from flask import Flask, request
from views.ContadorDeVentasSimples import ContadorDeVentasSimples
from views.HomePage import HomePage


app = Flask(__name__, template_folder='templates')
PORT = 5000
DEBUG = True

app.add_url_rule('/', view_func=HomePage.as_view('HomePage'))

app.add_url_rule('/ContadorDeVentasSimples', view_func=ContadorDeVentasSimples.as_view('ContadorDeVentasSimples'))


if __name__ == "__main__":
    app.run(port = PORT, debug = DEBUG)
