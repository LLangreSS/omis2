import tkinter as tk


class DashboardFrame(tk.Frame):
    """Главный экран / Дашборд"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        nav = tk.Frame(self, bg="#e0e0e0", pady=8)
        nav.pack(fill="x")
        tk.Button(nav, text="Операции", command=lambda: controller.show_frame("TransactionsFrame")).pack(side="left", padx=10)
        tk.Button(nav, text="Бюджет и лимиты", command=lambda: controller.show_frame("BudgetFrame")).pack(side="left", padx=10)
        tk.Button(nav, text="Отчеты", command=lambda: controller.show_frame("ReportsFrame")).pack(side="left", padx=10)
        tk.Button(nav, text="Выйти", command=lambda: controller.show_frame("LoginFrame")).pack(side="right", padx=10)

        tk.Label(self, text="Дашборд (Главный экран)", font=("Arial", 16, "bold")).pack(pady=15)

        tk.Label(self, text="Ваши счета:", font=("Arial", 12, "bold")).pack(anchor="w", padx=30)
        self.accounts_list = tk.Listbox(self, height=4, width=80)
        self.accounts_list.pack(padx=30, pady=5)

        tk.Label(self, text="Уведомления и мониторинг лимитов:", font=("Arial", 12, "bold")).pack(anchor="w", padx=30, pady=(15, 0))
        self.notif_list = tk.Listbox(self, height=5, width=80, fg="#b36b00")
        self.notif_list.pack(padx=30, pady=5)

    def on_show(self):
        self.accounts_list.delete(0, tk.END)
        for acc in self.controller.system.accounts:
            self.accounts_list.insert(tk.END, f"{acc.name} ({acc.account_type}) — Баланс: {acc.balance:.2f} руб.")

        self.notif_list.delete(0, tk.END)
        for n in self.controller.system.notifications:
            self.notif_list.insert(tk.END, f"[{n.date.strftime('%Y-%m-%d')}] {n.text}")