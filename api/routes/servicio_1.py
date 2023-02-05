from fastapi import APIRouter
servicio1= APIRouter()

@servicio1.get('/')
async def root():
    'Pagina de inicio'
    return '<h1>Rutas<h1><br><a href=#>-----<a>'

@servicio1.get('/show_data')
async def root1():
    """Mostrar informacion"""
    results = {
        'name':'Kevin Guevara',
        'age':19
    }
    obj = {"status": 200, "results": results, "msg": "Peticion correcta"}
    return obj

