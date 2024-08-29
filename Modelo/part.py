class Parte:
    def __init__(self,ser,mar,mod,tip,fecha,gar,id_equi,id_pro,id=None):
        self.__serial=ser
        self.__marca=mar
        self.__modelo=mod
        self.__tipo=tip
        self.__fecha_compra=fecha
        self.__garantia=gar
        self.__id_equipo=id_equi
        self.__id_proveedor=id_pro
        self.__id_parte=id
        
    @property
    def serial(self):
        return self.__serial
    @serial.setter
    def serial(self,ser):
        self.__serial=ser
    
    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,mar):
        self.__marca=mar
        
    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self,mod):
        self.__modelo=mod
        
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tip):
        self.__tipo=tip
    
    @property
    def fecha_compra(self):
        return self.__fecha_compra
    @fecha_compra.setter
    def fecha_compra(self,fecha):
        self.__fecha_compra=fecha
        
        
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
    def id_parte(self):
        return self.__id_parte
    @id_parte.setter
    def id_parte(self,id):
        self.__id_parte=id
        
        
        