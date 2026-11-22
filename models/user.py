from dataclasses import dataclass


@dataclass
class User:
    """Сущность: Пользователь"""
    user_id: int
    name: str
    login: str
    password: str
    role: str = "user"  