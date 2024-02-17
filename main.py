import json

def cargar_datos(ruta):
    with open(ruta) as contenido:
        base_de_datos = json.load(contenido)
        for entrada in base_de_datos:
            duracion = entrada.get('duracion', '')
            print(duracion)

if __name__ == '__main__':
    ruta = 'automatas/base_de_datos.json'
    cargar_datos(ruta)