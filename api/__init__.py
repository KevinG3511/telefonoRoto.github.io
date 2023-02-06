from fastapi import APIRouter
import requests
# import urllib3
# import json

router= APIRouter()

@router.get('/')
async def root():
    'Pagina de inicio'
    return 'http://127.0.0.1:8000/show_data'

@router.get('/show_data')
async def root1():
    """Mostrar informacion (lo que recibe request antes del cambio)"""
    results = {
        'telefono':'3',
        'author':'Kevin Guevara'
    }
    obj = {"status": 200, "results": results, "msg": "Peticion correcta"}
    return obj

@router.get("/telefono3")
def read_item():
    """inicio"""
    url = 'https://9st22m.deta.dev/telefono1/holaa'
    # url = 'https://ojyvp2.deta.dev/telefono4/'+cambios
    resp = requests.get(url)
    respuesta = resp.json()
    return respuesta

if __name__ == '__main__':
    router.run(port=8000)
