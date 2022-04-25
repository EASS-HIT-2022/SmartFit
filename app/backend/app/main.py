import uvicorn
from routes.api.api_v1 import api
from fastapi import FastAPI
from core.config import settings
import uvicorn
from middleware.checkObjectId import CustomHeaderMiddleware
from db import db
from fastapi.responses import RedirectResponse


app = FastAPI(title="SmartFit",
              description="This is SmartFit API", version="1.0.0")


app.include_router(api.api_router)


# app.add_middleware(CustomHeaderMiddleware) # This is for adding custom header to all response


@app.on_event("startup")
async def startup_db_client():
    db.connect_to_database(path=settings.DB_URL, db_name=settings.DB_NAME)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()


@app.get("/")
async def root():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.SERVER_HOST,
                port=settings.SERVER_PORT, debug=settings.DEBUG_MODE)
