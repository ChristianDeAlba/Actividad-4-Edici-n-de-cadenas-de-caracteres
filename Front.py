import tkinter as tk

root = tk.Tk()
root.title("Visualizador de Resultados")
root.geometry("600x500")  # Tamaño de la ventana

file_path = tk.StringVar()
cadena_original_text = tk.StringVar()
posiciones_text = tk.StringVar()
alteraciones_text = tk.StringVar()
chunk_text = tk.StringVar()

# Botón para abrir el archivo
btn_abrir = tk.Button(root, text="Abrir archivo CSV")
btn_abrir.pack(pady=10)

# Botón para mostrar los resultados
btn_mostrar = tk.Button(root, text="Mostrar resultados")
btn_mostrar.pack(pady=5)

# Etiqueta para mostrar la cadena original
lbl_cadena_original = tk.Label(root, text="Cadena Original:")
lbl_cadena_original.pack()
lbl_cadena_original_result = tk.Label(root, textvariable=cadena_original_text)
lbl_cadena_original_result.pack()

# Etiqueta para mostrar las posiciones
lbl_posiciones = tk.Label(root, text="Posiciones:")
lbl_posiciones.pack()
lbl_posiciones_result = tk.Label(root, textvariable=posiciones_text)
lbl_posiciones_result.pack()

# Etiqueta para mostrar las alteraciones
lbl_alteraciones = tk.Label(root, text="Alteraciones:")
lbl_alteraciones.pack()
lbl_alteraciones_result = tk.Label(root, textvariable=alteraciones_text)
lbl_alteraciones_result.pack()

# Campo de entrada para el número de chunk
lbl_chunk = tk.Label(root, text="Número de chunk:")
lbl_chunk.pack()
entry_chunk = tk.Entry(root)
entry_chunk.pack()

# Botón para mostrar el chunk seleccionado
btn_mostrar_chunk = tk.Button(root, text="Mostrar Chunk")
btn_mostrar_chunk.pack(pady=5)

# Etiqueta para mostrar el chunk
lbl_chunk_result = tk.Label(root, textvariable=chunk_text)
lbl_chunk_result.pack()

root.mainloop()