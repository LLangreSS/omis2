import tkinter as tk
from tkinter import ttk, messagebox


class ReportsFrame(tk.Frame):
    """Окно формирования отчетов"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Аналитика и Отчетность", font=("Arial", 16, "bold")).pack(pady=20)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Тип отчета:").grid(row=0, column=0, sticky="e", padx=5, pady=8)
        self.type_cb = ttk.Combobox(
            form,
            values=[
                "Отчет о движении средств",
                "Структура расходов",
                "Динамика доходов и расходов",
            ],
            width=35,
        )
        self.type_cb.current(0)
        self.type_cb.grid(row=0, column=1, padx=5, pady=8)

        tk.Label(form, text="Период:").grid(row=1, column=0, sticky="e", padx=5, pady=8)
        self.period_cb = ttk.Combobox(form, values=["Текущий месяц", "Прошлый месяц", "За год"], width=35)
        self.period_cb.current(0)
        self.period_cb.grid(row=1, column=1, padx=5, pady=8)

        btns = tk.Frame(self)
        btns.pack(pady=20)
        tk.Button(btns, text="Сформировать", command=lambda: messagebox.showinfo("Отчет", "Отчет сформирован.")).pack(side="left", padx=5)
        tk.Button(btns, text="Экспорт в PDF", command=lambda: messagebox.showinfo("Экспорт", "Файл экспортирован.")).pack(side="left", padx=5)
        tk.Button(btns, text="Назад на Дашборд", command=lambda: controller.show_frame("DashboardFrame")).pack(side="left", padx=5)