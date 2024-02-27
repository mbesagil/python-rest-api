# main.py
import time
from fastapi import FastAPI, Request
from app.route import user
from app.config.database import Base, engine
from dotenv import load_dotenv


#config .env
load_dotenv()





app = FastAPI()

# SQLAlchemy'den tabloları oluştur
Base.metadata.create_all(bind=engine)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(process_time)
    return response


# Base.metadata.create_all(bind=engine)

app.include_router(user.router)
# app.include_router(product.router)