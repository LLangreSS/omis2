import tkinter as tk
from tkinter import ttk, messagebox


class TransactionsFrame(tk.Frame):
    """Окно регистрации операций"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Регистрация операции", font=("Arial", 16, "bold")).pack(pady=20)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Счет:").grid(row=0, column=0, sticky="e", padx=5, pady=8)
        self.acc_cb = ttk.Combobox(form, values=[a.name for a in controller.system.accounts], width=30)
        self.acc_cb.current(0)
        self.acc_cb.grid(row=0, column=1, padx=5, pady=8)

        tk.Label(form, text="Категория:").grid(row=1, column=0, sticky="e", padx=5, pady=8)
        self.cat_cb = ttk.Combobox(form, values=[c.name for c in controller.system.categories], width=30)
        self.cat_cb.current(0)
        self.cat_cb.grid(row=1, column=1, padx=5, pady=8)

        tk.Label(form, text="Сумма:").grid(row=2, column=0, sticky="e", padx=5, pady=8)
        self.amount_entry = tk.Entry(form, width=33)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=8)

        tk.Label(form, text="Комментарий:").grid(row=3, column=0, sticky="e", padx=5, pady=8)
        self.comment_entry = tk.Entry(form, width=33)
        self.comment_entry.grid(row=3, column=1, padx=5, pady=8)

        btns = tk.Frame(self)
        btns.pack(pady=20)
        tk.Button(
            btns,
            text="Сохранить операцию",
            command=lambda: messagebox.showinfo("Сохранено", "Транзакция передана на валидацию."),
        ).pack(side="left", padx=10)
        tk.Button(btns, text="Назад на Дашборд", command=lambda: controller.show_frame("DashboardFrame")).pack(side="left", padx=10)