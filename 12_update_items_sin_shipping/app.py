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

              id_item = [0]
              title = row[1]
              price = row[2]
              available_quantity = row[3]



              data_product = {
                                  "title": title,
                                  "price": price,
                                  "available_quantity": available_quantity


                                }


              r = requests.put(f'https://api.mercadolibre.com/items/MLM{row[0]}?access_token={access_token}', data = json.dumps(data_product),headers=headers)


              print()
              print(r.text)

              json_convert = json.loads(r.content)

              x = [row[0],row[1],row[2],row[3]]

              datos.insert(0, x)


              time.sleep(1)
      with open('data_out.csv', mode='w') as archivo:
          archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
          for linea in range(len(datos)):
              archivo.writerow(datos[linea])



      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')
