from tkinter import *
from modificar import *
from base_datos import *


def modifica(variables, popupmodificar, elobjeto):
    popupmodificar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())

    actualizar = Noticia.update(titulo=lista[1], descripcion=lista[2]).where(
        Noticia.id == lista[0]
    )
    actualizar.execute()

    elobjeto.mostrar()


def modificar(objeto):

    popupmodificar = Toplevel()
    vars_modificar = crearformmodificar(popupmodificar, campos)
    print(vars_modificar)

    Button(
        popupmodificar,
        text="modificar",
        command=(lambda: modifica(vars_modificar, popupmodificar, objeto)),
    ).pack()

    popupmodificar.grab_set()
    popupmodificar.focus_set()
    popupmodificar.wait_window()
