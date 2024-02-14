import pandas as pd

def leer_archivo():
    dataframe = pd.read_csv('dataset.csv')
    return dataframe

def cadena_original():
    dataframe = leer_archivo()
    cadena = dataframe.iloc[0, 3]
    return cadena

def diccionario_caracteres():
    diccionario_caracteres = {}
    cadena = cadena_original()
    for i in range(len(cadena)):
        diccionario_caracteres[i] = cadena[i]
    return diccionario_caracteres

def posiciones():
    dataframe = leer_archivo()
    lista_posiciones = []
    for i in range(dataframe.shape[0]):
        posicion = dataframe.iloc[i, 0]
        lista_posiciones.append(posicion)
    return lista_posiciones
        
def referencias():
    dataframe = leer_archivo()
    lista_referencias = []
    for i in range(dataframe.shape[0]):
        referencia = dataframe.iloc[i, 1]
        lista_referencias.append(referencia)
    return lista_referencias

def alteraciones():
    dataframe = leer_archivo()
    lista_alteraciones = []
    for i in range(dataframe.shape[0]):
        alteracion = dataframe.iloc[i, 2]
        lista_alteraciones.append(alteracion)
    return lista_alteraciones
        
def verificar_referencias():
    posicion_referencia = dict(zip(posiciones(), referencias()))
    cadena = cadena_original()
    referencias_coinciden = True  # Variable de bandera para verificar si todas las referencias coinciden
    # Itera sobre las claves del diccionario posicion_referencia
    for posicion, referencia in posicion_referencia.items():
        # Verifica si la posición está dentro del rango de la cadena
        if posicion < len(cadena):
            # Comprueba si el carácter en la posición de la referencia coincide con el carácter en la cadena
            if cadena[posicion] == referencia:
                print(f"El carácter en la posición {posicion} coincide con la referencia '{referencia}'")
            else:
                print(f"El carácter en la posición {posicion} no coincide con la referencia '{referencia}'")
                referencias_coinciden = False  # Si alguna referencia no coincide, actualiza la variable de bandera
        else:
            print(f"La posición {posicion} está fuera del rango de la cadena")
            referencias_coinciden = False  # Si alguna posición está fuera del rango, actualiza la variable de bandera
    
    if referencias_coinciden:
        # Llama a la función que deseas ejecutar si todas las referencias coinciden
        cadena_alterada = si_coinciden(posiciones(), alteraciones())
        generar_csv_chunks(cadena_alterada)

def si_coinciden(posiciones, alteraciones):
    # Obtiene la cadena original
    cadena_alterada = list(cadena_original())  # Convierte la cadena en una lista para modificarla
    
    # Asigna los caracteres de alteración en las posiciones dadas
    for posicion, alteracion in zip(posiciones, alteraciones):
        cadena_alterada[posicion] = alteracion
        
    # Devuelve la cadena alterada
    cadena_alterada = ''.join(cadena_alterada)  # Convierte la lista de nuevo en cadena
    print("Cadena alterada:", cadena_alterada)
    return cadena_alterada
    
def chunks_cadena_original():
    cadena = cadena_original()
    clave = 0
    diccionario_chuncks_cadena_original = {}
    for i in range(0, len(cadena), 5):
        subcadena = cadena[i:i + 10]
        diccionario_chuncks_cadena_original[clave] = subcadena
        clave += 1
    return diccionario_chuncks_cadena_original

def chunk_cadena_alterada(cadena):
    clave = 0
    diccionario_chunks_cadena_alterada = {}
    for i in range(0, len(cadena), 5):
        subcadena = cadena[i:i + 10]
        diccionario_chunks_cadena_alterada[clave] = subcadena
        clave += 1
    return diccionario_chunks_cadena_alterada

def generar_csv_chunks(cadena):
    diccionario_chunks_alterados = chunk_cadena_alterada(cadena)
    dfb = pd.DataFrame.from_dict(diccionario_chunks_alterados, orient='index', columns=['Subcadena'])
    dfb.to_csv('chunks_cadena_alterada.csv', index_label='Chunk')
    print("Archivo 'chunks_cadena_alterada.csv' generado correctamente.")

diccionario_chunks_originales = chunks_cadena_original()

dfa = pd.DataFrame.from_dict(diccionario_chunks_originales, orient='index', columns=['Subcadena'])

dfa.to_csv('chunks_cadena_original.csv', index_label='Chunk')

print(f'\nCadena original: {cadena_original()}\n')
print(f'Longitud de la cadena: {len(cadena_original())}\n')
print(f'Posiciones: {posiciones()}\n')
print(f'Referencias: {referencias()}\n')
print(f'Alteraciones:{alteraciones()}\n')

verificar_referencias()
