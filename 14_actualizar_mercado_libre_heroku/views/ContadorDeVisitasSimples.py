from flask.views import View, MethodView
from flask import Flask, render_template,request
from resources.ContadorDeVisitasSimple import ContadorDeVisitasSimple
from werkzeug import secure_filename

class ContadorDeVisitasSimples(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        if request.method == 'POST': #this block is only entered when the form is submitted
            fecha_inicio = request.form.get('fecha_inicio')
            fecha_final = request.form['fecha_final']
            f = request.files['file']
            f.save(secure_filename(f.filename))

            ContadorDeVisitasSimple(fecha_inicio,fecha_final)
            fp = open ('data.txt','r')
            mensaje = fp.read()

            return '''
                      <h1>The fecha_inicio value is: {}</h1>
                      <h1>The fecha_final value is: {}</h1>
                      <h1>The file is: {}</h1>'''.format(fecha_inicio, fecha_final, mensaje)


        return render_template("contador_de _visitas_simples.html"), 200
#
