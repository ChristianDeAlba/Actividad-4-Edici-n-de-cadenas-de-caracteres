import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

dataframe = None

def abrir_archivo():
    global dataframe
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        dataframe = pd.read_csv(archivo)
        txt_cadena_original_print()

def cadena_original():
    if dataframe is not None and not dataframe.empty:
        return dataframe.iloc[0, 3]
    return ""

def txt_cadena_original_print():
    cadena = cadena_original()
    txt_cadena_original.config(state="normal")
    txt_cadena_original.delete('1.0', tk.END)
    txt_cadena_original.insert(tk.END, cadena)
    txt_cadena_original.config(state="disabled")
    root.update()

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
    return lista_alteraciones

def dicc_posicion_alteracion():
    return dict(zip(lista_posiciones(), lista_alteraciones()))

def diccionario_caracteres():
    diccionario_caracteres = {}
    cadena = cadena_original()
    lista_caracteres = list(cadena)
    for i in range(len(lista_caracteres)):
        diccionario_caracteres[i] = lista_caracteres[i]
    return diccionario_caracteres

def mostrar_resultados():
    pass  # Agrega la lógica para mostrar los resultados

def mostrar_chunk():
    numero_chunk = entry_chunk.get()
    if numero_chunk.isdigit():
        numero_chunk = int(numero_chunk)
        print(f'El chunk elegido es el: {numero_chunk}')
        recorrer_lista_caracteres_cadena_original(numero_chunk)
        
        # Aquí puedes llamar a la función para mostrar el chunk seleccionado
    else:
        messagebox.showerror("Error", "El número de chunk debe ser un valor entero.")
    
def recorrer_lista_caracteres_cadena_original(chunk):
    posicion_alteracion = dicc_posicion_alteracion()
    if chunk == 0:
        inicio = 0
        fin = 10
        cadenas = []
        for i in range(inicio,fin):
            for key, value in posicion_alteracion.items():
                if key == i:
                    cadena = cadena_original()
                    alterada =  cadena[:key] + value + cadena[key+1:]
                    cadenas.append(alterada)
                    print(f'Alteracion en la posicion {key} es {value}')
        imprimir_cadenas(cadenas)
    elif chunk > 0:
        inicio = chunk * 5
        fin = inicio + 10
        cadenas = []
        for i in range(inicio, fin):
            for key, value in posicion_alteracion.items():
                if key == i:
                    cadena = cadena_original()
                    alterada = cadena[:key] + value + cadena[key+1:]
                    cadenas.append(alterada)
                    print(f'Alteracion en la posicion {key} es {value}')
        imprimir_cadenas(cadenas)
    elif cadenas == '':
        print('No hay cambios')

def imprimir_cadenas(cadenas):
    txt_cadenas_modificadas.config(state="normal")
    txt_cadenas_modificadas.delete('1.0', tk.END)
    txt_cadenas_modificadas.insert(tk.END, cadenas)
    txt_cadenas_modificadas.config(state="disabled")
    pass
    
    

root = tk.Tk()
root.title("Visualizador de Resultados")
root.geometry("1060x500")  # Tamaño de la ventana

# Botón para abrir el archivo
btn_abrir = tk.Button(root, text="Abrir archivo CSV", command=abrir_archivo)
btn_abrir.place(x=570, y=450)

# Botón para mostrar los resultados
btn_mostrar = tk.Button(root, text="Mostrar resultados", command=mostrar_resultados)
btn_mostrar.place(x=450, y=450)

# Etiqueta para mostrar la cadena original
lbl_cadena_original = tk.Label(root, text="Cadena Original:")
lbl_cadena_original.place(x=10, y=10)
txt_cadena_original = tk.Text(root, height=2, width=130, state="disabled")
txt_cadena_original.place(x=10, y=30)

# Mostrar cadenas
txt_cadenas_modificadas = tk.Text(root, height=10, width=130, state="disabled")
txt_cadenas_modificadas.place(x=10, y=140)

# Campo de entrada para el número de chunk
lbl_chunk = tk.Label(root, text="Número de chunk:")
lbl_chunk.place(x=10, y=90)
entry_chunk = tk.Entry(root)
entry_chunk.place(x=10, y=110)

# Botón para mostrar el chunk seleccionado
btn_mostrar_chunk = tk.Button(root, text="Mostrar Chunk Modificado", command=mostrar_chunk)
btn_mostrar_chunk.place(x=150, y=105)

root.mainloop()
