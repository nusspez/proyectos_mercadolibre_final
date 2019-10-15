from app import app
from flask import render_template
from app.views.ActualizarAsinbook import ActualizarAsinbook
from app.views.HomePage import HomePage

@app.errorhandler(404)
def not_found(e):
  return render_template("/404/404.html"),404

app.add_url_rule('/', view_func=HomePage.as_view('HomePage'))

app.add_url_rule('/ActualizarAsinbook', view_func=ActualizarAsinbook.as_view('ActualizarAsinbook'))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
