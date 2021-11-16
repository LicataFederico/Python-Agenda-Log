from tkinter import *
from eliminar import *
from base_datos import *

def elimina(variables, popupeliminar, elobjeto):
    popupeliminar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())

    borrar = Noticia.get(Noticia.id == lista[0])
    borrar.delete_instance()

    elobjeto.mostrar()


def eliminar(objeto):

    popupeliminar = Toplevel()
    vars_eliminar = crearformeliminar(popupeliminar, campos)
    
    Button(popupeliminar, text='eliminar', command=(lambda: elimina(vars_eliminar, popupeliminar, objeto))).pack()

    popupeliminar.grab_set()
    popupeliminar.focus_set()
    popupeliminar.wait_window()


