import csv
import time
import requests
import json

datos = []

headers = {'content-type': 'application/json'}

print("introduce el access_token de la pagina")

access_token = input()

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

        r = requests.put(f'https://api.mercadolibre.com/items/MCO{numero_publicacion}?access_token={access_token}', data = json.dumps(data_product),headers=headers)


        x = [numero_publicacion, cantidad_actualizada,precio_actualizado]

        print("elemento no. " + row + x)

        datos.insert(0, x)

        with open('data_out.csv', mode='w') as archivo:
            archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(datos)):
                archivo.writerow(datos[i])

        time.sleep(0.001)
