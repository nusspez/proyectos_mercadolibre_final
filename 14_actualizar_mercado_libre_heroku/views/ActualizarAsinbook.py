from flask.views import View, MethodView
from flask import Flask, render_template,request
from resources.actualizar import actualizar

class ActualizarAsinbook(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        if request.method == 'POST': #this block is only entered when the form is submitted
            access_token =  request.form['access_token']
            project_token = request.form['project_token']
            start_number = request.form['start_number']


            # ActualizarAsinbook(access_token,project_token,start_number)
            actualizar(access_token,project_token,start_number)

            return '''
                      <h1>The fecha_inicio value is: {}</h1>
                      <h1>The fecha_final value is: {}</h1>
                      <h1>The file is: {}</h1>'''.format(access_token, project_token, start_number)


        return render_template("ActualizarAsinbook.html"), 200
#
