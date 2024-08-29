import mysql.connector

class DataBase:
    def __init__(self):
        self.connection= mysql.connector.connect(
            host='localhost',
            user='root' ,
            password='',
            database='db_inventario_ur'
        )
        self.cursor=self.connection.cursor()