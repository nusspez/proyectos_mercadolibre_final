from flask import Flask, request
from views.ContadorDeVisitasSimples import ContadorDeVisitasSimples
from views.HomePage import HomePage


app = Flask(__name__, template_folder='templates')
PORT = 5000
DEBUG = True

app.add_url_rule('/', view_func=HomePage.as_view('HomePage'))

app.add_url_rule('/ContadorDeVisitasSimples', view_func=ContadorDeVisitasSimples.as_view('ContadorDeVisitasSimples'))


if __name__ == "__main__":
    app.run(port = PORT, debug = DEBUG)
