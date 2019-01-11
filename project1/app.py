from progress.bar import Bar
import requests
import csv
import time
import json
import datetime

fecha = time.strftime("%d/%m/%y")

datos = []
lineas_documento = len(open('data.txt').readlines())
bar = Bar('Processing', max=lineas_documento)



url_headers_diciembre = "/visits?date_from=2018-12-01T00:00:00.000-00:00&date_to=2018-12-31T00:00:00.000-00:00"
url_headers_noviembre = "/visits?date_from=2018-11-01T00:00:00.000-00:00&date_to=2018-11-30T00:00:00.000-00:00"
url_headers_octubre = "/visits?date_from=2018-10-01T00:00:00.000-00:00&date_to=2018-10-31T00:00:00.000-00:00"
url_headers_septiembre = "/visits?date_from=2018-09-01T00:00:00.000-00:00&date_to=2018-09-30T00:00:00.000-00:00"
url_headers_agosto = "/visits?date_from=2018-08-01T00:00:00.000-00:00&date_to=2018-08-30T00:00:00.000-00:00"
url_headers_julio = "/visits?date_from=2018-07-01T00:00:00.000-00:00&date_to=2018-07-31T00:00:00.000-00:00"
url_headers_junio = "/visits?date_from=2018-06-01T00:00:00.000-00:00&date_to=2018-06-30T00:00:00.000-00:00"
url_headers_mayo = "/visits?date_from=2018-05-01T00:00:00.000-00:00&date_to=2018-05-31T00:00:00.000-00:00"
url_headers_abril = "/visits?date_from=2018-04-01T00:00:00.000-00:00&date_to=2018-04-30T00:00:00.000-00:00"
url_headers_marzo = "/visits?date_from=2018-03-01T00:00:00.000-00:00&date_to=2018-03-31T00:00:00.000-00:00"
url_headers_febrero = "/visits?date_from=2018-02-01T00:00:00.000-00:00&date_to=2018-02-28T00:00:00.000-00:00"
url_headers_enero = "/visits?date_from=2018-01-01T00:00:00.000-00:00&date_to=2018-01-31T00:00:00.000-00:00"

with open('data.txt') as lineas:
    for linea in lineas:
        linea_n = linea.strip('\n')

        datos_item = (f'https://api.mercadolibre.com/items/MLM{linea_n}')

        datos_enero = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_enero)
        datos_febrero = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_febrero)
        datos_marzo = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_marzo)
        datos_abril = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_abril)
        datos_mayo = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_mayo)
        datos_junio = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_junio)
        datos_julio = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_julio)
        datos_agosto = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_agosto)
        datos_septiembre = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_septiembre)
        datos_octubre = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_octubre)
        datos_noviembre = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_noviembre)
        datos_diciembre = (f"https://api.mercadolibre.com/items/MCO{linea_n}" + url_headers_diciembre)

        req_item = requests.get(datos_item)
        req_enero = requests.get(datos_enero)
        req_febrero = requests.get(datos_febrero)
        req_marzo = requests.get(datos_marzo)
        req_abril = requests.get(datos_abril)
        req_mayo = requests.get(datos_mayo)
        req_junio = requests.get(datos_junio)
        req_julio = requests.get(datos_julio)
        req_agosto = requests.get(datos_agosto)
        req_septiembre = requests.get(datos_septiembre)
        req_octubre = requests.get(datos_octubre)
        req_noviembre = requests.get(datos_noviembre)
        req_diciembre = requests.get(datos_diciembre)

        json_convert_item = json.loads(req_item.text)
        json_convert_enero = json.loads(req_enero.text)
        json_convert_febrero = json.loads(req_febrero.text)
        json_convert_marzo = json.loads(req_marzo.text)
        json_convert_abril = json.loads(req_abril.text)
        json_convert_mayo = json.loads(req_mayo.text)
        json_convert_junio = json.loads(req_junio.text)
        json_convert_julio = json.loads(req_julio.text)
        json_convert_agosto = json.loads(req_agosto.text)
        json_convert_septiembre = json.loads(req_septiembre.text)
        json_convert_octubre = json.loads(req_octubre.text)
        json_convert_noviembre = json.loads(req_noviembre.text)
        json_convert_diciembre = json.loads(req_diciembre.text)

        titulo_item = json_convert_item["title"]
        category_item = json_convert_item["category_id"]

        item_id_enero = json_convert_enero["item_id"]
        total_visits_enero = str(json_convert_enero["total_visits"])
        visits_detail_enero = str(json_convert_enero["visits_detail"])

        item_id_febrero = json_convert_febrero["item_id"]
        total_visits_febrero = str(json_convert_febrero["total_visits"])
        visits_detail_febrero = str(json_convert_febrero["visits_detail"])

        item_id_marzo = json_convert_marzo["item_id"]
        total_visits_marzo = str(json_convert_marzo["total_visits"])
        visits_detail_marzo = str(json_convert_marzo["visits_detail"])


        item_id_abril = json_convert_abril["item_id"]
        total_visits_abril = str(json_convert_abril["total_visits"])
        visits_detail_abril = str(json_convert_abril["visits_detail"])

        item_id_mayo = json_convert_mayo["item_id"]
        total_visits_mayo = str(json_convert_mayo["total_visits"])
        visits_detail_mayo = str(json_convert_mayo["visits_detail"])

        item_id_junio = json_convert_junio["item_id"]
        total_visits_junio = str(json_convert_junio["total_visits"])
        visits_detail_junio = str(json_convert_junio["visits_detail"])

        item_id_julio = json_convert_julio["item_id"]
        total_visits_julio = str(json_convert_julio["total_visits"])
        visits_detail_julio = str(json_convert_julio["visits_detail"])

        item_id_agosto = json_convert_agosto["item_id"]
        total_visits_agosto = str(json_convert_agosto["total_visits"])
        visits_detail_agosto = str(json_convert_agosto["visits_detail"])

        item_id_septiembre = json_convert_septiembre["item_id"]
        total_visits_septiembre = str(json_convert_septiembre["total_visits"])
        visits_detail_septiembre = str(json_convert_septiembre["visits_detail"])

        item_id_octubre = json_convert_octubre["item_id"]
        total_visits_octubre = str(json_convert_octubre["total_visits"])
        visits_detail_octubre = str(json_convert_octubre["visits_detail"])

        item_id_noviembre = json_convert_noviembre["item_id"]
        total_visits_noviembre = str(json_convert_noviembre["total_visits"])
        visits_detail_noviembre = str(json_convert_noviembre["visits_detail"])

        item_id_diciembre = json_convert_diciembre["item_id"]
        total_visits_diciembre = str(json_convert_diciembre["total_visits"])
        visits_detail_diciembre = str(json_convert_diciembre["visits_detail"])

        datos_category = (f"https://api.mercadolibre.com/categories/{category_item}")
        req_category = requests.get(datos_category)
        json_convert_category = json.loads(req_category.text)
        nombre_categoria = json_convert_category["name"]
        mega_categoria = json_convert_category["path_from_root"]
        mega_categoria = mega_categoria[0]

        data_enero = [titulo_item, category_item, item_id_enero, total_visits_enero]
        data_febrero = [titulo_item, category_item, item_id_febrero, total_visits_febrero]
        data_marzo = [titulo_item, category_item, item_id_marzo, total_visits_marzo]
        data_abril = [titulo_item, category_item, item_id_abril, total_visits_abril]
        data_mayo = [titulo_item, category_item, item_id_mayo, total_visits_mayo]
        data_junio = [titulo_item, category_item, item_id_junio, total_visits_junio]
        data_julio = [titulo_item, category_item, item_id_julio, total_visits_julio]
        data_agosto = [titulo_item, category_item, item_id_agosto, total_visits_agosto]
        data_septiembre = [titulo_item, category_item, item_id_septiembre, total_visits_septiembre]
        data_octubre = [titulo_item, category_item, item_id_octubre, total_visits_octubre]
        data_noviembre = [titulo_item, category_item, item_id_noviembre, total_visits_noviembre]
        data_diciembre = [titulo_item, category_item, item_id_diciembre, total_visits_diciembre]

        x = [titulo_item,nombre_categoria,mega_categoria, item_id_enero.strip('MCO'), category_item, total_visits_enero, total_visits_febrero, total_visits_marzo, total_visits_abril, total_visits_mayo, total_visits_junio, total_visits_julio, total_visits_agosto, total_visits_septiembre, total_visits_octubre, total_visits_noviembre, total_visits_diciembre]

        datos.insert(0, x)

        with open('data_out.csv', mode='w') as archivo:
            archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            archivo.writerow(["titulo", "categoria","titulo categoria" , "id", "titulo mega categoria", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic",fecha])
            for i in range(len(datos)):
                archivo.writerow(datos[i])

        time.sleep(1)

        bar.next()

bar.finish()
