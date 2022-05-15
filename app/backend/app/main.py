import asyncio
import uvicorn
from routes.api.api_v1 import api
from fastapi import FastAPI
from core.config import settings
import uvicorn
from middleware.checkObjectId import CustomHeaderMiddleware
from db import db
from fastapi.responses import RedirectResponse
from fastapi.testclient import TestClient
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="SmartFit",
              description="This is SmartFit API", version="1.0.0")


app.include_router(api.api_router, prefix=f'/{settings.API_V1_STR}')


app.add_middleware(CORSMiddleware , allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],) # This is for adding custom header to all response


@app.on_event("startup")
async def startup_db_client():
    await db.connect_to_database(path=settings.DB_URL, db_name=settings.DB_NAME)


@app.on_event("shutdown")
def shutdown():
    db.close_database_connection()

@app.get("/")
async def root():
    return RedirectResponse('/docs')



def main():
    uvicorn.run("main:app", host=settings.SERVER_HOST,
            port=settings.SERVER_PORT, debug=settings.DEBUG_MODE)

if __name__ == "__main__":
    asyncio.run(main())

