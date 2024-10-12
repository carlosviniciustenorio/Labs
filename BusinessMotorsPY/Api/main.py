from fastapi import FastAPI
from Api.Controllers import marcas_controller, tipos_combustiveis_controller, modelos_controller

app = FastAPI()

app.include_router(marcas_controller.router)
app.include_router(modelos_controller.router)
app.include_router(tipos_combustiveis_controller.router)
