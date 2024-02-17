import json

base_de_datos = []

for i in range(2):
    persona = {}
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = input('Ingrese su edad: ')
    sexo = input('Ingrese su sexo: ')
    peso = input('Ingrese su peso: ')
    altura = input('Ingrese su altura: ')

    persona['nombre'] = nombre
    persona['apellido'] = apellido
    persona['edad'] = edad
    persona['sexo'] = sexo
    persona['peso'] = peso
    persona['altura'] = altura
    base_de_datos.append(persona)

print(base_de_datos)

with open('base_de_datos.json' , 'w') as archivo:
    json.dump(base_de_datos, archivo)
    print("archivo guardado")
    print("hola")