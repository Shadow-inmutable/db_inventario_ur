class Software:
    def __init__(self,nom,ver,inkey,cls,vg,id_equi,id_pro,id=None):
        self.__nombre=nom
        self.__version=ver
        self.__instalationKey=inkey
        self.__cantLincencias=cls
        self.__vigencias=vg
        self.__id_equipo=id_equi
        self.__id_proveedor=id_pro
        self.__id=id
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self.__nombre=nom
    
    @property
    def version(self):
        return self.__version
    @version.setter
    def version(self,ver):
        self.__version=ver
        
    @property
    def instalationKey(self):
        return self.__instalationKey
    @instalationKey.setter
    def modeinstalationKeylo(self,inkey):
        self.__instalationKey=inkey
        
    @property
    def cantLincencias(self):
        return self.__cantLincencias
    @cantLincencias.setter
    def cantLincencias(self,cls):
        self.__cantLincencias=cls
    
    @property
    def vigencias(self):
        return self.__vigencias
    @vigencias.setter
    def vigencias(self,vg):
        self.__vigencias=vg
        
        
    @property
    def garantia(self):
        return self.__garantia
    @garantia.setter
    def garantia(self,gar):
        self.__garantia=gar
    
    @property
    def  id_equipo(self):
        return self.__id_equipo
    @id_equipo.setter
    def id_equipo(self,id_equi):
        self.__id_equipo=id_equi
        
    @property
    def  id_proveedor(self):
        return self.__id_proveedor
    @id_proveedor.setter
    def id_proveedor(self,id_pro):
        self.__id_proveedor=id_pro
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id=id