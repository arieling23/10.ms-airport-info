from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        self.secret_key = os.getenv("SECRET_KEY")
        self.algorithm = os.getenv("JWT_ALGORITHM", "HS256")
        self.app_port = int(os.getenv("APP_PORT", 8000))

settings = Settings()
