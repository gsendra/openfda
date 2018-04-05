import http.client
import json

SERVIDOR = "api.fda.gov"
RECURSO = "/drug/label.json"
info = {'User-Agent': 'http-client'}


conexion = http.client.HTTPSConnection(SERVIDOR)

#solicitud
try:
    conexion.request("GET", RECURSO, None, info)
except:
    print("Error")
    exit(1)

print("Solicitud aceptada")

#respuesta
respuesta1 = conexion.getresponse()

if respuesta1.status == 404:
    print("Recurso {} no encontrado".format(RECURSO))
    exit(1)

medicamentos = respuesta1.read().decode("utf-8")
conexion.close()

medicamento = json.loads(medicamentos)
meta = medicamento['meta']
limit = meta['results']['limit']


medicamento= medicamento['results'][0]
#diccionario con la respuesta


#Seleccionamos la información de interés
nombre= medicamento['openfda']['substance_name'][0]

id= medicamento['id']

proposito= medicamento['purpose'][0]

fabricante= medicamento['openfda']['manufacturer_name'][0]


print("Nombre: {}".format(nombre))
print("Id: {}".format(id))
print("Proposito: {}".format(proposito))
print("Fabricante: {}".format(fabricante))


#PROGRAMA2

#objetos recibidos:quiero 10, ponemos el limit, definido en el programa anterior en 10

conexion.request("GET", RECURSO + '?limit=10', None, info)

#respuesta

respuesta2 = conexion.getresponse()

if respuesta2.status == 404:
    print("ERROR")
    exit(1)

medicamentos = respuesta2.read().decode("utf-8")

conexion.close()

medicamento = json.loads(medicamentos)
medicamento = medicamento['results']

for numero in medicamento:
    print("Medicamento: {}".format(numero['id']))




