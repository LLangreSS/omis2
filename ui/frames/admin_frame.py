import tkinter as tk
from tkinter import messagebox


class AdminFrame(tk.Frame):
    """Панель администратора"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Панель Администратора", font=("Arial", 16, "bold")).pack(pady=25)

        tk.Button(
            self,
            text="Создать семейный счёт",
            width=35,
            pady=8,
            command=lambda: messagebox.showinfo("Счета", "Запрос на создание счета отправлен."),
        ).pack(pady=8)

        tk.Button(
            self,
            text="Создать категории",
            width=35,
            pady=8,
            command=lambda: messagebox.showinfo("Категории", "Запрос на создание категории отправлен."),
        ).pack(pady=8)

        tk.Button(
            self,
            text="Создать резервное копирование",
            width=35,
            pady=8,
            command=lambda: messagebox.showinfo("Резервное копирование", "Копия БД создана."),
        ).pack(pady=8)

        tk.Button(
            self,
            text="Перейти в Дашборд пользователя",
            width=35,
            pady=5,
            command=lambda: controller.show_frame("DashboardFrame"),
        ).pack(pady=(25, 5))

        tk.Button(self, text="Выйти", width=20, command=lambda: controller.show_frame("LoginFrame")).pack(pady=5)