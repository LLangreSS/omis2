import tkinter as tk
from tkinter import messagebox


class LoginFrame(tk.Frame):
    """Окно авторизации"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Авторизация в системе", font=("Arial", 18, "bold")).pack(pady=40)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Логин:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.login_entry = tk.Entry(form, width=25)
        self.login_entry.insert(0, "user")
        self.login_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Пароль:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.pass_entry = tk.Entry(form, width=25, show="*")
        self.pass_entry.insert(0, "1234")
        self.pass_entry.grid(row=1, column=1, padx=5, pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Войти", width=15, command=self.do_login).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Войти как Админ", width=18, command=self.admin_login).pack(side="left", padx=5)


    def _authenticate(self):
        login = self.login_entry.get().strip()
        password = self.pass_entry.get().strip()
        for u in self.controller.system.users:
            if u.login == login and u.password == password:
                return u
        return None

    def do_login(self):
        user = self._authenticate()
        if not user:
            messagebox.showerror("Ошибка входа", "Неверный логин или пароль")
            return
        self.controller.current_user = user
        self.controller.show_frame("DashboardFrame")

    def admin_login(self):
        user = self._authenticate()
        if not user:
            messagebox.showerror("Ошибка входа", "Неверный логин или пароль")
            return
        if user.role != "admin":
            messagebox.showerror("Ошибка доступа", "У данного пользователя нет прав администратора")
            return
        self.controller.current_user = user
        self.controller.show_frame("AdminFrame")