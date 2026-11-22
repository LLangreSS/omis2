from datetime import datetime
from typing import List
from models import User, Account, Category, Transaction, Budget, Report, Notification


class FinanceSystem:
    """Единое хранилище и фасад подсистем"""
    def __init__(self):
        self.users: List[User] = [
            User(1, "Иван Иванов", "user", "1234", "user"),
            User(2, "Администратор", "admin", "admin", "admin"),
        ]
        self.accounts: List[Account] = [
            Account(1, "Карта Сбербанк", "Дебетовая карта", 45000.0, 1),
            Account(2, "Наличные в кошельке", "Наличные", 3500.0, 1),
        ]
        self.categories: List[Category] = [
            Category(1, "Продукты", "расход"),
            Category(2, "Транспорт", "расход"),
            Category(3, "Рестораны", "расход"),
            Category(4, "Зарплата", "доход"),
        ]
        self.transactions: List[Transaction] = []
        self.budgets: List[Budget] = [
            Budget(1, 10000.0, "Текущий месяц", 9000.0, 3, 1),
        ]
        self.reports: List[Report] = []
        self.notifications: List[Notification] = [
            Notification(
                1,
                "Внимание: по категории 'Рестораны' потрачено 90% лимита!",
                datetime.now(),
                1,
                1,
            )
        ]