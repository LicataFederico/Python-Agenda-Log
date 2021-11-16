from tkinter import *
from tkinter.messagebox import *
import base_datos
from tkinter import ttk
from tkinter.ttk import Treeview
from temas.OpcionTemas import EleccionTema
from guardarmodal import *
from eliminarmodal import *
from modificarmodal import *
import guardarmodal


class Producto(guardarmodal.Obs):
    def __init__(self, window):
        self.observerBD = guardarmodal.Observando(self)
        self.tree = ttk.Treeview
        self.root = window
        self.root.title("Entrega Final")
        # VENTANA
        self.encabezado = Label(
            self.root,
            text="Ingrese sus datos",
            bg="black",
            fg="white",
            height=1,
            width=60,
            font=("system", 16, "bold"),
        )
        self.encabezado.grid(
            row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W + E
        )

        self.tree = ttk.Treeview(height=15, columns=4)
        self.tree["columns"] = ("uno", "dos", "tres")
        self.tree.grid(row=7, column=0, columnspan=3)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("uno", text="Título", anchor=CENTER)
        self.tree.heading("dos", text="Descripción", anchor=CENTER)
        self.tree.heading("tres", text="Fecha", anchor=CENTER)

        self.style = ttk.Style()
        self.style.configure(".", font=("Helvetica", 8), foreground="black")
        self.style.configure(
            "Treeview",
            background="khaki",
            foreground="black",
            fieldbackground="black",
        )
        self.style.map("Treeview", background=[("selected", "black")])

        ################################################## MBOTONES ##########################################################################
        Button(self.root, text="Guardar", command=lambda: self.guardar_registro()).grid(
            row=11, column=0
        )
        Button(
            self.root, text="Eliminar", command=lambda: self.eliminar_registro()
        ).grid(row=11, column=1)
        Button(
            self.root, text="Modificar", command=lambda: self.modificar_registro()
        ).grid(row=11, column=2)
        Button(self.root, text="Logs", command=lambda: self.logs()).grid(
            row=11, column=3
        )

    ################################################## LOGS Y TREEVIEW DE VENTANA SECUNDARIA ##########################################################################

    def logs(self):
        pantalla_log = Toplevel()
        pantalla_log.title("Log")
        pantalla_log.titulo = Label(
            pantalla_log,
            text="Logs",
            bg="black",
            fg="White",
            height=1,
            width=60,
            font=("system", 16, "bold"),
        )

        pantalla_log.titulo.grid(
            row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W + E
        )
        pantalla_log.tree = Treeview(pantalla_log, height=10, columns=3)
        pantalla_log.tree["columns"] = ("one", "two", "three")
        pantalla_log.tree.grid(row=7, column=0, columnspan=3)
        pantalla_log.tree.heading("#0", text="Fecha", anchor=CENTER)
        pantalla_log.tree.heading("one", text="ID", anchor=CENTER)
        pantalla_log.tree.heading("two", text="Título", anchor=CENTER)
        pantalla_log.tree.heading("three", text="Descripción", anchor=CENTER)
        pantalla_log.tree.column("one", width=50, anchor=CENTER)

        objetos = self.trae_log()

        for i in objetos:
            pantalla_log.tree.insert(
                "",
                0,
                text=i.fecha,
                values=(
                    i.id,
                    i.titulo,
                    i.descripcion,
                ),
            )

        pantalla_log.mainloop()

    def trae_log(self):
        objetos = Log.select()
        return objetos

    ################################################## FUNCIONES ##########################################################################
    def mostrar(
        self,
    ):

        # limpieza de tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        for fila in base_datos.Noticia.select():
            self.tree.insert(
                "",
                0,
                text=fila.id,
                values=(
                    fila.titulo,
                    fila.descripcion,
                    fila.fecha,
                ),
            )

    def guardar_registro(
        self,
    ):

        guardar(self)

    def eliminar_registro(
        self,
    ):

        eliminar(self)

    def modificar_registro(
        self,
    ):

        modificar(self)


if __name__ == "__main__":
    window = Tk()
    application = Producto(window)
    application.mostrar()
    elobservador = guardarmodal.Observando(application)
    window.mainloop()
