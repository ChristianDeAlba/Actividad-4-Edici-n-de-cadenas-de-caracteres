from tkinter import *
from tkinter import filedialog

def explorar_archivos():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Seleccionar archivo", filetypes = (("Archivos de texto", "*.csv*"), ("todos los archivos", "*.*")))
    label_explorador_archivos.configure(text="Archivo abierto: "+filename)

ventana = Tk()
ventana.title('Leer CSV')
ventana.geometry("500x500")
ventana.config(background = "white")

label_explorador_archivos = Label(ventana, text = "Explorador de archivos usando Tkinter", width = 100, height = 4, fg = "blue")

boton_explorar = Button(ventana, text = "Explorar archivos", command = explorar_archivos)
boton_salir = Button(ventana, text = "Salir", command = exit)

label_explorador_archivos.grid(column = 1, row = 1)
boton_explorar.grid(column = 1, row = 2)
boton_salir.grid(column = 1, row = 3)

ventana.mainloop()
