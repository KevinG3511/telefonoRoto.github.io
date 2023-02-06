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

@router.get("/telefono5/{palabra}")
def read_item(palabra: str):
    """inicio"""
    return {'change4': palabra.split(' ')}

@router.get("/tel1")
def root5():
    """inicio"""
    return {'mensaje':'este es un mensaje oculto'}

if __name__ == '__main__':
    router.run(port=8000)
