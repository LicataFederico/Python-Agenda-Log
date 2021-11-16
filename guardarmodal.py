from tkinter import *
from guardar import *
from base_datos import *


class Obs:

    observadores = []

    def notificando(self, *args):
        for observador in self.observadores:
            observador.notificar(self, *args)

    def agregando(self, obj):
        self.observadores.append(obj)

    def quitando(self, obj):
        self.observadores.remove(obj)


class Observando:
    def __init__(self, Obs):
        Obs.agregando(self)

    def guarda(variables, popupguardar, elobjeto):

        popupguardar.destroy()
        lista = []
        for variable in variables:
            lista.append(variable.get())
        noticia = Noticia()
        noticia.titulo = lista[0]
        noticia.descripcion = lista[1]
        noticia.save()
        elobjeto.mostrar()
        notificar(lista)


def guardar(objeto):

    popupguardar = Toplevel()
    vars_guardar = crearformguardar(popupguardar, campos)
    Button(
        popupguardar,
        text="guardar",
        command=(lambda: Observando.guarda(vars_guardar, popupguardar, objeto)),
    ).pack()
    popupguardar.grab_set()
    popupguardar.focus_set()
    popupguardar.wait_window()


def notificar(obj):
    newreg = Log()
    newreg.titulo = obj[0]
    newreg.descripcion = obj[1]
    newreg.save()
