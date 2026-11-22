from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Account:
    """Сущность: Счет"""
    account_id: int
    name: str
    account_type: str
    balance: float
    user_id: int


@dataclass
class Category:
    """Сущность: Категория"""
    category_id: int
    name: str
    category_type: str  
    parent_category_id: Optional[int] = None


@dataclass
class Transaction:
    """Сущность: Транзакция"""
    transaction_id: int
    date: datetime
    amount: float
    comment: str
    account_id: int
    category_id: int
    user_id: int