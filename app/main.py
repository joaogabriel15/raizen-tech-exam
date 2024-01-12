from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes import routes

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa a aplicação FastAPI.
app = FastAPI(title="Weather API Cache")


# Inclui as rotas definidas no iterable 'routes' na aplicação.
for route in routes:
    app.include_router(route)