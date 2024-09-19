from fastapi import FastAPI

app = FastAPI()

@app.get("/inicio")
def read_root():
    return {"Hello": "World"}

