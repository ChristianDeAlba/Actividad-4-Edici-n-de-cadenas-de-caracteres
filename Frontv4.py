import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from main import chunk_cadena_alterada

def leer_archivo(ruta):
    try:
        dataframe = pd.read_csv(ruta)
        return dataframe
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")

def generar_chunks_alterados(cadena):
    diccionario_chunks_alterados = chunk_cadena_alterada(cadena)
    return diccionario_chunks_alterados

def mostrar_chunks_alterados(cadena):
    diccionario_chunks_alterados = generar_chunks_alterados(cadena)
    cadena_chunks = ""
    for clave, subcadena in diccionario_chunks_alterados.items():
        cadena_chunks += f"{clave},{subcadena}\n"
    return cadena_chunks

def verificar_referencias():
    ruta = file_path.get()
    dataframe = leer_archivo(ruta)
    if dataframe is not None:
        cadena = dataframe.iloc[0, 3]
        posiciones = dataframe.iloc[:, 0]
        referencias = dataframe.iloc[:, 1]
        alteraciones = dataframe.iloc[:, 2]

        resultado = ""
        referencias_coinciden = True

        for i, (posicion, referencia, alteracion) in enumerate(zip(posiciones, referencias, alteraciones)):
            if cadena[posicion] != referencia:
                resultado += f"El carácter en la posición {posicion} no coincide con la referencia '{referencia}'\n"
                referencias_coinciden = False

        if referencias_coinciden:
            cadena_alterada = list(cadena)
            for posicion, alteracion in zip(posiciones, alteraciones):
                cadena_alterada[posicion] = alteracion

            cadena_alterada = ''.join(cadena_alterada)
            resultado += f"\nCadena alterada: {cadena_alterada}"
            generar_csv_chunks(cadena_alterada, posiciones, alteraciones)
            
            # Actualizar el campo de texto con la cadena alterada
            txt_resultado.delete(1.0, tk.END)
            txt_resultado.insert(tk.END, resultado)
            
            # Mostrar la cadena de chunks alterada en otro campo de texto
            txt_chunks_alterados.delete(1.0, tk.END)
            txt_chunks_alterados.insert(tk.END, mostrar_chunks_alterados(cadena_alterada))

def obtener_cadena_chunks(cadena_alterada):
    chunks = [cadena_alterada[i:i+10] for i in range(0, len(cadena_alterada), 10)]
    cadena_chunks = ""
    for i, chunk in enumerate(chunks):
        cadena_chunks += f"{i},{chunk}\n"
    return cadena_chunks

def abrir_archivo():
    file_path.set(filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")]))

def generar_csv_chunks(cadena, posiciones, alteraciones):
    # Implementa la generación del CSV con los chunks alterados
    # Aquí puedes usar los datos de posiciones y alteraciones para generar el CSV
    pass

# Crear la ventana principal
root = tk.Tk()
root.title("Verificador de Referencias")
root.geometry("600x500")  # Tamaño de la ventana

file_path = tk.StringVar()

# Botón para abrir el archivo
btn_abrir = tk.Button(root, text="Abrir archivo CSV", command=abrir_archivo)
btn_abrir.pack(pady=10)

# Botón para verificar referencias
btn_verificar = tk.Button(root, text="Verificar referencias", command=verificar_referencias)
btn_verificar.pack(pady=5)

# Área de texto para mostrar los resultados
txt_resultado = tk.Text(root, height=10, width=60)
txt_resultado.pack(pady=10)

# Área de texto para mostrar la cadena de chunks alterada
txt_chunks_alterados = tk.Text(root, height=10, width=60)
txt_chunks_alterados.pack(pady=10)

root.mainloop()
