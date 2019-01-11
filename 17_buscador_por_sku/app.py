import requests
import json
import csv
from progress.bar import Bar

datos = []

API_KEY = 'tTiMYTuTwX04'

RUN_TOKEN = input("introduce el run token key")

params = {
  "api_key": str(API_KEY),
  "format": "JSON"
}

req_data = requests.get(f'https://www.parsehub.com/api/v2/runs/{str(RUN_TOKEN)}/data', params=params)
data_decoded_data = json.loads(req_data.content)
numero_productos_data = len(data_decoded_data["Ads"])

ACCESS_TOKEN = "APP_USR-2825701065362178-112103-6ea692d4819957384bf8fdc1774d96bb-212058903"
Cust_id = "212058903"


bar = Bar('Processing', max=numero_productos_data)
i = 0

for i in range(numero_productos_data):

    seller_custom_field = data_decoded_data["Ads"][i]["ASIN"]

    req = requests.get(f"https://api.mercadolibre.com//users/{Cust_id}/items/search?sku={seller_custom_field}&status=active&access_token={ACCESS_TOKEN}")
    data_decoded = json.loads(req.content)
    resultados = data_decoded["results"]

    x = [resultados, seller_custom_field]
    datos.insert(0, x)

    with open('data_out.csv', mode='w') as archivo:
        archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(datos)):
            archivo.writerow(datos[i])

    bar.next()


bar.finish()
