from tkinter import *
#from tkinter import messagebox
#from tkinter import ttk
from Vista.gui import *
from Modelo.supplier import *
from Modelo.owner import *
from Modelo.team import *
from Modelo.software import *
from Modelo.part import *
from Modelo.location import *


if __name__=='__main__':
    root=Tk()
    ventana= MiVentanaPrincipal(root)
    root.mainloop()
