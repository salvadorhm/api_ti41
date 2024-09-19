# Importamos la clase FastAPI desde el módulo fastapi, la cual nos permite crear una aplicación web.
from fastapi import FastAPI

# Importamos la clase BaseModel desde pydantic, que se utiliza para validar y modelar los datos en FastAPI.
from pydantic import BaseModel

# Definimos una clase "Persona" que hereda de "BaseModel". Esta clase sirve para estructurar y validar los datos
# que se recibirán o enviarán en las solicitudes relacionadas con una "Persona".
class Persona(BaseModel):
    # Definimos los atributos de la clase Persona. Aquí, name es una cadena (str) y age es un número entero (int).
    name: str
    age: int

# Creamos una instancia de FastAPI. "app" es la aplicación FastAPI que se usará para definir las rutas y manejar las solicitudes HTTP.
app = FastAPI()

# Definimos una ruta (endpoint) GET que estará disponible en "/inicio".
# Esta función devuelve un diccionario JSON que contiene la clave "Hello" y el valor "World".
@app.get("/inicio")
def read_root():
    return {"Hello": "World"}

# Definimos otra ruta GET que recibirá un parámetro "numero" desde la URL.
# Este parámetro es dinámico y se espera que sea un valor entero. 
@app.get("/parametro/{numero}")
def incrementar(numero: int):  # Agregué la anotación del tipo para claridad
    # La función incrementa el valor de "numero" en 1 y devuelve el resultado en formato JSON.
    numero = numero + 1
    return {"Incremento": numero}

# Definimos una ruta POST en la que se recibirá un objeto de tipo "Persona" en el cuerpo de la solicitud.
# Este método procesará datos enviados en formato JSON que coincidan con el esquema de la clase Persona.
@app.post("/personas")
def get_personas(usuario: Persona):
    # Retorna un diccionario JSON que contiene el nombre y la edad extraídos de la instancia de "Persona" recibida.
    return {
        "nombre": usuario.name,
        "edad": usuario.age
    }

@app.get("/query")
def suma(numero1 : int , numero2: int):
    resultado = numero1 + numero2
    return {"suma":resultado}
