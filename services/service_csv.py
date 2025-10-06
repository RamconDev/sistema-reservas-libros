import pandas as pd
import os

class ServiceCsv:
    def __init__(self, nombre_archivo):
        self.__nombre_archivo =  nombre_archivo
        self.__path = os.path.dirname(__file__)
        self.__csv_path = os.path.join(self.__path,"..","data",self.__nombre_archivo)

    def get_data(self):
        try:
            archive = pd.read_csv(self.__csv_path)
            return archive
        except FileNotFoundError:
            print(f"Archivo '{self.__nombre_archivo}' no encontrado")
            return pd.DataFrame
        
    
    
class LibrosCsv(ServiceCsv):
    def __init__(self, nombre_archivo):
        super().__init__(nombre_archivo)
        

archive_name = "libros.csv"

libros = LibrosCsv("libros.csv")
archive = libros.get_data()

print(type(archive))
for line in archive:
    print(line)