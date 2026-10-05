import tkinter as tk
from pathlib import Path
from tkinter import ttk


class LoginView(tk.Frame):
    def __init__(self, master, restaurante_servicio, al_iniciar_sesion):
        super().__init__(master, bg="#eef3f8")

        self.restaurante_servicio = restaurante_servicio
        self.al_iniciar_sesion = al_iniciar_sesion

        self.usuario_entry = None
        self.contrasena_entry = None
        self.mensaje_error = None
        self.logo = None

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Login.TButton",
            background="#2563eb",
            foreground="#ffffff",
            font=("Arial", 11, "bold"),
            padding=(14, 10),
            borderwidth=0,
        )
        estilo.map(
            "Login.TButton",
            background=[("active", "#1d4ed8")],
            foreground=[("active", "#ffffff")],
        )

    def cargar_logo(self):
        ruta_base = Path(__file__).resolve().parent.parent
        ruta_logo = ruta_base / "assets" / "icons" / "logo.png"

        if not ruta_logo.exists():
            return None

        logo_original = tk.PhotoImage(file=str(ruta_logo))
        self.logo = logo_original.subsample(7, 7)
        return self.logo

    def construir_interfaz(self):
        contenedor = tk.Frame(self, bg="#ffffff", padx=32, pady=30, highlightthickness=1, highlightbackground="#dfe7f1")
        contenedor.place(relx=0.5, rely=0.5, anchor="center")

        logo = self.cargar_logo()
        if logo is not None:
            tk.Label(contenedor, image=logo, bg="#ffffff").pack(pady=(0, 12))
        else:
            marco_logo = tk.Label(
                contenedor,
                text="Castillo\nRestaurant",
                bg="#dbeafe",
                fg="#1d4ed8",
                font=("Arial", 15, "bold"),
                justify="center",
                padx=18,
                pady=10,
                borderwidth=1,
                relief="solid",
            )
            marco_logo.pack(pady=(0, 12))

        titulo = tk.Label(
            contenedor,
            text="Castillo Restaurant",
            bg="#ffffff",
            fg="#1f2a44",
            font=("Arial", 24, "bold"),
        )
        titulo.pack(pady=(0, 6))

        subtitulo = tk.Label(
            contenedor,
            text="Inicio de sesión",
            bg="#ffffff",
            fg="#516173",
            font=("Arial", 11),
        )
        subtitulo.pack(pady=(0, 18))

        tk.Label(
            contenedor,
            text="Usuario",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")

        self.usuario_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11),
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#cbd5e1",
        )
        self.usuario_entry.pack(pady=(4, 12), ipady=5)
        self.usuario_entry.focus()

        tk.Label(
            contenedor,
            text="Contraseña",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w")

        self.contrasena_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11),
            show="*",
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#cbd5e1",
        )
        self.contrasena_entry.pack(pady=(4, 12), ipady=5)

        self.usuario_entry.bind("<Return>", lambda event: self.iniciar_sesion())
        self.contrasena_entry.bind("<Return>", lambda event: self.iniciar_sesion())

        self.mensaje_error = tk.Label(
            contenedor,
            text="",
            bg="#ffffff",
            fg="#b42318",
            font=("Arial", 10),
        )
        self.mensaje_error.pack(pady=(0, 14))

        boton = ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion,
            style="Login.TButton",
        )
        boton.pack(fill="x")

    def iniciar_sesion(self):
        # Obtiene los valores escritos y solicita la validación al servicio
        assert self.usuario_entry is not None
        assert self.contrasena_entry is not None
        assert self.mensaje_error is not None

        usuario = self.usuario_entry.get().strip()
        contrasena = self.contrasena_entry.get().strip()

        if not usuario or not contrasena:
            self.mensaje_error.config(text="Ingrese usuario y contrasena.")
            return

        usuario_validado = self.restaurante_servicio.validar_acceso(usuario, contrasena)

        if usuario_validado is None:
            self.mensaje_error.config(text="Credenciales incorrectas.")
            self.contrasena_entry.delete(0, tk.END)
            return

        self.mensaje_error.config(text="")
        self.al_iniciar_sesion(usuario_validado)