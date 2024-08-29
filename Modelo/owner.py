class Cuentadante:
    def __init__(self,doc,nom,ape,cor,cel,id=None):
        self.__documento=doc
        self.__nombres=nom
        self.__apellidos=ape
        self.__correo=cor
        self.__celular=cel
        self.__id=id
    
    @property
    def documento(self):
        return self.__documento
    
    @documento.setter
    def documento(self,doc):
        self.__documento= doc
    
    @property
    def nombres(self):
        return self.__nombres
    
    @nombres.setter
    def nombres(self,nom):
        self.__nombres=nom
    
    @property
    def apellidos(self):
        return self.__apellidos
    
    @apellidos.setter
    def apellidos(self,ape):
        self.__apellidos=ape
    
    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self,cel):
        self.__celular= cel
    
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self,cor):
        self.__correo= cor
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id):
        self.__id= id