from flask import Flask, render_template, request
from werkzeug import secure_filename

import csv
import requests
import json
import time

datos = []

print("introduce el access_token de la pagina")

app = Flask(__name__)
headers = {'content-type': 'application/json'}
access_token = input()

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

              data_paused = {
                              "status":"paused"
                           }

              r = requests.put(f'https://api.mercadolibre.com/items/MLM{row[0]}?access_token={access_token}', data = json.dumps(data_paused),headers=headers)

              x = [row[0]]

              datos.insert(0, x)


              time.sleep(1)
      with open('data_out.csv', mode='w') as archivo:
          archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
          for linea in range(len(datos)):
              archivo.writerow(datos[linea])



      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')
