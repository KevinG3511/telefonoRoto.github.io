from fastapi import APIRouter
import requests
servicio1= APIRouter()

@servicio1.get('/')
async def root():
    'Pagina de inicio'
    return 'http://127.0.0.1:8000/api1/get_data'

@servicio1.get('/show_data')
async def root1():
    """Mostrar informacion (lo que recibe request antes del cambio)"""
    results = {
        'name':'Kevin Guevara',
        'age':19
    }
    obj = {"status": 200, "results": results, "msg": "Peticion correcta"}
    return obj

@servicio1.get('/get_data')
async def root2():
    """Retornar informacion ('despues del cambio')"""
    results = {
        'name':'Este es un nuevo mensaje',
    }
    obj = {"status": 200, "results": results, "msg": "Peticion correcta"}
    return obj

