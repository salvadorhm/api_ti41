# Importamos la clase FastAPI desde el módulo fastapi, la cual nos permite crear una aplicación web.
from fastapi import FastAPI

# Creamos una instancia de FastAPI. "app" es la aplicación FastAPI que se usará para definir las rutas y manejar las solicitudes HTTP.
app = FastAPI()

# Definimos una ruta (endpoint) GET que estará disponible en "/inicio".
# Esta función devuelve un diccionario JSON que contiene la clave "Hello" y el valor "World".
@app.get("/inicio")
def read_root():
    return {"Hello": "World"}
