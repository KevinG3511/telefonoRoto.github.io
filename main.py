from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ruta 1"}

@app.get("/get_data")
def root1():
    response = requests.get('https://reqres.in/api/users?page=2')
    res = response.json()
    return {"message": "esta es la respuesta de la otra api", 'resp': res}

if __name__ == '__main__':
    app.run(port=8000)