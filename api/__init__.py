from fastapi import APIRouter
from .routes import servicio_1

router = APIRouter()

router.include_router(servicio_1.servicio1, prefix='/api1')

if __name__ == '__main__':
    router.run(port=8000)