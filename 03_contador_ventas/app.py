from flask import Flask, render_template, request
from werkzeug import secure_filename

from lxml import html

import csv
import requests
import json
import time
import re


datos = []


app = Flask(__name__)
headers = {'content-type': 'application/json'}

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_btn():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))

      with open('data.csv', newline='') as File:
          reader = csv.reader(File)
          for row in reader:

              id_item = row[0]

              url = (f'https://articulo.mercadolibre.com.co/MLM-{id_item}-_JM')

              print(url)

              req = requests.get(url)

              tree = html.fromstring(req.content)

              numero_ventas = tree.xpath('//*[@id="short-desc"]/div/dl/div/text()')

              numero_ventas = re.findall(r'([+-]?\d+(?:\.\d+)?(?:[eE][+-]\d+)?)', str(numero_ventas))

              longitud = len(numero_ventas)

              if longitud > 1:
                  numero_ventas = numero_ventas[longitud - 1]

              x = [row[0], numero_ventas]

              datos.insert(0, x)

              time.sleep(1)

      with open('data_out.csv', mode='w') as archivo:
          archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
          for linea in range(len(datos)):
              archivo.writerow(datos[linea])



      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')
