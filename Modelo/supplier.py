class Proveedor:
    def __init__(self,nit,razon,dir,tel,email,id=None):
        self.__nit=nit
        self.__razon_social=razon
        self.__direccion=dir
        self.__telefono=tel
        self.__email=email
        self.__id=id
    
    @property
    def nit(self):
        return self.__nit
    
    @nit.setter
    def nit(self,nit):
        self.__nit= nit
    
    @property
    def razon_social(self):
        return self.__razon_social
    
    @razon_social.setter
    def razon_social(self,razon):
        self.__razon_social=razon
    
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self,dir):
        self.__direccion=dir
    
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,tel):
        self.__telefono= tel
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        self.__email= email
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id):
        self.__id= id