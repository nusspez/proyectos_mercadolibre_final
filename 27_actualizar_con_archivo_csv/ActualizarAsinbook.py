import csv
import time
import requests
import json

with open('config.json') as config_file:
    data = json.load(config_file)

access_token = data['access_token']
site = data['site']

datos = []

headers = {'content-type': 'application/json'}

with open('data.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:

        numero_publicacion = row[0]
        cantidad_actualizada = row[1]
        precio_actualizado = row[2]

        data_product = {
                            "price": precio_actualizado,
                            "available_quantity": cantidad_actualizada
                          }

        r = requests.put(f'https://api.mercadolibre.com/items/{site}{numero_publicacion}?access_token={access_token}', data = json.dumps(data_product),headers=headers)

        x = [numero_publicacion, cantidad_actualizada,precio_actualizado]

        print("elemento no. ", str(row))

        datos.insert(0, x)

        with open('data_out.csv', mode='w') as archivo:
            archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(datos)):
                archivo.writerow(datos[i])

        time.sleep(0.001)
