import pandas as pd

dataframe = pd.read_csv('dataset.csv')

def cadena_original():
    cadena_original = dataframe.iloc[0, 3]
    return cadena_original

def longitud_cadena_original():
    return len(cadena_original())

def lista_posiciones():
    lista_posiciones = []
    for i in range(dataframe.shape[0]):
        posicion = dataframe.iloc[i, 0]
        lista_posiciones.append(posicion)
    return lista_posiciones

def lista_referencias():
    lista_referencias = []
    for i in range(dataframe.shape[0]):
        referencia = dataframe.iloc[i, 1]
        lista_referencias.append(referencia)
    return lista_referencias

def lista_alteraciones():
    lista_alteraciones = []
    for i in range(dataframe.shape[0]):
        alteracion = dataframe.iloc[i,2]
        lista_alteraciones.append(alteracion)
    return(lista_alteraciones)

def diccionario_caracteres():
    diccionario_caracteres = {}
    cadena = cadena_original()
    lista_caracteres = list(cadena)
    for i in range(len(lista_caracteres)):
        diccionario_caracteres[i] = lista_caracteres[i]
    return diccionario_caracteres

def posicion_alteracion():
    diccionario_posicion_alteracion = zip(lista_posiciones(), lista_alteraciones())
    return dict(diccionario_posicion_alteracion)

def chunk(diccionario_caracteres):
    alteracion_diccionario = posicion_alteracion()
    
    diccionario = diccionario_caracteres.items()
    diccionario_lista = list(diccionario)
    numero_chunk = int(input(f'Ingrese el numero del chunk del que quiere ver los cambios: '))
    if numero_chunk == 0:
        chunk_elegido = diccionario_lista[:10]
        for  key, value in chunk_elegido:
            print (f"Posición {key}: {value} valor")
        print(chunk_elegido)
    elif numero_chunk > 0:
        chunk_elegido = (diccionario_lista[(numero_chunk)*5:(numero_chunk*5)+10])
        for key, value in chunk_elegido:
            print(f'Posicion {key}: {value} valor')
        print(chunk_elegido)
    chunk(diccionario_caracteres)
        

# Llamada a la función diccionario_caracteres y luego a la función chunk
chunk(diccionario_caracteres())