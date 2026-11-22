import tkinter as tk
from services import FinanceSystem
from ui.frames import (
    LoginFrame,
    DashboardFrame,
    TransactionsFrame,
    BudgetFrame,
    ReportsFrame,
    AdminFrame,
)


class FinanceApp(tk.Tk):
    """Главное окно приложения и контроллер переходов между экранами"""
    def __init__(self):
        super().__init__()
        self.title("Система учета и мониторинга движения финансов")
        self.geometry("750x500")
        self.resizable(False, False)

        self.system = FinanceSystem()
        self.current_user = None

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for FrameClass in (
            LoginFrame,
            DashboardFrame,
            TransactionsFrame,
            BudgetFrame,
            ReportsFrame,
            AdminFrame,
        ):
            frame = FrameClass(parent=self.container, controller=self)
            self.frames[FrameClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")

    def show_frame(self, frame_name: str):
        frame = self.frames[frame_name]
        if hasattr(frame, "on_show"):
            frame.on_show()
        frame.tkraise()