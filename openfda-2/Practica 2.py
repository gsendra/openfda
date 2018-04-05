import http.client
import json

SERVIDOR = "api.fda.gov"
RECURSO = "/drug/label.json"
limit = 200
busqueda = "/?search=active_ingredient:acetylsalicylic&limit={}".format(limit)

info = {'User-Agent': 'http-client'}

conexion = http.client.HTTPSConnection(SERVIDOR)
conexion.request("GET", RECURSO + busqueda, None, info)

respuesta1 = conexion.getresponse()

if respuesta1.status == 404:
    print("ERROR")
    exit(1)


resultado = respuesta1.read().decode("utf-8")
conexion.close()



aspirina = json.loads(resultado)['results'][0]

for numero in aspirina:
    print("* ID: {}".format(numero['id']))
    if numero['openfda']:
        fabricante = numero['openfda']['manufacturer_name'][0]
        print("  * Fabricante: {}".format(manufacturer))
    else:
        print("  *Fabricante no encontrado")