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

@router.get("/telefono2/{palabra}")
def read_item(palabra: str):
    """inicio"""
    url = 'https://7gskcu.deta.dev/telefono3/'+palabra.upper()
    resp = requests.get(url)
    respuesta = resp.json()
    return {'status': 200,
            'results': {
                'original': palabra,
                'change': respuesta
            }
            }

if __name__ == '__main__':
    router.run(port=8000)
