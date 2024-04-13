from tkinter import *
import PsqlConexion

class Ventana(Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.root.title('Almacen de Datos')
        self.root.geometry("235x100")
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill='both', expand=True)
        self.botonCargar = Button(text="Cargar datos", bd=5, bg='black', fg='white', justify='center',
                                   activebackground='white', activeforeground='black', font='Roboto',
                                  width=20, height=2,command=self.cargar)
        self.botonCargarCanvas = self.canvas.create_window(20, 20, anchor='nw', window=self.botonCargar)

    def cargar(self):
        self.conexion_psql_origen, self.conexion_psql_destino = PsqlConexion.abrirConexiones()
        PsqlConexion.cargaDatos(self.conexion_psql_origen, self.conexion_psql_destino)
        PsqlConexion.cerrarConexiones(self.conexion_psql_origen, self.conexion_psql_destino)