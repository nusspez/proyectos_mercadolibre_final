from flask.views import View, MethodView
from flask import Flask, render_template

class HomePage(View):
    def dispatch_request(self):
        return render_template("/index/index.html"), 200
