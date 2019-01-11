import requests
import json
import time
import csv
import datetime
from progress.bar import Bar


fecha = time.strftime("%d/%m/%y")

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

datos = []

print("introduce el access_token de la pagina")
access_token = input()
cust_id = '212058903'
url = (f'https://api.mercadolibre.com/users/{cust_id}/items/search?access_token={access_token}')
headers = {'content-type': 'application/json'}

r = requests.get(url)
items = json.loads(r.content)
items_l = items['results']
items_n = len(items['results'])

bar = Bar('Processing', max=items_n)


for i in range(items_n):

    datos_enero = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_enero)
    datos_febrero = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_febrero)
    datos_marzo = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_marzo)
    datos_abril = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_abril)
    datos_mayo = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_mayo)
    datos_junio = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_junio)
    datos_julio = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_julio)
    datos_agosto = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_agosto)
    datos_septiembre = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_septiembre)
    datos_octubre = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_octubre)
    datos_noviembre = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_noviembre)
    datos_diciembre = (f"https://api.mercadolibre.com/items/{items_l[i]}" + url_headers_diciembre)

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

    item_id_enero = json_convert_enero["item_id"]
    date_to_enero = json_convert_enero["date_to"]
    date_from_enero = json_convert_enero["date_from"]
    total_visits_enero = str(json_convert_enero["total_visits"])
    visits_detail_enero = str(json_convert_enero["visits_detail"])

    item_id_febrero = json_convert_febrero["item_id"]
    date_to_febrero = json_convert_febrero["date_to"]
    date_from_febrero = json_convert_febrero["date_from"]
    total_visits_febrero = str(json_convert_febrero["total_visits"])
    visits_detail_febrero = str(json_convert_febrero["visits_detail"])

    item_id_marzo = json_convert_marzo["item_id"]
    date_to_marzo = json_convert_marzo["date_to"]
    date_from_marzo = json_convert_marzo["date_from"]
    total_visits_marzo = str(json_convert_marzo["total_visits"])
    visits_detail_marzo = str(json_convert_marzo["visits_detail"])


    item_id_abril = json_convert_abril["item_id"]
    date_to_abril = json_convert_abril["date_to"]
    date_from_abril = json_convert_abril["date_from"]
    total_visits_abril = str(json_convert_abril["total_visits"])
    visits_detail_abril = str(json_convert_abril["visits_detail"])

    item_id_mayo = json_convert_mayo["item_id"]
    date_to_mayo = json_convert_mayo["date_to"]
    date_from_mayo = json_convert_mayo["date_from"]
    total_visits_mayo = str(json_convert_mayo["total_visits"])
    visits_detail_mayo = str(json_convert_mayo["visits_detail"])

    item_id_junio = json_convert_junio["item_id"]
    date_to_junio = json_convert_junio["date_to"]
    date_from_junio = json_convert_junio["date_from"]
    total_visits_junio = str(json_convert_junio["total_visits"])
    visits_detail_junio = str(json_convert_junio["visits_detail"])

    item_id_julio = json_convert_julio["item_id"]
    date_to_julio = json_convert_julio["date_to"]
    date_from_julio = json_convert_julio["date_from"]
    total_visits_julio = str(json_convert_julio["total_visits"])
    visits_detail_julio = str(json_convert_julio["visits_detail"])

    item_id_agosto = json_convert_agosto["item_id"]
    date_to_agosto = json_convert_agosto["date_to"]
    date_from_agosto = json_convert_agosto["date_from"]
    total_visits_agosto = str(json_convert_agosto["total_visits"])
    visits_detail_agosto = str(json_convert_agosto["visits_detail"])

    item_id_septiembre = json_convert_septiembre["item_id"]
    date_to_septiembre = json_convert_septiembre["date_to"]
    date_from_septiembre = json_convert_septiembre["date_from"]
    total_visits_septiembre = str(json_convert_septiembre["total_visits"])
    visits_detail_septiembre = str(json_convert_septiembre["visits_detail"])

    item_id_octubre = json_convert_octubre["item_id"]
    date_to_octubre = json_convert_octubre["date_to"]
    date_from_octubre = json_convert_octubre["date_from"]
    total_visits_octubre = str(json_convert_octubre["total_visits"])
    visits_detail_octubre = str(json_convert_octubre["visits_detail"])

    item_id_noviembre = json_convert_noviembre["item_id"]
    date_to_noviembre = json_convert_noviembre["date_to"]
    date_from_noviembre = json_convert_noviembre["date_from"]
    total_visits_noviembre = str(json_convert_noviembre["total_visits"])
    visits_detail_noviembre = str(json_convert_noviembre["visits_detail"])

    item_id_diciembre = json_convert_diciembre["item_id"]
    date_to_diciembre = json_convert_diciembre["date_to"]
    date_from_diciembre = json_convert_diciembre["date_from"]
    total_visits_diciembre = str(json_convert_diciembre["total_visits"])
    visits_detail_diciembre = str(json_convert_diciembre["visits_detail"])

    data_enero = [item_id_enero, date_to_enero, date_from_enero, total_visits_enero]
    data_febrero = [item_id_febrero, date_to_febrero, date_from_febrero, total_visits_febrero]
    data_marzo = [item_id_marzo, date_to_marzo, date_from_marzo, total_visits_marzo]
    data_abril = [item_id_abril, date_to_abril, date_from_abril, total_visits_abril]
    data_mayo = [item_id_mayo, date_to_mayo, date_from_mayo, total_visits_mayo]
    data_junio = [item_id_junio, date_to_junio, date_from_junio, total_visits_junio]
    data_julio = [item_id_julio, date_to_julio, date_from_julio, total_visits_julio]
    data_agosto = [item_id_agosto, date_to_agosto, date_from_agosto, total_visits_agosto]
    data_septiembre = [item_id_septiembre, date_to_septiembre, date_from_septiembre, total_visits_septiembre]
    data_octubre = [item_id_octubre, date_to_octubre, date_from_octubre, total_visits_octubre]
    data_noviembre = [item_id_noviembre, date_to_noviembre, date_from_noviembre, total_visits_noviembre]
    data_diciembre = [item_id_diciembre, date_to_diciembre, date_from_diciembre, total_visits_diciembre]

    x = [item_id_enero, total_visits_enero, total_visits_febrero, total_visits_marzo, total_visits_abril, total_visits_mayo, total_visits_junio, total_visits_julio, total_visits_agosto, total_visits_septiembre, total_visits_octubre, total_visits_noviembre, total_visits_diciembre]
    datos.insert(0, x)

    time.sleep(1)

    bar.next()

bar.finish()


with open('data_out.csv', mode='w') as archivo:
  archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  archivo.writerow(["id", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",fecha])
  for linea in range(items_n):
      archivo.writerow(datos[linea])





#
