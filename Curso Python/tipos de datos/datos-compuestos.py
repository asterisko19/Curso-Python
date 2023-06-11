#creando una lista (se puede modificar)
lista = ["Juany Encinas","Juany",True,1.75]

#creando una tupla (no puede modificar)
tupla = ("Juany Encinas","Juany",True,1.75)

#esto es valido
lista[3] = "Maquinola"

#esto no es valido
#tupla[3] = "Maquinola"

print(lista[3])

#creando un conjunto (set) (mo se accede a elementos por indice, no almacena datos duplicados)

conjunto = {"Juany Encinas","Juany",True,1.75}
#print(conjunto[3]) -> no puede accceder al elemento

#creando un diccionario (dict) (la estructura es key : valu y separamos con coma)
diccionario = {
    'nombre' : 'Juany Encinas',
    'edad' : 19
}

print(diccionario['nombre'])