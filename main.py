import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from collections import Counter
import re
import random
from datetime import datetime

# ==========================================
# NOVA AI - ACCURACY ANALYZER
# Pure Python | Standard Library Only
# ==========================================

BG = "#080D19"
PANEL = "#111B2D"
ACCENT = "#00D9FF"
PURPLE = "#9B7CFF"
GREEN = "#00E6A0"
WHITE = "#EAF2FF"
MUTED = "#8293AD"


class NovaAI:
    def __init__(self, root):
        self.root = root
        self.root.title("NOVA AI | Accuracy Intelligence")
        self.root.geometry("1150x780")
        self.root.minsize(950, 680)
        self.root.configure(bg=BG)

        self.particles = []
        self.report = ""

        self.setup_style()
        self.build_interface()
        self.animate_background()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TProgressbar",
            troughcolor="#202D43",
            background=ACCENT,
            thickness=9
        )

    def build_interface(self):
        # Animated background
        self.canvas = tk.Canvas(
            self.root, bg=BG, highlightthickness=0
        )
        self.canvas.place(relwidth=1, relheight=1)

        for _ in range(45):
            x = random.randint(0, 1150)
            y = random.randint(0, 780)
            speed = random.uniform(0.2, 1.0)
            self.particles.append(
                [x, y, speed, random.randint(1, 3)]
            )

        # Main layout
        main = tk.Frame(self.root, bg=BG)
        main.pack(fill="both", expand=True, padx=35, pady=22)
        main.lift()

        # Header
        header = tk.Frame(main, bg=BG)
        header.pack(fill="x", pady=(0, 22))

        tk.Label(
            header, text="NOVA AI",
            font=("Segoe UI", 27, "bold"),
            fg=ACCENT, bg=BG
        ).pack(side="left")

        tk.Label(
            header, text="  /  INTELLIGENCE ANALYZER",
            font=("Segoe UI", 11, "bold"),
            fg=WHITE, bg=BG
        ).pack(side="left", pady=(12, 0))

        self.status = tk.Label(
            header, text="● SYSTEM ONLINE",
            font=("Segoe UI", 9, "bold"),
            fg=GREEN, bg=BG
        )
        self.status.pack(side="right", pady=12)

        # Input panels
        inputs = tk.Frame(main, bg=BG)
        inputs.pack(fill="both", expand=True)

        self.expected_box = self.create_input_panel(
            inputs, "EXPECTED ANSWER",
            "Enter the reference answer..."
        )
        self.ai_box = self.create_input_panel(
            inputs, "AI GENERATED ANSWER",
            "Enter the AI response..."
        )

        # Analyze button
        tk.Button(
            main,
            text="⚡  ANALYZE AI ACCURACY",
            font=("Segoe UI", 12, "bold"),
            bg=ACCENT, fg=BG,
            activebackground="#72E9FF",
            activeforeground=BG,
            relief="flat", cursor="hand2",
            command=self.analyze,
            pady=13
        ).pack(fill="x", pady=18)

        # Results panel
        results = tk.Frame(
            main, bg=PANEL,
            highlightbackground="#263A55",
            highlightthickness=1
        )
        results.pack(fill="x")

        tk.Label(
            results, text="ANALYSIS DASHBOARD",
            font=("Segoe UI", 12, "bold"),
            fg=WHITE, bg=PANEL
        ).pack(anchor="w", padx=18, pady=(15, 10))

        self.score = tk.Label(
            results, text="--%",
            font=("Segoe UI", 35, "bold"),
            fg=ACCENT, bg=PANEL
        )
        self.score.pack()

        tk.Label(
            results, text="TEXT OVERLAP SCORE",
            font=("Segoe UI", 9, "bold"),
            fg=MUTED, bg=PANEL
        ).pack(pady=(0, 12))

        metrics = tk.Frame(results, bg=PANEL)
        metrics.pack(fill="x", padx=15, pady=(0, 16))

        self.metric_labels = {}

        for name in ["Precision", "Recall", "F1 Score"]:
            card = tk.Frame(
                metrics, bg="#19273C",
                padx=12, pady=10
            )
            card.pack(side="left", fill="x", expand=True, padx=5)

            tk.Label(
                card, text=name.upper(),
                fg=MUTED, bg="#19273C",
                font=("Segoe UI", 8, "bold")
            ).pack()

            value = tk.Label(
                card, text="--%",
                fg=WHITE, bg="#19273C",
                font=("Segoe UI", 18, "bold")
            )
            value.pack()

            self.metric_labels[name] = value

        self.result_text = tk.Label(
            results, text="Waiting for analysis...",
            font=("Segoe UI", 10),
            fg=MUTED, bg=PANEL
        )
        self.result_text.pack(pady=(0, 15))

        # Footer
        footer = tk.Frame(main, bg=BG)
        footer.pack(fill="x", pady=(15, 0))

        tk.Label(
            footer, text="NOVA AI  |  PYTHON INTELLIGENCE ENGINE",
            font=("Segoe UI", 8),
            fg=MUTED, bg=BG
        ).pack(side="left")

        tk.Button(
            footer, text="SAVE REPORT",
            font=("Segoe UI", 9, "bold"),
            bg="#19273C", fg=ACCENT,
            activebackground="#263A55",
            relief="flat", cursor="hand2",
            command=self.save_report,
            padx=15, pady=8
        ).pack(side="right")

    def create_input_panel(self, parent, title, placeholder):
        panel = tk.Frame(
            parent, bg=PANEL,
            highlightbackground="#263A55",
            highlightthickness=1
        )
        panel.pack(
            side="left", fill="both",
            expand=True, padx=7
        )

        tk.Label(
            panel, text=title,
            font=("Segoe UI", 10, "bold"),
            fg=ACCENT, bg=PANEL
        ).pack(anchor="w", padx=15, pady=12)

        box = tk.Text(
            panel, height=7,
            bg="#0C1423", fg=WHITE,
            insertbackground=ACCENT,
            font=("Consolas", 10),
            wrap="word", relief="flat",
            padx=12, pady=12,
            undo=True
        )
        box.pack(
            fill="both", expand=True,
            padx=12, pady=(0, 12)
        )

        box.insert("1.0", placeholder)
        box.config(fg=MUTED)

        def focus_in(event):
            if box.get("1.0", "end-1c") == placeholder:
                box.delete("1.0", "end")
                box.config(fg=WHITE)

        def focus_out(event):
            if not box.get("1.0", "end-1c").strip():
                box.insert("1.0", placeholder)
                box.config(fg=MUTED)

        box.bind("<FocusIn>", focus_in)
        box.bind("<FocusOut>", focus_out)

        return box

    @staticmethod
    def tokenize(text):
        return re.findall(r"\b\w+\b", text.lower())

    def analyze(self):
        expected = self.expected_box.get("1.0", "end-1c").strip()
        actual = self.ai_box.get("1.0", "end-1c").strip()

        if not expected or not actual:
            messagebox.showwarning(
                "Missing Input",
                "Please enter both answers before analysis."
            )
            return

        ref = Counter(self.tokenize(expected))
        ans = Counter(self.tokenize(actual))

        if not ref or not ans:
            messagebox.showwarning(
                "Invalid Input",
                "Please enter meaningful text in both boxes."
            )
            return

        common = sum((ref & ans).values())

        precision = common / sum(ans.values())
        recall = common / sum(ref.values())

        f1 = (
            2 * precision * recall / (precision + recall)
            if precision + recall else 0
        )

        accuracy = f1 * 100

        missing = list((ref - ans).elements())
        extra = list((ans - ref).elements())

        self.score.config(text=f"{accuracy:.1f}%")

        self.metric_labels["Precision"].config(
            text=f"{precision * 100:.1f}%"
        )
        self.metric_labels["Recall"].config(
            text=f"{recall * 100:.1f}%"
        )
        self.metric_labels["F1 Score"].config(
            text=f"{f1 * 100:.1f}%"
        )

        if accuracy >= 80:
            verdict = "STRONG TEXT SIMILARITY"
            color = GREEN
        elif accuracy >= 50:
            verdict = "MODERATE TEXT SIMILARITY"
            color = "#FFC857"
        else:
            verdict = "LOW TEXT SIMILARITY"
            color = "#FF657A"

        self.result_text.config(
            text=f"● {verdict}",
            fg=color
        )

        self.report = f"""
NOVA AI - ACCURACY ANALYSIS REPORT
===================================

Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}

EXPECTED ANSWER:
{expected}

AI GENERATED ANSWER:
{actual}

ANALYSIS METRICS:
-----------------
Text Similarity (F1): {accuracy:.2f}%
Precision: {precision * 100:.2f}%
Recall: {recall * 100:.2f}%
F1 Score: {f1 * 100:.2f}%

MATCHED WORD COUNT: {common}

MISSING WORDS:
{', '.join(missing) if missing else 'None'}

EXTRA WORDS:
{', '.join(extra) if extra else 'None'}

VERDICT: {verdict}

IMPORTANT:
This is a token-level text similarity measurement.
It does not establish factual correctness, meaning,
or semantic equivalence.
"""

        self.status.config(text="● ANALYSIS COMPLETE", fg=GREEN)

    def save_report(self):
        if not self.report:
            messagebox.showinfo(
                "No Report",
                "Run an analysis before saving a report."
            )
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Report", "*.txt")],
            initialfile="NOVA_AI_Report.txt"
        )

        if path:
            try:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(self.report)

                messagebox.showinfo(
                    "Success",
                    "Your analysis report was saved successfully!"
                )
            except OSError as error:
                messagebox.showerror("Save Error", str(error))

    def animate_background(self):
        self.canvas.delete("particles")

        width = self.root.winfo_width()
        height = self.root.winfo_height()

        for particle in self.particles:
            x, y, speed, size = particle

            self.canvas.create_oval(
                x, y, x + size, y + size,
                fill="#17405A",
                outline="",
                tags="particles"
            )

            particle[1] += speed

            if particle[1] > height:
                particle[1] = 0
                particle[0] = random.randint(0, width)

        self.root.after(35, self.animate_background)


if __name__ == "__main__":
    root = tk.Tk()
    app = NovaAI(root)
    root.mainloop()