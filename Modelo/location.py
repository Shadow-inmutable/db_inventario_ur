class Ubicacion:
    def __init__(self,nom,descrp):
        self.__nombre=nom
        self.__descripcion=descrp
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self.__nombre=nom
    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self,descrip):
        self.__descripcion=descrip
 