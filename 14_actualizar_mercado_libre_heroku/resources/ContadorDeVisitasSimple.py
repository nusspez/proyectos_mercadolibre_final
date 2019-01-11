import requests
import json
import time
import csv
import datetime

def ContadorDeVisitasSimple(fecha_inicio, fecha_final):

    datos = []
    url = 'https://api.mercadolibre.com/items/MLM'

    url_headers = (f'/visits?date_from={fecha_inicio}T00:00:00.000-00:00&date_to={fecha_final}T00:00:00.000-00:00')
    headers = {'content-type': 'application/json'}

    lineas_documento = len(open('data.txt').readlines())

    with open('data.txt') as lineas:
        for linea in lineas:
            linea_n = linea.strip('\n')

            datos_item = url + linea_n

            datos_req = url + linea_n + url_headers

            req_item = requests.get(datos_item)

            req = requests.get(datos_req)

            json_convert_item = json.loads(req_item.text)

            json_convert = json.loads(req.text)

            category_item = json_convert_item["category_id"]
            seller_id = json_convert_item["seller_id"]

            item_id = json_convert["item_id"]
            date_to = json_convert["date_to"]
            date_from = json_convert["date_from"]
            total_visits = str(json_convert["total_visits"])
            visits_detail = str(json_convert["visits_detail"])

            datos_category = (f"https://api.mercadolibre.com/categories/{category_item}")
            req_category = requests.get(datos_category)
            json_convert_category = json.loads(req_category.text)
            nombre_categoria = json_convert_category["name"]
            mega_categoria = json_convert_category["path_from_root"]
            mega_categoria = mega_categoria[0]


            x = [seller_id, nombre_categoria,mega_categoria, item_id.strip('MCO'), category_item, total_visits]

            datos.insert(0, x)

            with open('data_out.csv', mode='w') as archivo:
                archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                archivo.writerow(["seller_id", "categoria","titulo categoria" , "id", "titulo mega categoria", "numero_de visitas"])
                for i in range(len(datos)):
                    archivo.writerow(datos[i])


            time.sleep(1)

    pass
