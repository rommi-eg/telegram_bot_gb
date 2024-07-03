from pydantic_settings import (

    BaseSettings, 
    SettingsConfigDict
    
    )
from pydantic import SecretStr
import os

DOTENV = os.path.join(

    os.path.dirname(__file__),
    '.env'
    
    )

class Settings(BaseSettings):
    bot_token: SecretStr
    model_config = SettingsConfigDict(

        env_file=DOTENV, 
        env_file_encoding='utf-8'

        )

token = Settings()