import requests
import json
import time
import csv
import datetime
from lxml import html


def ContadorDeVentasSimple():
    datos = []

    with open('data.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:

            id_item = row[0]

            url_item = (f'https://api.mercadolibre.com/items/MCO{id_item}')

            req_item = requests.get(url_item)

            data_decoded = json.loads(req_item.content)

            url = data_decoded["permalink"]

            print(url)

            req = requests.get(url)

            tree = html.fromstring(req.content)

            numero_ventas = tree.xpath('//div[1]/dl/div[1][contains(@class, "item-conditions")]')
            numero_ventas = " ".join(numero_ventas[0].text.split())

            x = [id_item, numero_ventas]
            datos.insert(0, x)

        with open('data_out.csv', mode='w') as archivo:
            archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for linea in range(len(datos)):
                archivo.writerow(datos[linea])
    return datos
