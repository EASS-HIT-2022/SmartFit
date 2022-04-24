from pydantic import BaseModel


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
    SERVER_PORT: int = 8070


class DatabaseSettings(BaseModel):
    """
    Database settings for app
    """
    DB_URL: str = "mongodb+srv://talsag:288944@cluster0.n8bbj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DB_NAME: str = "SmartFit"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    """
    Settings for app
    """
    pass


settings = Settings()
