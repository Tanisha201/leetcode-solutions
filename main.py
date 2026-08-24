from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    debug: bool = False
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings(app_name="MyApp", database_url="sqlite:///:memory:")
print(settings.app_name)