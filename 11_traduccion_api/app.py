import goslate
import csv
import time
import requests
import json

print('insterte la url del API')

datos = []

gs = goslate.Goslate()

url = input()

req = requests.get(url)

data_decoded = json.loads(req.content)

numero_productos = len(data_decoded["Ads"])

for i in range(numero_productos):

    ads_asin = data_decoded["Ads"][i]["ASIN"]
    ads_title = data_decoded["Ads"][i]["Title"]
    ads_descor = data_decoded["Ads"][i]["DESCOR"]
    ads_deslar = data_decoded["Ads"][i]["DESLAR"]

    traduccion_ads_title = gs.translate(ads_title, 'es')
    traduccion_ads_descor = gs.translate(ads_descor, 'es')
    traduccion_ads_deslar = gs.translate(ads_deslar, 'es')

    x = [ads_asin, traduccion_ads_title.strip(','), traduccion_ads_descor.strip(','), traduccion_ads_deslar.strip(',')]
    datos.insert(0, x)

    with open('data_out.csv', mode='w') as archivo:
        archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(datos)):
            archivo.writerow(datos[i])

    time.sleep(1)
