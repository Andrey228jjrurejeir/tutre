from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

# Ініціалізація для базової авторизації
security = HTTPBasic()
# Словник для зберігання логінів та паролів (для демонстрації)
fake_users_db = {
    "user1": {
        "username": "Andriy12",
        "password": "asd1213T"  # пароль для user1
    }
}

# Модель для запиту авторизації
class User(BaseModel):
    username: str
    password: str

# Функція для перевірки користувача та пароля
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = fake_users_db.get(credentials.username)
    if user is None or user['password'] != credentials.password:
        raise HTTPException(
            status_code=401, detail="Invalid username or password"
        )
    return {"message": f"Hello {credentials.username}, I know you!"}

# Маршрут для перевірки авторизації
@app.get("/login")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    return authenticate_user(credentials)
