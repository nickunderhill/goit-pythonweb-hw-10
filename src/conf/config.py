class Config:
    DB_URL = "postgresql+asyncpg://postgres:password@localhost:5432/contacts_db"
    JWT_SECRET = "your_secret_key"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_SECONDS = 3600  # 1 hour


config = Config
