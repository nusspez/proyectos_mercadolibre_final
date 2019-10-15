from flask.views import View, MethodView
from flask import Flask, render_template,request
from app.resources.actualizar import actualizar
from werkzeug import secure_filename

class ActualizarAsinbook(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        if request.method == 'POST': #this block is only entered when the form is submitted
            access_token =  request.form['access_token']
            f = request.files['file']
            f.save(secure_filename(f.filename))

            # ActualizarAsinbook(access_token,project_token,start_number)
            actualizar(access_token)

            return 'ok'


        return render_template("Actualizar/Actualizarasinbook.html"), 200
#
