import tkinter as tk
from tkinter import ttk, messagebox


class BudgetFrame(tk.Frame):
    """Окно установки лимита по категории"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Планировщик бюджета", font=("Arial", 16, "bold")).pack(pady=20)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Категория:").grid(row=0, column=0, sticky="e", padx=5, pady=8)
        self.cat_cb = ttk.Combobox(form, values=[c.name for c in controller.system.categories], width=30)
        self.cat_cb.current(0)
        self.cat_cb.grid(row=0, column=1, padx=5, pady=8)

        tk.Label(form, text="Период:").grid(row=1, column=0, sticky="e", padx=5, pady=8)
        self.period_entry = tk.Entry(form, width=33)
        self.period_entry.insert(0, "Текущий месяц")
        self.period_entry.grid(row=1, column=1, padx=5, pady=8)

        tk.Label(form, text="Лимит (руб.):").grid(row=2, column=0, sticky="e", padx=5, pady=8)
        self.limit_entry = tk.Entry(form, width=33)
        self.limit_entry.grid(row=2, column=1, padx=5, pady=8)

        btns = tk.Frame(self)
        btns.pack(pady=20)
        tk.Button(
            btns,
            text="Установить лимит",
            command=lambda: messagebox.showinfo("Бюджет", "Лимит сохранен."),
        ).pack(side="left", padx=10)
        tk.Button(btns, text="Назад на Дашборд", command=lambda: controller.show_frame("DashboardFrame")).pack(side="left", padx=10)