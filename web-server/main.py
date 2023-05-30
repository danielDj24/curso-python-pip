#modulo donde la esta la funcion que trae la peticion
import store 

from fastapi import FastAPI #importamos la lib
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/') #ruta para ver desde la web
def get_list():
    return [1, 2, 3,]

@app.get('/contact', response_class=HTMLResponse) #ruta
def get_list():
    return """
        <h1> Hola soy una pagina</h1>
        <p>soy un parrafo</p>
""" 

def run():
    
#llamamos la funcion del modulo anterior
    store.get_categories() 
    
    
#ejecutamos como un script este modulo
if __name__ == '__main__': 
    run()