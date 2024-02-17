import json

def cargar_datos(ruta):
    with open(ruta) as contenido:
        resultado = json.load(contenido)
        for entrada in resultado:
            duracion = entrada.get('duracion', '')
            print(resultado)

if __name__ == '__main__':
    ruta = 'datos.json'
    cargar_datos(ruta)