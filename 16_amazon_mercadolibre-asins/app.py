from progress.bar import Bar
import csv
import time
import requests
import json

datos = []

url = 'https://api.mercadolibre.com/items?access_token='


headers = {'content-type': 'application/json'}

# start = time.clock()

print("introduce el access_token")
access_token = input()

print("introduce el run_token")
RUN_TOKEN = input()

API_KEY = 'tTiMYTuTwX04'

params = {
  "api_key": str(API_KEY),
  "format": "JSON"
}

r = requests.get(f'https://www.parsehub.com/api/v2/runs/{str(RUN_TOKEN)}/data', params=params)

status_code = r.status_code
status = r.content

if status_code == 200:
    print('la conexion con parsehub es correcta')

    data_decoded = json.loads(r.content)

    numero_productos = len(data_decoded["Ads"])


    bar = Bar('Processing', max=numero_productos)

    i = 0

    for i in range(numero_productos - 1):

        seller_custom_field = data_decoded['Ads'][i]['ASIN']
        title = data_decoded['Ads'][i]['TITULOPUBLICACION']
        category_id = data_decoded['Ads'][i]['IDCATEGORIA']
        price = data_decoded['Ads'][i]['PRECIOCOP']
        currency_id = 'COP'
        available_quantity = '10'
        buying_mode = 'buy_it_now'
        listing_type_id = 'gold_special'
        condition = 'new'
        description = data_decoded['Ads'][i]['DESCRIPTION']
        video_id = data_decoded['Ads'][i]['YOUTUBE']
        warranty = data_decoded['Ads'][i]['WARRANTY']

        source1 = data_decoded['Ads'][i]['URLPhoto1']
        source2 = data_decoded['Ads'][i]['URLMYPIC']
        source3 = data_decoded['Ads'][i]['URLPhoto2']
        source4 = data_decoded['Ads'][i]['URLPhoto3']
        source5 = data_decoded['Ads'][i]['URLPhoto4']
        source6 = data_decoded['Ads'][i]['URLPhoto5']
        ads_envio = data_decoded['Ads'][i]['Ads_envio']


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

        r = requests.post(url + access_token, data=json.dumps(data_product),headers=headers)

        status_code_publicacion = r.status_code
        status_publicacion = r.content

        if status_code_publicacion == 200:
            print('los articulos de maercado libre han sido publicados')
            json_convert = json.loads(r.content)

            id_item = json_convert["id"]

            url_value = (f'https://api.mercadolibre.com/items/{id_item}?access_token={access_token}')

            data = {'seller_custom_field':str(seller_custom_field)}

            r = requests.put(url_value, data = json.dumps(data))

            x = [seller_custom_field,id_item.strip("MLM"),title,category_id,price,currency_id,available_quantity,buying_mode,listing_type_id,condition,description,video_id,warranty,source1,source2,source3,source4,source5,source6,ads_envio]
            datos.insert(0, x)

            with open('data_out.csv', mode='w') as archivo:
                archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(len(datos)):
                    archivo.writerow(datos[i])

            time.sleep(1)

            bar.next()

        else:
            print(status_publicacion)
else:
    print(status)

bar.finish()

# print ("%.2f sec" % (time.clock() - start))
