from flask.views import View, MethodView
from flask import Flask, render_template,request
from resources.ContadorDeVentasSimple import ContadorDeVentasSimple
from werkzeug import secure_filename

class ContadorDeVentasSimples(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        if request.method == 'POST': #this block is only entered when the form is submitted
            f = request.files['file']
            f.save(secure_filename(f.filename))

            datos = ContadorDeVentasSimple()

            return "ok", datos


        return render_template("contador_de_ventas_simples.html"), 200
#
