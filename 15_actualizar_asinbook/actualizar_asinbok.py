from progress.bar import Bar
import csv
import time
import requests
import json

# start = time.clock()

print("introduce el access_token")
access_token = input()

datos = []

print("introduce el project_token")
PROJECT_TOKEN = input()

print("introduce el numero de inicio de publicacion dentro de parsehub")
start_number = input()


# PROJECT_TOKEN = 'tjM50RyEFTuB'
API_KEY = 'tTiMYTuTwX04'


params = {
  "api_key": API_KEY,
  "format": "JSON"
}

r = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params=params)

data_decoded = json.loads(r.content)

numero_productos = len(data_decoded["list1"])

numero_productos_final = len(data_decoded["list1"]) - int(start_number)

bar = Bar('Processing', max=numero_productos)

i = numero_productos

for i in range(numero_productos - 1):

    list1_ad = data_decoded['list1'][numero_productos-numero_productos_final+i]['ad']

    list1_Cantidad = data_decoded["list1"][numero_productos-numero_productos_final+i]["Cantidad"]
    list1_precio = data_decoded["list1"][numero_productos-numero_productos_final+i]["preciocop"]

    headers = {'content-type': 'application/json'}

    data_product = {
                        "price": list1_precio,
                        "available_quantity": list1_Cantidad
                      }

    r = requests.put(f'https://api.mercadolibre.com/items/MLM{list1_ad}?access_token={access_token}', data = json.dumps(data_product),headers=headers)

    x = [list1_ad, list1_Cantidad,list1_precio]
    datos.insert(0, x)

    with open('data_out.csv', mode='w') as archivo:
        archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(datos)):
            archivo.writerow(datos[i])

    time.sleep(1)

    bar.next()

bar.finish()

# print ("%.2f sec" % (time.clock() - start))
