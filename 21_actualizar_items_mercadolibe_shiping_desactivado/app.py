from flask import Flask, render_template, request
from werkzeug import secure_filename

import csv
import requests
import json
import time

datos = []

print("introduce el access_token de la pagina")

app = Flask(__name__)

url = 'https://api.mercadolibre.com/items?access_token='
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
              id_delete = row[0]
              seller_custom_field =row[1]
              title = row[2]
              category_id = row[3]
              price = row[4]
              currency_id = row[5]
              available_quantity = row[6]
              buying_mode = row[7]
              listing_type_id = row[8]
              condition = row[9]
              description = row[10]
              video_id = row[11]
              warranty = row[12]

              source1 = row[13]
              source2 = row[14]
              source3 = row[15]
              source4 = row[16]
              source5 = row[17]
              source6 = row[18]

              data_product = {
                                "title": title,
                                "category_id":category_id,
                                "price":price,
                                "currency_id":currency_id,
                                "available_quantity":available_quantity,
                                "buying_mode":buying_mode,
                                "listing_type_id":listing_type_id,
                                "condition":condition,
                                "description": {"plain_text":description},
                                "video_id": video_id,
                                "warranty": warranty,
                                "pictures":[
                                {"source": source1},{"source":source2},{"source":source3},{"source":source4},{"source":source5},{"source":source6}
                                ]
                                }

              data_close = {
                                "status":"closed"
                           }

              data_delete = {
                                "deleted":"true"
                            }

              r = requests.put(f'https://api.mercadolibre.com/items/MLM{row[0]}?access_token={access_token}', data = json.dumps(data_close),headers=headers)

              r = requests.put(f'https://api.mercadolibre.com/items/MLM{row[0]}?access_token={access_token}', data = json.dumps(data_delete),headers=headers)


              r = requests.post(url + access_token, data=json.dumps(data_product),headers=headers)
              print()
              print(r.text)

              json_convert = json.loads(r.content)
              id_item = json_convert["id"]

              url_value = (f'https://api.mercadolibre.com/items/{id_item}?access_token={access_token}')

              data = {'seller_custom_field':str(seller_custom_field)}

              r = requests.put(url_value, data = json.dumps(data))

              print('numero de item :' +  str(row) + ' status code: ' + str(r.status_code))
              print(' ')
              print('--------------------------------------------------------------------------------------------------------------')

              x = [id_item,row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18]]

              datos.insert(0, x)


              time.sleep(1)
      with open('data_out.csv', mode='w') as archivo:
          archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
          for linea in range(len(datos)):
              archivo.writerow(datos[linea])



      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')
