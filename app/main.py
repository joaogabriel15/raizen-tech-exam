from uvicorn import run
from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes import routes

load_dotenv()
app = FastAPI()

for route in routes:
    app.include_router(route)


   



if __name__ == "__main__":
    run("main:app", port=8000, log_level="debug")