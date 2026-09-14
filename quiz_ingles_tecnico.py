"""
Quiz de Ingles Tecnico - Simple Present vs Present Continuous
Tema: vocabulario de Ciencia da Computacao

Como executar:
    python quiz_ingles_tecnico.py

Requisitos: apenas Python 3 (tkinter ja vem incluso na instalacao padrao).
"""

import random
import tkinter as tk
from tkinter import ttk

COR_FUNDO = "#0f172a"
COR_PAINEL = "#1e293b"
COR_DESTAQUE = "#38bdf8"
COR_TEXTO = "#e2e8f0"
COR_CERTO = "#22c55e"
COR_ERRADO = "#ef4444"
COR_BOTAO = "#334155"
COR_BOTAO_HOVER = "#475569"

PERGUNTAS = [
    {
        "pergunta": "Every night, the server ______ a backup of all databases.",
        "opcoes": ["run", "runs", "is running", "are running"],
        "correta": 1,
        "explicacao": "Acao habitual/rotina -> Simple Present. 3a pessoa do singular (server = it) recebe 's': runs.",
    },
    {
        "pergunta": "Look at the screen! The system ______ right now.",
        "opcoes": ["update", "updates", "is updating", "updated"],
        "correta": 2,
        "explicacao": "'Right now' indica acao em andamento no momento da fala -> Present Continuous: is/are/am + verbo-ing.",
    },
    {
        "pergunta": "Which sentence is in the SIMPLE PRESENT?",
        "opcoes": [
            "The algorithm is sorting the array.",
            "The compiler translates the source code into machine code.",
            "She is debugging the program at the moment.",
            "They are uploading the files now.",
        ],
        "correta": 1,
        "explicacao": "Frases habituais/verdades gerais sobre o que o compilador faz -> Simple Present (translates).",
    },
    {
        "pergunta": "The programmer ______ (write) clean code every day.",
        "opcoes": ["write", "writes", "is writing", "writing"],
        "correta": 1,
        "explicacao": "'Every day' e um marcador de habito -> Simple Present. Sujeito 'the programmer' = he/she/it, entao +s.",
    },
    {
        "pergunta": "At this moment, the developers ______ a critical bug in production.",
        "opcoes": ["fix", "fixes", "are fixing", "fixed"],
        "correta": 2,
        "explicacao": "'At this moment' = agora -> Present Continuous. Sujeito plural (developers) usa 'are'.",
    },
    {
        "pergunta": "Complete corretamente: 'She usually ______ her code before pushing to GitHub.'",
        "opcoes": ["test", "tests", "is testing", "testing"],
        "correta": 1,
        "explicacao": "'Usually' e um adverbio de frequencia tipico do Simple Present -> tests (3a pessoa +s).",
    },
    {
        "pergunta": "Qual e a forma NEGATIVA correta? 'The application ______ (not / work) properly at the moment.'",
        "opcoes": ["doesn't work", "don't work", "isn't working", "wasn't working"],
        "correta": 2,
        "explicacao": "'At the moment' -> Present Continuous negativo: to be (isn't/aren't) + verbo-ing.",
    },
    {
        "pergunta": "Which alternative shows the correct structure of the PRESENT CONTINUOUS?",
        "opcoes": [
            "verb to be (present) + main verb + ing",
            "verb to be (present) + to + main verb",
            "main verb + ing",
            "do/does + main verb + ing",
        ],
        "correta": 0,
        "explicacao": "Estrutura do Present Continuous: sujeito + to be (am/is/are) + verbo principal + ing.",
    },
    {
        "pergunta": "The company's servers ______ (process) thousands of requests per second on average.",
        "opcoes": ["process", "processes", "is processing", "are processing"],
        "correta": 0,
        "explicacao": "'On average' indica uma verdade geral/rotina -> Simple Present. Sujeito plural 'servers' (they) nao recebe 's': process.",
    },
    {
        "pergunta": "Right now, my laptop ______ (restart) because of a system update.",
        "opcoes": ["restart", "restarts", "is restarting", "restarted"],
        "correta": 2,
        "explicacao": "'Right now' indica acao em progresso -> Present Continuous: is + restarting.",
    },
    {
        "pergunta": "Which sentence is in the PRESENT CONTINUOUS?",
        "opcoes": [
            "Our team deploys new features every Friday.",
            "The network connects automatically to known Wi-Fi networks.",
            "The engineers are testing the new API right now.",
            "This function returns a boolean value.",
        ],
        "correta": 2,
        "explicacao": "'Right now' + are + testing -> Present Continuous, acao em andamento.",
    },
    {
        "pergunta": "Complete: 'Data scientists usually ______ (analyze) large datasets to find patterns.'",
        "opcoes": ["analyze", "analyzes", "is analyzing", "are analyzing"],
        "correta": 0,
        "explicacao": "Sujeito plural (data scientists = they) + 'usually' (habito) -> Simple Present sem 's': analyze.",
    },
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz - Ingles Tecnico | Simple Present vs Present Continuous")
        self.root.geometry("820x560")
        self.root.configure(bg=COR_FUNDO)
        self.root.resizable(False, False)

        self.perguntas = list(PERGUNTAS)
        self.indice = 0
        self.pontos = 0
        self.respondeu = False

        self.container = tk.Frame(self.root, bg=COR_FUNDO)
        self.container.pack(fill="both", expand=True)

        self.tela_inicial()

    def limpar_tela(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def tela_inicial(self):
        self.limpar_tela()

        tk.Label(
            self.container,
            text="Inglês Técnico",
            font=("Segoe UI", 32, "bold"),
            fg=COR_DESTAQUE,
            bg=COR_FUNDO,
        ).pack(pady=(60, 5))

        tk.Label(
            self.container,
            text="Simple Present  vs  Present Continuous",
            font=("Segoe UI", 18),
            fg=COR_TEXTO,
            bg=COR_FUNDO,
        ).pack(pady=(0, 10))

        tk.Label(
            self.container,
            text="Aplicado ao vocabulário de Ciência da Computação",
            font=("Segoe UI", 12, "italic"),
            fg="#94a3b8",
            bg=COR_FUNDO,
        ).pack(pady=(0, 40))

        tk.Label(
            self.container,
            text=f"{len(self.perguntas)} perguntas  •  Múltipla escolha  •  Feedback explicado",
            font=("Segoe UI", 11),
            fg="#94a3b8",
            bg=COR_FUNDO,
        ).pack(pady=(0, 30))

        btn = tk.Button(
            self.container,
            text="Começar Quiz",
            font=("Segoe UI", 14, "bold"),
            fg="white",
            bg=COR_DESTAQUE,
            activebackground="#0ea5e9",
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2",
            command=self.iniciar_quiz,
        )
        btn.pack()

    def iniciar_quiz(self):
        random.shuffle(self.perguntas)
        self.indice = 0
        self.pontos = 0
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        self.limpar_tela()
        self.respondeu = False

        pergunta = self.perguntas[self.indice]

        topo = tk.Frame(self.container, bg=COR_FUNDO)
        topo.pack(fill="x", padx=40, pady=(30, 10))

        tk.Label(
            topo,
            text=f"Pergunta {self.indice + 1} de {len(self.perguntas)}",
            font=("Segoe UI", 12, "bold"),
            fg=COR_DESTAQUE,
            bg=COR_FUNDO,
        ).pack(side="left")

        tk.Label(
            topo,
            text=f"Pontos: {self.pontos}",
            font=("Segoe UI", 12, "bold"),
            fg=COR_TEXTO,
            bg=COR_FUNDO,
        ).pack(side="right")

        barra = ttk.Progressbar(
            self.container,
            length=740,
            mode="determinate",
            maximum=len(self.perguntas),
            value=self.indice,
        )
        barra.pack(padx=40, pady=(0, 20))

        painel = tk.Frame(self.container, bg=COR_PAINEL, padx=30, pady=30)
        painel.pack(fill="both", expand=True, padx=40, pady=(0, 20))

        tk.Label(
            painel,
            text=pergunta["pergunta"],
            font=("Segoe UI", 15, "bold"),
            fg=COR_TEXTO,
            bg=COR_PAINEL,
            wraplength=700,
            justify="left",
        ).pack(anchor="w", pady=(0, 20))

        self.botoes_opcoes = []
        for i, opcao in enumerate(pergunta["opcoes"]):
            botao = tk.Button(
                painel,
                text=opcao,
                font=("Segoe UI", 12),
                fg=COR_TEXTO,
                bg=COR_BOTAO,
                activebackground=COR_BOTAO_HOVER,
                relief="flat",
                anchor="w",
                padx=20,
                pady=12,
                cursor="hand2",
                command=lambda i=i: self.responder(i),
            )
            botao.pack(fill="x", pady=6)
            self.botoes_opcoes.append(botao)

        self.label_feedback = tk.Label(
            self.container,
            text="",
            font=("Segoe UI", 11),
            fg=COR_TEXTO,
            bg=COR_FUNDO,
            wraplength=740,
            justify="left",
        )
        self.label_feedback.pack(padx=40, anchor="w")

        self.botao_avancar = tk.Button(
            self.container,
            text="Próxima →",
            font=("Segoe UI", 12, "bold"),
            fg="white",
            bg=COR_DESTAQUE,
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            state="disabled",
            command=self.avancar,
        )
        self.botao_avancar.pack(pady=(10, 0), anchor="e", padx=40)

    def responder(self, indice_escolhido):
        if self.respondeu:
            return
        self.respondeu = True

        pergunta = self.perguntas[self.indice]
        correta = pergunta["correta"]

        for i, botao in enumerate(self.botoes_opcoes):
            botao.configure(state="disabled")
            if i == correta:
                botao.configure(bg=COR_CERTO, fg="white")
            elif i == indice_escolhido:
                botao.configure(bg=COR_ERRADO, fg="white")

        if indice_escolhido == correta:
            self.pontos += 1
            prefixo = "✅ Correto!"
        else:
            prefixo = "❌ Incorreto."

        self.label_feedback.configure(text=f"{prefixo} {pergunta['explicacao']}")
        self.botao_avancar.configure(state="normal")

    def avancar(self):
        self.indice += 1
        if self.indice < len(self.perguntas):
            self.mostrar_pergunta()
        else:
            self.tela_resultado()

    def tela_resultado(self):
        self.limpar_tela()

        total = len(self.perguntas)
        percentual = round((self.pontos / total) * 100)

        if percentual >= 80:
            mensagem = "Excellent! You master Present tenses in tech English! 🚀"
        elif percentual >= 50:
            mensagem = "Good job! Keep practicing Simple Present and Present Continuous. 💪"
        else:
            mensagem = "Keep studying! Review the grammar rules and try again. 📚"

        tk.Label(
            self.container,
            text="Resultado Final",
            font=("Segoe UI", 26, "bold"),
            fg=COR_DESTAQUE,
            bg=COR_FUNDO,
        ).pack(pady=(70, 20))

        tk.Label(
            self.container,
            text=f"{self.pontos} / {total} acertos ({percentual}%)",
            font=("Segoe UI", 20, "bold"),
            fg=COR_TEXTO,
            bg=COR_FUNDO,
        ).pack(pady=(0, 15))

        tk.Label(
            self.container,
            text=mensagem,
            font=("Segoe UI", 13, "italic"),
            fg="#94a3b8",
            bg=COR_FUNDO,
            wraplength=600,
        ).pack(pady=(0, 40))

        botao_frame = tk.Frame(self.container, bg=COR_FUNDO)
        botao_frame.pack()

        tk.Button(
            botao_frame,
            text="Jogar de novo",
            font=("Segoe UI", 12, "bold"),
            fg="white",
            bg=COR_DESTAQUE,
            relief="flat",
            padx=25,
            pady=10,
            cursor="hand2",
            command=self.iniciar_quiz,
        ).pack(side="left", padx=10)

        tk.Button(
            botao_frame,
            text="Sair",
            font=("Segoe UI", 12, "bold"),
            fg=COR_TEXTO,
            bg=COR_BOTAO,
            relief="flat",
            padx=25,
            pady=10,
            cursor="hand2",
            command=self.root.destroy,
        ).pack(side="left", padx=10)


if __name__ == "__main__":
    janela = tk.Tk()
    app = QuizApp(janela)
    janela.mainloop()
