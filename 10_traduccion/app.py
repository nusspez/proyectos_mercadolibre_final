import goslate
import csv
import time



gs = goslate.Goslate()

datos = []

with open('data.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:

        ads_asin = row[0]
        ads_title = row[1]
        ads_descor = row[2]
        ads_deslar = row[3]

        traduccion_ads_title = gs.translate(row[1], 'es')
        traduccion_ads_descor = gs.translate(row[2], 'es')
        traduccion_ads_deslar = gs.translate(row[3], 'es')


        x = [ads_asin, traduccion_ads_title.strip(','), traduccion_ads_descor.strip(','), traduccion_ads_deslar.strip(',')]
        datos.insert(0, x)

        with open('data_out.csv', mode='w') as archivo:
            archivo = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(datos)):
                archivo.writerow(datos[i])
                
        time.sleep(1)
