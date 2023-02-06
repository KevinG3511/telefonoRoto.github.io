# from fastapi import APIRouter
# import requests
# servicio1= APIRouter()

# @servicio1.get('/')
# async def root():
#     'Pagina de inicio'
#     return 'http://127.0.0.1:8000/api1/get_data'

# @servicio1.get('/show_data')
# async def root1():
#     """Mostrar informacion (lo que recibe request antes del cambio)"""
#     results = {
#         'name':'Kevin Guevara',
#         'age':19
#     }
#     obj = {"status": 200, "results": results, "msg": "Peticion correcta"}
#     return obj

# @servicio1.get("/telefono3/{palabra}")
# def read_item(palabra: str):
#     """inicio"""
#     cambios = palabra.replace('A', '4').replace('E', '3').replace(
#         'I', '1').replace('O', '0').replace('U', '8')
#     url = 'https://ojyvp2.deta.dev/telefono4/'+cambios
#     resp = requests.get(url)
#     respuesta = resp.json()
#     return {'status': 200,
#             'results': {
#                 'change1': palabra,
#                 'change2': cambios,
#                 'change': respuesta
#             }
#             }
