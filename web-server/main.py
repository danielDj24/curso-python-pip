#modulo donde la esta la funcion que trae la peticion
import store 

def run():
    
#llamamos la funcion del modulo anterior
    store.get_categories() 
    
    
#ejecutamos como un script este modulo
if __name__ == '__main__': 
    run()