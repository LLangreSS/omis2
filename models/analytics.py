from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Budget:
    """Сущность: Бюджет"""
    budget_id: int
    limit: float
    period: str
    spent: float
    category_id: int
    user_id: int


@dataclass
class Report:
    """Сущность: Отчет"""
    report_id: int
    period: str
    report_type: str
    user_id: int


@dataclass
class Notification:
    """Сущность: Уведомление"""
    notification_id: int
    text: str
    date: datetime
    user_id: int
    budget_id: Optional[int] = None