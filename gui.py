"""Giao diện desktop cho sổ thu chi cá nhân, dùng dữ liệu chung với app.py."""

import tkinter as tk
from datetime import date
from tkinter import messagebox, simpledialog, ttk
import webbrowser
from urllib.parse import quote

import app as finance


BG = "#111719"
CARD = "#1d2528"
INK = "#e2eae6"
MUTED = "#a0b0a9"
GREEN = "#76c6a4"
RED = "#e28b94"
BLUE = "#9ab8c3"
PURPLE = "#b0a0d0"
LINE = "#34413f"
DEEP = "#111c1a"
DEEP_PANEL = "#1c2b28"
FEEDBACK_EMAIL = "huynhkhiem178@gmail.com"


def money(value):
    """Định dạng số tiền cho dễ đọc trong giao diện."""
    return f"{int(value):,} ₫"


class FinanceWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sổ thu chi cá nhân")
        self.root.geometry("1180x760")
        self.root.minsize(940, 620)
        self.root.configure(bg=BG)

        self.month_var = tk.StringVar(value=date.today().strftime("%Y-%m"))
        self.category_filter_var = tk.StringVar()
        self.kind_var = tk.StringVar(value="Chi")
        self.amount_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.day_var = tk.StringVar(value=date.today().isoformat())
        self.note_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Dữ liệu được lưu trên máy này.")
        self.active_month = self.month_var.get()
        self.active_category = ""

        self._configure_style()
        self._build_window()
        self.refresh()
        self.show_home()
        self.amount_entry.bind("<Control-Return>", lambda _event: self.add_transaction())

    def _configure_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background=BG)
        style.configure("Card.TFrame", background=CARD)
        style.configure("Header.TFrame", background=DEEP)
        style.configure("TLabel", background=BG, foreground=INK, font=("Segoe UI", 10))
        style.configure("Card.TLabel", background=CARD, foreground=INK, font=("Segoe UI", 10))
        style.configure("Muted.Card.TLabel", background=CARD, foreground=MUTED, font=("Segoe UI", 9))
        style.configure("Title.TLabel", background=BG, foreground=INK, font=("Segoe UI", 23, "bold"))
        style.configure("HeaderTitle.TLabel", background=DEEP, foreground="#edf4f0", font=("Segoe UI", 24, "bold"))
        style.configure("HeaderSubtitle.TLabel", background=DEEP, foreground="#b5c7be", font=("Segoe UI", 10))
        style.configure("HeaderTag.TLabel", background="#294039", foreground="#d6e8de", font=("Segoe UI", 9, "bold"), padding=8)
        style.configure("LobbyHero.TFrame", background=DEEP)
        style.configure("LobbyTitle.TLabel", background=DEEP, foreground="#edf4f0", font=("Segoe UI", 29, "bold"))
        style.configure("LobbyText.TLabel", background=DEEP, foreground="#b5c7be", font=("Segoe UI", 11))
        style.configure("LobbyEyebrow.TLabel", background=DEEP, foreground="#82c7a5", font=("Segoe UI", 9, "bold"))
        style.configure("HeroPanel.TFrame", background=DEEP_PANEL)
        style.configure("HeroPanelTitle.TLabel", background=DEEP_PANEL, foreground="#edf4f0", font=("Segoe UI", 13, "bold"))
        style.configure("HeroPanelText.TLabel", background=DEEP_PANEL, foreground="#b5c7be", font=("Segoe UI", 10))
        style.configure("HeroPanelEyebrow.TLabel", background=DEEP_PANEL, foreground="#82c7a5", font=("Segoe UI", 9, "bold"))
        style.configure("Intro.TFrame", background="#26312f")
        style.configure("IntroTitle.TLabel", background="#26312f", foreground="#d8e7df", font=("Segoe UI", 14, "bold"))
        style.configure("IntroText.TLabel", background="#26312f", foreground="#b0beb7", font=("Segoe UI", 10))
        style.configure("Hero.TButton", background="#355c4c", foreground="#e4f2e9", font=("Segoe UI", 10, "bold"), padding=(14, 10))
        style.map("Hero.TButton", background=[("active", "#426d5b")])
        style.configure("LobbyCard.TFrame", background=CARD)
        style.configure("LobbyCardTitle.TLabel", background=CARD, foreground=INK, font=("Segoe UI", 13, "bold"))
        style.configure("LobbyCardText.TLabel", background=CARD, foreground=MUTED, font=("Segoe UI", 9))
        style.configure("Metric.TLabel", background=CARD, foreground=INK, font=("Segoe UI", 16, "bold"))
        style.configure("IncomeCard.TFrame", background="#20372e")
        style.configure("ExpenseCard.TFrame", background="#39292d")
        style.configure("BalanceCard.TFrame", background="#263438")
        style.configure("IncomeCard.Muted.TLabel", background="#20372e", foreground="#8bd3b2", font=("Segoe UI", 9, "bold"))
        style.configure("ExpenseCard.Muted.TLabel", background="#39292d", foreground="#f0a3aa", font=("Segoe UI", 9, "bold"))
        style.configure("BalanceCard.Muted.TLabel", background="#263438", foreground="#b0ccd4", font=("Segoe UI", 9, "bold"))
        style.configure("IncomeCard.Value.TLabel", background="#20372e", foreground="#8bd3b2", font=("Segoe UI", 17, "bold"))
        style.configure("ExpenseCard.Value.TLabel", background="#39292d", foreground="#f0a3aa", font=("Segoe UI", 17, "bold"))
        style.configure("BalanceCard.Value.TLabel", background="#263438", foreground="#b0ccd4", font=("Segoe UI", 17, "bold"))
        style.configure("Treeview", rowheight=36, font=("Segoe UI", 10), background=CARD,
                        fieldbackground=CARD, foreground=INK, bordercolor=LINE)
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"), background="#293432",
                        foreground=INK, padding=(8, 10))
        style.map("Treeview", background=[("selected", "#345044")], foreground=[("selected", "#edf4f0")])
        style.configure("TEntry", fieldbackground="#26312f", foreground=INK, padding=7)
        style.configure("TCombobox", fieldbackground="#26312f", foreground=INK, padding=6,
                        arrowcolor=PURPLE)
        style.map("TCombobox", fieldbackground=[("readonly", "#26312f")],
                  foreground=[("readonly", INK)])
        style.configure("Vertical.TScrollbar", background="#34413f", troughcolor=BG,
                        arrowcolor="#82a894")
        style.configure("Horizontal.TScrollbar", background="#34413f", troughcolor=BG,
                        arrowcolor="#82a894")
        style.configure("TButton", font=("Segoe UI", 9, "bold"), padding=(10, 8))
        style.configure("TButton", background="#293432", foreground=INK)
        style.configure("Primary.TButton", background="#4e9b79", foreground="#10201a")
        style.map("Primary.TButton", background=[("active", "#62ae8c")])
        style.configure("Accent.TButton", background="#2b3935", foreground="#c2d8ca")
        style.map("Accent.TButton", background=[("active", "#374842")])
        style.configure("Danger.TButton", background="#3a292d", foreground="#f0a3aa")
        style.map("Danger.TButton", background=[("active", "#4a3036")])
        style.configure("Rating.TRadiobutton", background="#2b3935", foreground=INK,
                        font=("Segoe UI", 12, "bold"), padding=(13, 10))
        style.map("Rating.TRadiobutton", background=[("selected", "#345044"), ("active", "#374842")],
                  foreground=[("selected", PURPLE)])
        style.configure("Budget.Horizontal.TProgressbar", troughcolor="#34413f", background=GREEN)
        style.configure("OverBudget.Horizontal.TProgressbar", troughcolor="#34413f", background=RED)

    def _build_window(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)

        header = ttk.Frame(self.root, style="Header.TFrame", padding=(28, 22, 28, 20))
        self.header = header
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(0, weight=1)
        self.header_title = ttk.Label(header, text="Sổ thu chi cá nhân", style="HeaderTitle.TLabel")
        self.header_title.grid(row=0, column=0, sticky="w")
        self.header_subtitle = ttk.Label(header, text="Ghi lại thu chi, theo dõi ngân sách và xem số dư trong một nơi.", style="HeaderSubtitle.TLabel")
        self.header_subtitle.grid(
            row=1, column=0, sticky="w", pady=(5, 0)
        )
        header_actions = ttk.Frame(header, style="Header.TFrame")
        header_actions.grid(row=0, column=1, rowspan=2, sticky="e")
        ttk.Button(header_actions, text="＋  Thêm giao dịch", style="Primary.TButton",
                   command=self.open_add_transaction).pack(side="left", padx=(0, 8))
        ttk.Button(header_actions, text="⌂  Sảnh chính", style="Accent.TButton",
                   command=self.show_home).pack(side="left")

        metrics = ttk.Frame(self.root, padding=(26, 0, 26, 18))
        self.metrics = metrics
        metrics.grid(row=1, column=0, sticky="ew")
        for column in range(3):
            metrics.columnconfigure(column, weight=1, uniform="metric")
        self.income_value = self._metric_card(metrics, 0, "TỔNG THU", "IncomeCard")
        self.expense_value = self._metric_card(metrics, 1, "TỔNG CHI", "ExpenseCard")
        self.balance_value = self._metric_card(metrics, 2, "SỐ DƯ", "BalanceCard")

        body = ttk.Frame(self.root, padding=(26, 0, 26, 14))
        self.body = body
        body.grid(row=2, column=0, sticky="nsew")
        body.columnconfigure(0, weight=0, minsize=300)
        body.columnconfigure(1, weight=1)
        body.rowconfigure(0, weight=1)
        self._build_form(body)
        self._build_transactions(body)
        self._build_report_page(body)
        self._build_budget_page(body)
        self._build_rating_page(body)

        status = tk.Label(self.root, textvariable=self.status_var, bg="#1a2224", fg=MUTED,
                          anchor="w", padx=26, pady=9, font=("Segoe UI", 9))
        self.status = status
        status.grid(row=3, column=0, sticky="ew")
        self.dashboard_widgets = [header, metrics, body, status]
        self._build_home()

    def _build_home(self):
        self.home_panel = ttk.Frame(self.root, padding=(26, 22))
        self.home_panel.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.home_panel.columnconfigure(0, weight=1)
        self.home_panel.columnconfigure(1, weight=1)

        hero = ttk.Frame(self.home_panel, style="LobbyHero.TFrame", padding=(24, 16))
        hero.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 18))
        hero.columnconfigure(0, weight=1)
        ttk.Label(hero, text="SỔ THU CHI CÁ NHÂN  ·  PYTHON", style="LobbyEyebrow.TLabel").grid(
            row=0, column=0, sticky="w", pady=(0, 4)
        )
        ttk.Label(hero, text="Quản lý tiền bạc, rõ ràng mỗi ngày.",
                  style="LobbyTitle.TLabel", font=("Segoe UI", 21, "bold")).grid(row=1, column=0, sticky="w")
        ttk.Label(hero, text="Ghi thu chi, xem báo cáo và theo dõi ngân sách ngay trên máy của bạn.",
                  style="LobbyText.TLabel").grid(row=2, column=0, sticky="w", pady=(4, 0))
        ttk.Label(hero, text=date.today().strftime("%d/%m/%Y"), style="HeaderTag.TLabel").grid(
            row=0, column=1, rowspan=3, sticky="e", padx=(12, 0)
        )
        hero_art = tk.Canvas(hero, width=220, height=96, bg=DEEP, highlightthickness=0)
        hero_art.grid(row=0, column=2, rowspan=3, sticky="e", padx=(18, 0))
        self._draw_hero_art(hero_art)

        left = ttk.Frame(self.home_panel, style="Card.TFrame", padding=18)
        left.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        left.columnconfigure(0, weight=1)
        ttk.Label(left, text="Giới thiệu", style="Metric.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Label(left,
                  text="Sổ thu chi cá nhân giúp bạn ghi lại các khoản thu, chi, xem lịch sử và đặt ngân sách theo tháng. Dữ liệu được lưu trên máy.",
                  style="Muted.Card.TLabel", wraplength=430, justify="left").grid(
            row=1, column=0, sticky="w", pady=(7, 18)
        )
        ttk.Label(left, text="Tình hình hiện tại", style="LobbyCardTitle.TLabel").grid(
            row=2, column=0, sticky="w", pady=(0, 9)
        )
        overview = ttk.Frame(left, style="Card.TFrame")
        overview.grid(row=3, column=0, sticky="ew")
        overview.columnconfigure(0, weight=1)
        self.home_income = self._metric_card(overview, 0, "TỔNG THU", "IncomeCard", row=0)
        self.home_expense = self._metric_card(overview, 0, "TỔNG CHI", "ExpenseCard", row=1)
        self.home_balance = self._metric_card(overview, 0, "SỐ DƯ", "BalanceCard", row=2)

        right = ttk.Frame(self.home_panel, style="Card.TFrame", padding=18)
        right.grid(row=1, column=1, sticky="nsew", padx=(10, 0))
        right.columnconfigure(0, weight=1)
        right.columnconfigure(1, weight=1)
        ttk.Label(right, text="Chọn chức năng", style="Metric.TLabel").grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 12)
        )
        self._home_action(right, 0, "＋", "Thêm giao dịch", "Ghi khoản thu hoặc chi.",
                          "Primary.TButton", self.open_add_transaction)
        self._home_action(right, 1, "▤", "Sổ giao dịch", "Xem, lọc và xóa giao dịch.",
                          "Accent.TButton", self.open_transactions)
        self._home_action(right, 2, "▥", "Báo cáo thu chi", "Tổng kết toàn bộ hoặc theo tháng.",
                          "Accent.TButton", self.open_report)
        self._home_action(right, 3, "◉", "Ngân sách tháng", "Đặt hạn mức và theo dõi chi tiêu.",
                          "Accent.TButton", self.open_budget)

        home_footer = ttk.Frame(self.home_panel, style="Intro.TFrame", padding=(16, 10))
        home_footer.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(16, 0))
        home_footer.columnconfigure(0, weight=1)
        ttk.Label(home_footer, text="Có góp ý? Gửi đánh giá để giúp dự án tốt hơn.",
                  style="IntroText.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Button(home_footer, text="★  Đánh giá ứng dụng", style="Accent.TButton",
                   command=self.open_rating).grid(row=0, column=1, sticky="e")

    def _home_action(self, parent, column, icon, title, description, button_style, command):
        card = ttk.Frame(parent, style="LobbyCard.TFrame", padding=14)
        card.grid(row=1 + column // 2, column=column % 2, sticky="nsew",
                  padx=(0 if column % 2 == 0 else 7, 7 if column % 2 == 0 else 0),
                  pady=(0 if column < 2 else 8, 4))
        icon_canvas = tk.Canvas(card, width=42, height=42, bg=CARD, highlightthickness=0)
        icon_canvas.pack(anchor="w")
        self._draw_home_icon(icon_canvas, column)
        ttk.Label(card, text=title, style="LobbyCardTitle.TLabel", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(4, 2))
        ttk.Label(card, text=description, style="LobbyCardText.TLabel", wraplength=190).pack(anchor="w", pady=(0, 9))
        ttk.Button(card, text="Mở", style=button_style, command=command).pack(fill="x")

    @staticmethod
    def _draw_hero_art(canvas):
        """Ve minh hoa giao dien du lieu theo phong cach bang mach so."""
        canvas.create_rectangle(2, 2, 218, 94, fill=DEEP_PANEL, outline="#405751", width=1)
        for x in range(14, 214, 16):
            canvas.create_line(x, 28, x, 87, fill="#304640", width=1)
        for y in range(34, 91, 14):
            canvas.create_line(8, y, 213, y, fill="#304640", width=1)

        canvas.create_text(13, 16, text="FINANCE / LIVE", anchor="w", fill="#d1ded7",
                           font=("Consolas", 8, "bold"))
        canvas.create_oval(192, 11, 198, 17, fill="#91c9aa", outline="")
        canvas.create_text(205, 14, text="ON", anchor="e", fill="#a9d4b8",
                           font=("Consolas", 7, "bold"))

        # Bieu do du lieu phat sang ben trai.
        canvas.create_line(13, 80, 112, 80, fill="#617a70", width=1)
        canvas.create_line(14, 65, 31, 58, 48, 68, 66, 47, 83, 52, 101, 37, 113, 32,
                           fill="#91c9aa", width=2, smooth=True)
        for x, y in ((31, 58), (66, 47), (101, 37)):
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="#c2d7c9", outline=DEEP_PANEL)

        # The thong minh voi chan ket noi nhu mot chip nho.
        canvas.create_rectangle(137, 37, 202, 78, fill="#293d36", outline="#638976", width=1)
        canvas.create_rectangle(137, 44, 202, 49, fill="#405d50", outline="")
        canvas.create_text(147, 61, text="VÍ CÁ NHÂN", anchor="w", fill="#d8e3da",
                           font=("Consolas", 7, "bold"))
        canvas.create_text(147, 70, text="SAFE  ·  LOCAL", anchor="w", fill="#a9d4b8",
                           font=("Consolas", 6, "bold"))
        for y in (42, 55, 68):
            canvas.create_line(128, y, 137, y, fill="#c2d7c9", width=1)
            canvas.create_oval(124, y - 2, 128, y + 2, fill="#c2d7c9", outline="")

    @staticmethod
    def _draw_home_icon(canvas, kind):
        """Ve bieu tuong don gian, hien thi ro tren cac may Windows."""
        palettes = (
            ("#20372e", GREEN),
            ("#263438", BLUE),
            ("#302d3b", PURPLE),
            ("#39292d", RED),
        )
        background, accent = palettes[kind]
        canvas.create_polygon(10, 2, 32, 2, 41, 21, 32, 40, 10, 40, 1, 21,
                              fill=background, outline=accent, width=1)
        canvas.create_oval(33, 6, 37, 10, fill=accent, outline="")
        if kind == 0:
            canvas.create_rectangle(14, 14, 28, 28, outline=accent, width=1)
            canvas.create_line(21, 17, 21, 25, fill=accent, width=2, capstyle="round")
            canvas.create_line(17, 21, 25, 21, fill=accent, width=2, capstyle="round")
        elif kind == 1:
            for y in (13, 21, 29):
                canvas.create_rectangle(10, y - 2, 14, y + 2, outline=accent, width=1)
                canvas.create_line(18, y, 31, y, fill=accent, width=1)
        elif kind == 2:
            canvas.create_line(10, 31, 32, 31, fill=accent, width=1)
            canvas.create_line(11, 29, 18, 24, 23, 26, 31, 13, fill=accent, width=2,
                               smooth=True, arrow="last")
            for x, y in ((11, 29), (18, 24), (23, 26)):
                canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill=background, outline=accent)
        else:
            canvas.create_oval(10, 10, 32, 32, outline="#a9b8af", width=2)
            canvas.create_arc(10, 10, 32, 32, start=90, extent=260, style="arc",
                              outline=accent, width=3)
            canvas.create_oval(18, 18, 24, 24, fill=background, outline=accent)

    def show_home(self):
        for widget in self.dashboard_widgets:
            widget.grid_remove()
        self.home_panel.grid()
        self.refresh_home()

    def show_dashboard(self, screen):
        self.home_panel.grid_remove()
        self.header.grid()
        self.body.grid()
        self.status.grid()
        self.metrics.grid_remove()

        self.form_panel.grid_remove()
        self.transactions_panel.grid_remove()
        self.report_page.grid_remove()
        self.budget_page.grid_remove()
        self.rating_page.grid_remove()
        self.body.columnconfigure(0, weight=0, minsize=0)
        self.body.columnconfigure(1, weight=0, minsize=0)

        if screen == "add":
            self.header_title.configure(text="Thêm giao dịch")
            self.header_subtitle.configure(text="Ghi lại một khoản thu hoặc chi mới.")
            self.body.columnconfigure(0, weight=1)
            self.form_panel.grid()
            self.amount_entry.focus_set()
        elif screen == "transactions":
            self.header_title.configure(text="Sổ giao dịch")
            self.header_subtitle.configure(text="Tìm, lọc và xem lại các khoản thu chi đã ghi.")
            self.body.columnconfigure(1, weight=1)
            self.transactions_panel.grid()
            self.table.focus_set()
        elif screen == "budget":
            self.header_title.configure(text="Ngân sách tháng")
            self.header_subtitle.configure(text="Đặt hạn mức và theo dõi số tiền đã chi trong tháng.")
            self.body.columnconfigure(0, weight=1)
            self.budget_page.grid()
            self.monthly_budget_entry.focus_set()
            self.refresh_budget()
        elif screen == "report":
            self.header_title.configure(text="Báo cáo thu chi")
            self.header_subtitle.configure(text="Xem số liệu tổng thể hoặc riêng từng tháng.")
            self.body.columnconfigure(0, weight=1)
            self.report_page.grid()
            self.report_month_entry.focus_set()
            self.refresh_report()
        else:
            self.header_title.configure(text="Đánh giá ứng dụng")
            self.header_subtitle.configure(text="Gửi nhận xét để giúp dự án ngày càng tốt hơn.")
            self.body.columnconfigure(0, weight=1)
            self.rating_page.grid()
            self.rating_comment.focus_set()

    def open_add_transaction(self):
        self.show_dashboard("add")

    def open_transactions(self):
        self.show_dashboard("transactions")

    def open_budget(self):
        self.show_dashboard("budget")

    def open_report(self):
        self.show_dashboard("report")

    def open_rating(self):
        self.show_dashboard("rating")

    def _build_rating_page(self, parent):
        self.rating_page = ttk.Frame(parent, style="Card.TFrame", padding=28)
        self.rating_page.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.rating_page.columnconfigure(0, weight=1)
        ttk.Label(self.rating_page, text="Bạn thấy ứng dụng thế nào?", style="Metric.TLabel").grid(
            row=0, column=0, sticky="w"
        )
        ttk.Label(self.rating_page,
                  text="Chọn số sao và để lại góp ý. App sẽ mở email đã điền sẵn để bạn xem lại trước khi gửi.",
                  style="Muted.Card.TLabel", wraplength=760).grid(row=1, column=0, sticky="w", pady=(6, 20))

        self.rating_var = tk.StringVar(value="")
        stars = ttk.Frame(self.rating_page, style="Card.TFrame")
        stars.grid(row=2, column=0, sticky="w", pady=(0, 18))
        for score in range(1, 6):
            ttk.Radiobutton(stars, text=f"★  {score}", value=str(score), variable=self.rating_var,
                            style="Rating.TRadiobutton").pack(side="left", padx=(0, 8))

        ttk.Label(self.rating_page, text="Góp ý của bạn (không bắt buộc)", style="Card.TLabel",
                  font=("Segoe UI", 10, "bold")).grid(row=3, column=0, sticky="w", pady=(0, 7))
        self.rating_comment = tk.Text(self.rating_page, height=8, wrap="word", undo=True,
                                      bg=CARD, fg=INK, insertbackground=INK, relief="flat",
                                      padx=12, pady=10, font=("Segoe UI", 10),
                                      highlightthickness=1, highlightbackground=LINE,
                                      highlightcolor=PURPLE)
        self.rating_comment.grid(row=4, column=0, sticky="ew", pady=(0, 18))
        ttk.Button(self.rating_page, text="Mở email để gửi đánh giá", style="Primary.TButton",
                   command=self.submit_rating).grid(row=5, column=0, sticky="w")
        ttk.Label(self.rating_page, text=f"Email nhận góp ý: {FEEDBACK_EMAIL}",
                  style="Muted.Card.TLabel").grid(row=6, column=0, sticky="w", pady=(12, 0))
        self.rating_page.grid_remove()

    def submit_rating(self):
        score = self.rating_var.get()
        if not score:
            messagebox.showwarning("Chưa chọn số sao", "Hãy chọn mức đánh giá từ 1 đến 5 sao.", parent=self.root)
            return

        comment = self.rating_comment.get("1.0", "end-1c").strip()
        if len(comment) > 1500:
            messagebox.showwarning("Góp ý quá dài", "Vui lòng giữ góp ý dưới 1.500 ký tự.", parent=self.root)
            return

        subject = f"Đánh giá ứng dụng Sổ thu chi: {score}/5 sao"
        body = f"Đánh giá: {score}/5 sao\n\nGóp ý:\n{comment or '(Không có góp ý thêm)'}"
        mailto = f"mailto:{FEEDBACK_EMAIL}?subject={quote(subject)}&body={quote(body)}"
        if webbrowser.open(mailto):
            self.status_var.set("Đã mở ứng dụng email để bạn kiểm tra và gửi đánh giá.")
            messagebox.showinfo("Email đã sẵn sàng", "Email đánh giá đã được soạn. Hãy kiểm tra nội dung rồi bấm Gửi trong ứng dụng email của bạn.", parent=self.root)
        else:
            messagebox.showerror("Không mở được email", "Hãy cài đặt ứng dụng email mặc định trên máy rồi thử lại.", parent=self.root)

    def refresh_home(self):
        if not hasattr(self, "home_income"):
            return
        income = sum(tx.get("amount", 0) for tx in finance.transactions if tx.get("kind") == "Thu")
        expense = sum(tx.get("amount", 0) for tx in finance.transactions if tx.get("kind") == "Chi")
        self.home_income.configure(text=money(income))
        self.home_expense.configure(text=money(expense))
        self.home_balance.configure(text=money(income - expense))

    def _build_report_page(self, parent):
        self.report_page = ttk.Frame(parent, style="Card.TFrame", padding=26)
        self.report_page.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.report_page.columnconfigure(0, weight=1)

        ttk.Label(self.report_page, text="Tổng quan tài chính", style="Metric.TLabel").grid(
            row=0, column=0, sticky="w"
        )
        ttk.Label(self.report_page, text="Tổng hợp từ tất cả giao dịch đã lưu.",
                  style="Muted.Card.TLabel").grid(row=1, column=0, sticky="w", pady=(4, 10))
        overall = ttk.Frame(self.report_page, style="Card.TFrame")
        overall.grid(row=2, column=0, sticky="ew", pady=(0, 24))
        for column in range(3):
            overall.columnconfigure(column, weight=1, uniform="overall_report")
        self.report_all_income = self._metric_card(overall, 0, "TỔNG THU", "IncomeCard")
        self.report_all_expense = self._metric_card(overall, 1, "TỔNG CHI", "ExpenseCard")
        self.report_all_balance = self._metric_card(overall, 2, "SỐ DƯ", "BalanceCard")

        month_bar = ttk.Frame(self.report_page, style="Card.TFrame")
        month_bar.grid(row=3, column=0, sticky="ew", pady=(0, 8))
        month_bar.columnconfigure(2, weight=1)
        ttk.Label(month_bar, text="Báo cáo theo tháng", style="LobbyCardTitle.TLabel").grid(
            row=0, column=0, sticky="w", padx=(0, 18)
        )
        ttk.Label(month_bar, text="Tháng (YYYY-MM)", style="Card.TLabel").grid(
            row=0, column=1, sticky="w", padx=(0, 8)
        )
        self.report_month_entry = ttk.Entry(month_bar, textvariable=self.month_var, width=13)
        self.report_month_entry.grid(row=0, column=2, sticky="w", padx=(0, 8), ipady=4)
        ttk.Button(month_bar, text="Xem báo cáo", style="Accent.TButton",
                   command=self.refresh_report).grid(row=0, column=3, sticky="e")

        monthly = ttk.Frame(self.report_page, style="Card.TFrame")
        monthly.grid(row=4, column=0, sticky="ew")
        for column in range(3):
            monthly.columnconfigure(column, weight=1, uniform="monthly_report")
        self.report_month_income = self._metric_card(monthly, 0, "THU TRONG THÁNG", "IncomeCard")
        self.report_month_expense = self._metric_card(monthly, 1, "CHI TRONG THÁNG", "ExpenseCard")
        self.report_month_balance = self._metric_card(monthly, 2, "SỐ DƯ TRONG THÁNG", "BalanceCard")
        self.report_hint = ttk.Label(self.report_page, text="", style="Muted.Card.TLabel")
        self.report_hint.grid(row=5, column=0, sticky="w", pady=(12, 0))
        self.report_page.grid_remove()

    def refresh_report(self):
        all_income = sum(tx.get("amount", 0) for tx in finance.transactions if tx.get("kind") == "Thu")
        all_expense = sum(tx.get("amount", 0) for tx in finance.transactions if tx.get("kind") == "Chi")
        self.report_all_income.configure(text=money(all_income))
        self.report_all_expense.configure(text=money(all_expense))
        self.report_all_balance.configure(text=money(all_income - all_expense))

        month = self.month_var.get().strip()
        try:
            date.fromisoformat(month + "-01")
        except ValueError:
            for label in (self.report_month_income, self.report_month_expense, self.report_month_balance):
                label.configure(text="—")
            self.report_hint.configure(text="Nhập tháng theo định dạng YYYY-MM, ví dụ 2026-09.", foreground=RED)
            return

        month_transactions = [tx for tx in finance.transactions if tx.get("day", "").startswith(month)]
        month_income = sum(tx.get("amount", 0) for tx in month_transactions if tx.get("kind") == "Thu")
        month_expense = sum(tx.get("amount", 0) for tx in month_transactions if tx.get("kind") == "Chi")
        self.report_month_income.configure(text=money(month_income))
        self.report_month_expense.configure(text=money(month_expense))
        self.report_month_balance.configure(text=money(month_income - month_expense))
        self.report_hint.configure(text=f"{month}: {len(month_transactions)} giao dịch. Số dư tháng = tổng thu tháng − tổng chi tháng.", foreground=MUTED)

    def _build_budget_page(self, parent):
        self.budget_page = ttk.Frame(parent, style="Card.TFrame", padding=28)
        self.budget_page.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.budget_page.columnconfigure(0, weight=1)
        ttk.Label(self.budget_page, text="Theo dõi ngân sách", style="Metric.TLabel").grid(
            row=0, column=0, sticky="w"
        )
        ttk.Label(self.budget_page,
                  text="Chọn tháng cần theo dõi. Hạn mức chỉ áp dụng cho các khoản chi trong tháng đó.",
                  style="Muted.Card.TLabel", wraplength=700).grid(row=1, column=0, sticky="w", pady=(6, 20))

        controls = ttk.Frame(self.budget_page, style="Card.TFrame")
        controls.grid(row=2, column=0, sticky="w", pady=(0, 20))
        ttk.Label(controls, text="Tháng (YYYY-MM)", style="Card.TLabel").grid(row=0, column=0, sticky="w", padx=(0, 10))
        self.monthly_budget_entry = ttk.Entry(controls, textvariable=self.month_var, width=14)
        self.monthly_budget_entry.grid(row=0, column=1, sticky="w", padx=(0, 10), ipady=4)
        ttk.Button(controls, text="Cập nhật", style="Accent.TButton", command=self.refresh_budget).grid(row=0, column=2)

        summary = ttk.Frame(self.budget_page, style="Card.TFrame")
        summary.grid(row=3, column=0, sticky="ew", pady=(0, 18))
        summary.columnconfigure(0, weight=1)
        ttk.Label(summary, text="Tình hình ngân sách", style="LobbyCardTitle.TLabel").grid(
            row=0, column=0, sticky="w", pady=(0, 12)
        )
        self.budget_page_text = ttk.Label(summary, text="", style="Card.TLabel", wraplength=750,
                                          font=("Segoe UI", 13, "bold"))
        self.budget_page_text.grid(row=1, column=0, sticky="w", pady=(0, 12))
        self.budget_text = self.budget_page_text
        self.budget_page_progress = ttk.Progressbar(
            summary, style="Budget.Horizontal.TProgressbar", mode="determinate", maximum=100
        )
        self.budget_page_progress.grid(row=2, column=0, sticky="ew", pady=(0, 8))
        self.budget_progress = self.budget_page_progress
        self.budget_page_hint = ttk.Label(summary, text="", style="Muted.Card.TLabel")
        self.budget_page_hint.grid(row=3, column=0, sticky="w")
        ttk.Button(self.budget_page, text="Đặt hoặc sửa hạn mức", style="Primary.TButton",
                   command=self.set_budget).grid(row=4, column=0, sticky="w")
        self.budget_page.grid_remove()

    def _metric_card(self, parent, column, title, theme, row=0):
        card = ttk.Frame(parent, style=f"{theme}.TFrame", padding=(14, 8))
        card.grid(row=row, column=column, sticky="ew",
                  padx=(0 if column == 0 else 6, 6 if column < 2 else 0),
                  pady=(0 if row == 0 else 6, 0))
        ttk.Label(card, text=title, style=f"{theme}.Muted.TLabel").pack(anchor="w")
        value = ttk.Label(card, text="0 ₫", style=f"{theme}.Value.TLabel")
        value.pack(anchor="w", pady=(6, 0))
        return value

    def _build_form(self, parent):
        panel = ttk.Frame(parent, style="Card.TFrame", padding=20)
        self.form_panel = panel
        panel.grid(row=0, column=0, sticky="nsew", padx=(0, 14))
        panel.columnconfigure(0, weight=1)
        ttk.Label(panel, text="Thêm giao dịch", style="Metric.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Label(panel, text="Nhập thông tin khoản thu hoặc chi.", style="Muted.Card.TLabel").grid(
            row=1, column=0, sticky="w", pady=(4, 18)
        )

        self._field_label(panel, 2, "Loại giao dịch")
        ttk.Combobox(panel, textvariable=self.kind_var, values=("Thu", "Chi"),
                     state="readonly").grid(row=3, column=0, sticky="ew", pady=(5, 13), ipady=3)
        self._field_label(panel, 4, "Số tiền (₫)")
        self.amount_entry = ttk.Entry(panel, textvariable=self.amount_var)
        self.amount_entry.grid(row=5, column=0, sticky="ew", pady=(5, 13), ipady=4)
        self._field_label(panel, 6, "Danh mục")
        ttk.Entry(panel, textvariable=self.category_var).grid(row=7, column=0, sticky="ew", pady=(5, 13), ipady=4)
        self._field_label(panel, 8, "Ngày (YYYY-MM-DD)")
        ttk.Entry(panel, textvariable=self.day_var).grid(row=9, column=0, sticky="ew", pady=(5, 13), ipady=4)
        self._field_label(panel, 10, "Ghi chú (không bắt buộc)")
        ttk.Entry(panel, textvariable=self.note_var).grid(row=11, column=0, sticky="ew", pady=(5, 15), ipady=4)
        ttk.Button(panel, text="＋  Lưu giao dịch", style="Primary.TButton",
                   command=self.add_transaction).grid(row=12, column=0, sticky="ew", ipady=2)
        ttk.Label(panel, text="Mẹo: Ctrl + Enter để lưu nhanh.", style="Muted.Card.TLabel").grid(
            row=13, column=0, sticky="w", pady=(8, 2)
        )

    @staticmethod
    def _field_label(parent, row, text):
        ttk.Label(parent, text=text, style="Card.TLabel", font=("Segoe UI", 9, "bold")).grid(
            row=row, column=0, sticky="w"
        )

    def _build_transactions(self, parent):
        panel = ttk.Frame(parent, style="Card.TFrame", padding=18)
        self.transactions_panel = panel
        panel.grid(row=0, column=1, sticky="nsew")
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(3, weight=1)

        title_row = ttk.Frame(panel, style="Card.TFrame")
        title_row.grid(row=0, column=0, sticky="ew")
        title_row.columnconfigure(0, weight=1)
        ttk.Label(title_row, text="Giao dịch", style="Metric.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Button(title_row, text="Sửa đã chọn", style="Accent.TButton",
                   command=self.edit_selected).grid(row=0, column=1, sticky="e", padx=(0, 8))
        ttk.Button(title_row, text="Xóa giao dịch đã chọn", style="Danger.TButton",
                   command=self.delete_selected).grid(row=0, column=2, sticky="e", padx=(0, 8))
        ttk.Button(title_row, text="Hiện tất cả", style="Accent.TButton",
                   command=self.show_all).grid(row=0, column=3, sticky="e")

        filters = ttk.Frame(panel, style="Card.TFrame", padding=(0, 14, 0, 13))
        filters.grid(row=1, column=0, sticky="ew")
        filters.columnconfigure(1, weight=1)
        filters.columnconfigure(5, weight=1)
        ttk.Label(filters, text="Tháng", style="Card.TLabel").grid(row=0, column=0, sticky="w", padx=(0, 7))
        ttk.Entry(filters, textvariable=self.month_var, width=11).grid(row=0, column=1, sticky="ew", padx=(0, 7), ipady=3)
        ttk.Button(filters, text="Lọc tháng", style="Accent.TButton", command=self.filter_month).grid(row=0, column=2, padx=(0, 18))
        ttk.Label(filters, text="Danh mục", style="Card.TLabel").grid(row=0, column=3, sticky="w", padx=(0, 7))
        ttk.Entry(filters, textvariable=self.category_filter_var, width=14).grid(row=0, column=4, sticky="ew", padx=(0, 7), ipady=3)
        ttk.Button(filters, text="Tìm", style="Accent.TButton", command=self.filter_category).grid(row=0, column=5, sticky="w")
        ttk.Label(panel, text="Tháng theo dạng YYYY-MM  ·  Tìm danh mục theo tên hoặc một phần tên.",
                  style="Muted.Card.TLabel").grid(row=2, column=0, sticky="w", pady=(0, 9))

        table_frame = ttk.Frame(panel, style="Card.TFrame")
        table_frame.grid(row=3, column=0, sticky="nsew")
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)
        columns = ("day", "kind", "category", "amount", "note")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        headings = (("day", "Ngày", 105), ("kind", "Loại", 72), ("category", "Danh mục", 120),
                    ("amount", "Số tiền", 135), ("note", "Ghi chú", 180))
        for column, title, width in headings:
            self.table.heading(column, text=title)
            self.table.column(column, width=width, minwidth=65, stretch=column in ("category", "note"),
                              anchor="e" if column == "amount" else "w")
        self.table.grid(row=0, column=0, sticky="nsew")
        vertical = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        vertical.grid(row=0, column=1, sticky="ns")
        horizontal = ttk.Scrollbar(table_frame, orient="horizontal", command=self.table.xview)
        horizontal.grid(row=1, column=0, sticky="ew")
        self.table.configure(yscrollcommand=vertical.set, xscrollcommand=horizontal.set)
        self.table.tag_configure("income", foreground="#8bd3b2", background="#202d28")
        self.table.tag_configure("expense", foreground="#f0a3aa", background="#2c2528")
        self.table.tag_configure("alternate", background="#222c2d")

        actions = ttk.Frame(panel, style="Card.TFrame")
        actions.grid(row=4, column=0, sticky="ew", pady=(12, 0))
        self.result_label = ttk.Label(actions, text="", style="Muted.Card.TLabel")
        self.result_label.pack(side="left")
        ttk.Label(actions, text="Chọn một dòng trong bảng rồi bấm nút Xóa phía trên.",
                  style="Muted.Card.TLabel").pack(side="right", padx=(10, 0))
        self.table.bind("<Delete>", lambda _event: self.delete_selected())
        self.table.bind("<Double-1>", lambda _event: self.edit_selected())

    def add_transaction(self):
        try:
            amount = int(self.amount_var.get().strip())
        except ValueError:
            messagebox.showerror("Số tiền chưa hợp lệ", "Hãy nhập số nguyên dương, ví dụ 50000.", parent=self.root)
            self.amount_entry.focus_set()
            return
        if amount <= 0:
            messagebox.showerror("Số tiền chưa hợp lệ", "Số tiền phải lớn hơn 0.", parent=self.root)
            self.amount_entry.focus_set()
            return

        category = self.category_var.get().strip()
        if not category:
            messagebox.showerror("Thiếu danh mục", "Hãy nhập danh mục cho giao dịch.", parent=self.root)
            return
        transaction_day = self.day_var.get().strip()
        try:
            date.fromisoformat(transaction_day)
        except ValueError:
            messagebox.showerror("Ngày chưa hợp lệ", "Nhập ngày theo dạng YYYY-MM-DD.", parent=self.root)
            return

        finance.transactions.append({
            "kind": self.kind_var.get(), "amount": amount, "category": category,
            "day": transaction_day, "note": self.note_var.get().strip(),
        })
        if not finance.save_transactions():
            finance.transactions.pop()
            messagebox.showerror(
                "Không thể lưu dữ liệu",
                "Giao dịch chưa được lưu vào file. Hãy kiểm tra quyền ghi thư mục rồi thử lại.",
                parent=self.root,
            )
            return
        self.amount_var.set("")
        self.category_var.set("")
        self.note_var.set("")
        self.status_var.set("Đã lưu giao dịch.")
        self.refresh()
        self.amount_entry.focus_set()

    def filter_month(self):
        month = self.month_var.get().strip()
        try:
            date.fromisoformat(month + "-01")
        except ValueError:
            messagebox.showerror("Tháng chưa hợp lệ", "Nhập tháng theo dạng YYYY-MM, ví dụ 2026-09.", parent=self.root)
            return
        self.active_month = month
        self.refresh()

    def filter_category(self):
        category = self.category_filter_var.get().strip()
        if not category:
            messagebox.showerror("Thiếu danh mục", "Nhập tên hoặc một phần tên danh mục.", parent=self.root)
            return
        self.active_category = category.casefold()
        self.refresh()

    def show_all(self):
        self.active_month = None
        self.active_category = ""
        self.category_filter_var.set("")
        self.refresh()

    def visible_transactions(self):
        records = list(enumerate(finance.transactions))
        if self.active_month:
            records = [(index, tx) for index, tx in records if tx.get("day", "").startswith(self.active_month)]
        if self.active_category:
            records = [(index, tx) for index, tx in records
                       if self.active_category in tx.get("category", "").casefold()]
        return sorted(records, key=lambda item: (item[1].get("day", ""), item[0]), reverse=True)

    def refresh(self):
        visible = self.visible_transactions()
        for row in self.table.get_children():
            self.table.delete(row)
        for row_number, (index, tx) in enumerate(visible):
            tag = "income" if tx.get("kind") == "Thu" else "expense"
            tags = (tag, "alternate") if row_number % 2 else (tag,)
            self.table.insert("", "end", iid=str(index), values=(
                tx.get("day", "Chưa có ngày"), tx.get("kind", "Không rõ"),
                tx.get("category", "Không rõ"), money(tx.get("amount", 0)), tx.get("note", ""),
            ), tags=tags)

        records = [tx for _, tx in visible]
        income = sum(tx.get("amount", 0) for tx in records if tx.get("kind") == "Thu")
        expense = sum(tx.get("amount", 0) for tx in records if tx.get("kind") == "Chi")
        self.income_value.configure(text=money(income))
        self.expense_value.configure(text=money(expense))
        self.balance_value.configure(text=money(income - expense))
        self.result_label.configure(text=f"{len(records)} giao dịch đang hiển thị")
        self.refresh_budget()
        self.refresh_home()

    def refresh_budget(self):
        month = self.month_var.get().strip()
        try:
            date.fromisoformat(month + "-01")
        except ValueError:
            self.budget_text.configure(text="Nhập tháng dạng YYYY-MM để xem ngân sách.")
            self.budget_progress.configure(value=0)
            self.budget_page_hint.configure(text="Tháng không hợp lệ. Hãy dùng định dạng YYYY-MM.")
            return

        month_expense = sum(tx.get("amount", 0) for tx in finance.transactions
                            if tx.get("kind") == "Chi" and tx.get("day", "").startswith(month))
        budget = finance.monthly_budgets.get(month)
        if budget is None:
            self.budget_text.configure(text=f"{month}: đã chi {money(month_expense)}. Chưa đặt hạn mức.", foreground=INK)
            self.budget_progress.configure(value=0)
            self.budget_progress.configure(style="Budget.Horizontal.TProgressbar")
            self.budget_page_hint.configure(text="Bạn chưa đặt hạn mức cho tháng này.")
            return

        remaining = budget - month_expense
        percent = min(month_expense / budget * 100, 100) if budget else 0
        self.budget_progress.configure(value=percent)
        if remaining < 0:
            self.budget_text.configure(text=f"{month}: đã chi {money(month_expense)}, vượt {money(abs(remaining))}.", foreground=RED)
            self.budget_progress.configure(style="OverBudget.Horizontal.TProgressbar")
            self.budget_page_hint.configure(text=f"Đã dùng {month_expense / budget * 100:.0f}% hạn mức. Hãy cân nhắc các khoản chi tiếp theo.")
        else:
            self.budget_text.configure(text=f"{month}: đã chi {money(month_expense)}. Còn {money(remaining)} / {money(budget)}.", foreground=GREEN)
            self.budget_progress.configure(style="Budget.Horizontal.TProgressbar")
            self.budget_page_hint.configure(text=f"Đã dùng {month_expense / budget * 100:.0f}% hạn mức tháng này.")

    def set_budget(self):
        month = self.month_var.get().strip()
        try:
            date.fromisoformat(month + "-01")
        except ValueError:
            messagebox.showerror("Tháng chưa hợp lệ", "Nhập tháng theo dạng YYYY-MM trước.", parent=self.root)
            return
        current = finance.monthly_budgets.get(month, 0)
        amount = simpledialog.askinteger("Ngân sách tháng", f"Hạn mức chi cho {month} (₫). Nhập 0 để tắt:",
                                         initialvalue=current, minvalue=0, parent=self.root)
        if amount is None:
            return
        previous = finance.monthly_budgets.get(month)
        if amount == 0:
            finance.monthly_budgets.pop(month, None)
        else:
            finance.monthly_budgets[month] = amount
        if not finance.save_budgets():
            if previous is None:
                finance.monthly_budgets.pop(month, None)
            else:
                finance.monthly_budgets[month] = previous
            messagebox.showerror(
                "Không thể lưu ngân sách",
                "Ngân sách chưa được lưu vào file. Hãy kiểm tra quyền ghi thư mục rồi thử lại.",
                parent=self.root,
            )
            return
        if amount == 0:
            self.status_var.set(f"Đã tắt ngân sách tháng {month}.")
        else:
            self.status_var.set(f"Đã đặt ngân sách tháng {month}: {money(amount)}.")
        self.refresh_budget()

    def edit_selected(self):
        selection = self.table.selection()
        if not selection:
            messagebox.showinfo("Chưa chọn giao dịch", "Chọn một dòng trong danh sách rồi bấm Sửa.", parent=self.root)
            return

        index = int(selection[0])
        transaction = finance.transactions[index]
        dialog = tk.Toplevel(self.root)
        dialog.title("Sửa giao dịch")
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.configure(bg=BG)
        dialog.resizable(False, False)

        form = ttk.Frame(dialog, style="Card.TFrame", padding=22)
        form.pack(fill="both", expand=True)
        form.columnconfigure(0, weight=1)
        ttk.Label(form, text="Cập nhật thông tin", style="Metric.TLabel").grid(
            row=0, column=0, sticky="w", pady=(0, 14)
        )

        kind_var = tk.StringVar(value=transaction.get("kind", "Chi"))
        amount_var = tk.StringVar(value=str(transaction.get("amount", "")))
        category_var = tk.StringVar(value=transaction.get("category", ""))
        day_var = tk.StringVar(value=transaction.get("day", ""))
        note_var = tk.StringVar(value=transaction.get("note", ""))

        fields = (
            ("Loại giao dịch", ttk.Combobox(form, textvariable=kind_var, values=("Thu", "Chi"), state="readonly")),
            ("Số tiền (₫)", ttk.Entry(form, textvariable=amount_var)),
            ("Danh mục", ttk.Entry(form, textvariable=category_var)),
            ("Ngày (YYYY-MM-DD)", ttk.Entry(form, textvariable=day_var)),
            ("Ghi chú", ttk.Entry(form, textvariable=note_var)),
        )
        for row, (label, field) in enumerate(fields, start=1):
            ttk.Label(form, text=label, style="Card.TLabel",
                      font=("Segoe UI", 9, "bold")).grid(row=row * 2 - 1, column=0, sticky="w")
            field.grid(row=row * 2, column=0, sticky="ew", pady=(3, 9), ipady=3)

        def save_changes(_event=None):
            try:
                amount = int(amount_var.get().strip())
            except ValueError:
                messagebox.showerror("Số tiền chưa hợp lệ", "Hãy nhập số nguyên dương.", parent=dialog)
                return
            if amount <= 0:
                messagebox.showerror("Số tiền chưa hợp lệ", "Số tiền phải lớn hơn 0.", parent=dialog)
                return
            category = category_var.get().strip()
            if not category:
                messagebox.showerror("Thiếu danh mục", "Danh mục không được để trống.", parent=dialog)
                return
            transaction_day = day_var.get().strip()
            try:
                date.fromisoformat(transaction_day)
            except ValueError:
                messagebox.showerror("Ngày chưa hợp lệ", "Nhập ngày theo dạng YYYY-MM-DD.", parent=dialog)
                return

            previous = transaction.copy()
            transaction.update({
                "kind": kind_var.get(),
                "amount": amount,
                "category": category,
                "day": transaction_day,
                "note": note_var.get().strip(),
            })
            if not finance.save_transactions():
                transaction.clear()
                transaction.update(previous)
                messagebox.showerror(
                    "Không thể lưu dữ liệu",
                    "Thay đổi chưa được lưu vào file. Hãy kiểm tra quyền ghi thư mục rồi thử lại.",
                    parent=dialog,
                )
                return
            self.status_var.set("Đã cập nhật giao dịch.")
            dialog.destroy()
            self.refresh()
            row_id = str(index)
            if self.table.exists(row_id):
                self.table.selection_set(row_id)
                self.table.see(row_id)

        buttons = ttk.Frame(form, style="Card.TFrame")
        buttons.grid(row=11, column=0, sticky="e", pady=(5, 0))
        ttk.Button(buttons, text="Hủy", style="Accent.TButton", command=dialog.destroy).pack(side="left", padx=(0, 8))
        ttk.Button(buttons, text="Lưu thay đổi", style="Primary.TButton", command=save_changes).pack(side="left")
        dialog.bind("<Control-Return>", save_changes)
        dialog.bind("<Escape>", lambda _event: dialog.destroy())
        fields[1][1].focus_set()

    def delete_selected(self):
        selection = self.table.selection()
        if not selection:
            messagebox.showinfo("Chưa chọn giao dịch", "Chọn một giao dịch trong danh sách trước.", parent=self.root)
            return
        index = int(selection[0])
        transaction = finance.transactions[index]
        description = f"{transaction.get('category', 'Giao dịch')} · {money(transaction.get('amount', 0))}"
        if not messagebox.askyesno("Xóa giao dịch", f"Bạn có chắc muốn xóa {description}?", parent=self.root):
            return
        deleted = finance.transactions.pop(index)
        if not finance.save_transactions():
            finance.transactions.insert(index, deleted)
            messagebox.showerror(
                "Không thể lưu dữ liệu",
                "Giao dịch chưa bị xóa khỏi file. Hãy kiểm tra quyền ghi thư mục rồi thử lại.",
                parent=self.root,
            )
            return
        self.status_var.set("Đã xóa giao dịch.")
        self.refresh()


def main():
    finance.transactions = finance.load_transactions()
    finance.monthly_budgets = finance.load_budgets()
    root = tk.Tk()
    FinanceWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
