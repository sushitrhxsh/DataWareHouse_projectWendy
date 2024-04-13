from tkinter import *
import PsqlConexion

class Ventana(Frame):
    #Constructor
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.root.title('Almacen de Datos')
        self.root.geometry("700x500")
        self.screenCanvas = Canvas(self.root)
        self.screenCanvas.pack(fill='both', expand=True)

        self.selectTree = ttk.Treeview(self.root, height=15)
        self.selectTree['columns'] = ('id', 'first_name', 'card', 'job_title')
        self.selectTree.column('#0', width=0, stretch=NO)
        self.selectTree.column('id', anchor='center', width=50)
        self.selectTree.column('first_name', anchor='nw', width=120)
        self.selectTree.column('card', anchor='nw', width=120)
        self.selectTree.column('job_title', anchor='nw', width=120)
        #self.selectTree.column('college', anchor='nw', width=120)
        self.selectTree.heading('id', text='ID', anchor='center')
        self.selectTree.heading('first_name', text='first_name', anchor='nw')
        self.selectTree.heading('last_name', text='last_name', anchor='nw')
        self.selectTree.heading('job_title', text='job_title', anchor='nw')
        #self.selectTree.heading('college', text='college', anchor='nw')
        self.selectTree_canvas = self.screenCanvas.create_window(25, 25, anchor='nw', window=self.selectTree)

        self.ButtonSalir = Button(image=self.salir, bd=0, command=self.return2Main)
        self.ButtonSalir_canvas = self.screenCanvas.create_window(278, 420, anchor='nw', window=self.ButtonSalir)

        try:
            sql = 'SELECT id_client, first_name, last_name, job_title, college FROM public."dimclient";'

            n = 0
            for row in clients:
                self.selectTree.insert(parent='', index='end', iid=n, text='',
                                       values=(row[0], row[1], row[2], row[3],
                                               row[4], row[5]))
                n += 1
        except(Exception, psycopg2.Error) as error:
            print(error)
            messagebox.showerror("Validacion erronea", "ERROR")

    def return2Main(self):
        self.root.destroy()
        wn = mainWindow(root=Tk())
        wn.mainloop()

if __name__ == '__main__':
    main = Mostrar.Ventana(root=Tk())
    main.mainloop()