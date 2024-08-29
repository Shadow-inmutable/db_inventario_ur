class Equipo:
    def __init__(self,ser,mar,mod,tip,fecha,gar,cla,id_cue,id_ubi,id_pro,id=None):
        self.__serial=ser
        self.__marca=mar
        self.__modelo=mod
        self.__tipo=tip
        self.__fecha_compra=fecha
        self.__garantia=gar
        self.__clasificacion=cla
        self.__id_cuentadante=id_cue
        self.__id_ubicacion=id_ubi
        self.__id_proveedor=id_pro        
        self.__id=id
    
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
    def clasificacion(self):
        return self.__clasificacion
    
    @clasificacion.setter
    def clasificacion(self,cla):
        self.__clasificacion=cla

    @property
    def id_cuentadante(self):
        return self.__id_cuentadante
    
    @id_cuentadante.setter
    def id_cuentadante(self,id_cue):
        self.__id_cuentadante=id_cue
    
    @property
    def id_ubicacion(self):
        return self.__id_ubicacion
    
    @id_ubicacion.setter
    def id_ubicacion(self,id_ubi):
        self.__id_ubicacion=id_ubi
    
    @property
    def id_proveedor(self):
        return self.__id_proveedor
    
    @id_proveedor.setter
    def id_proveedor(self,id_pro):
        self.__id_proveedor=id_pro
