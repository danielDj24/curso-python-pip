#importamos la libreria que instalamos en la carpeta del proyecto
import requests 

api_platzi= 'https://api.escuelajs.co/api/v1/categories'
#funcion para hacer solicitudes a la API
def get_categories():
    
    #variable donde establecemos la direccion de donde obtendremos la solicitud
    r = requests.get(api_platzi) 
    
    #imprime el status de la solicitud
    print(f'status code=>', r.status_code ) 
    
    #respuesta de la solicitud:
    print(f'text=>', r.text)
    
    #para conocer el formato en que recibimos los datos  
    print(type(r.text)) # suelta un str
    
    #para transformar este a una lista de diccionarios
    categories = r.json()#el formato json, lo transforma automaticamente en una lista
    
    #para que nos devuelva solo el nombre de las categorias
    for category in categories :
        print(category['name'])