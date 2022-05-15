from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()


class CommonSettings(BaseModel):
    """
    Common settings for app
    """
    APP_NAME: str = "SmartFit"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "AI fitness app"
    APP_AUTHOR: str = "Talsag"
    DEBUG_MODE: bool = True


class ServerSettings(BaseModel):
    """
    Server settings for app
    """
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = int(os.environ.get('SERVER_PORT'))
    API_V1_STR: str = "api/api_v1"

class DatabaseSettings(BaseModel):
    """
    Database settings for app
    """
    DB_URL: str = "mongodb+srv://talsag:288944@cluster0.n8bbj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DB_NAME: str = "SmartFit"
    EMAIL_TEST_USER:str = 'example@exa.com'
    PASSWORD_TEST_USER:str = 'example'
    FULL_NAME_TEST_USER:str =  "Test"
    TEST_USER_ID:str = '5844f810-873d-41e7-9290-2e679f0769d4'



class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    """
    Settings for app
    """
    pass


settings = Settings()
