import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Lista de usuarios considerados peligrosos o genéricos
usuarios_sospechosos = ['admin', 'root', 'test', '123', 'user', 'default']

def verificar_usuario(usuario):
    usuario = usuario.lower()
    for sospechoso in usuarios_sospechosos:
        if sospechoso in usuario:
            return True
    return False

def iniciar_sesion():
    usuario = entry_usuario.get()
    clave = entry_clave.get()

    if not usuario or not clave:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return

    if verificar_usuario(usuario):
        messagebox.showerror("Acceso denegado", "Nombre de usuario potencialmente inseguro.")
        return

    # Aquí iría la lógica de acceso real
    messagebox.showinfo("Bienvenido", f"Acceso concedido a {usuario}")

# --- INTERFAZ ---

root = tk.Tk()
root.title("Advanced Smart Logistics - Login")
root.geometry("450x400")
root.configure(bg="#0d1b2a")

# Logo (opcional: usa tu propia imagen con temática de inventario o logística)
try:
    logo_img = Image.open("logo-inventario.png")  # Cambia por la ruta de tu logo
    logo_img = logo_img.resize((100, 100))
    logo = ImageTk.PhotoImage(logo_img)
    lbl_logo = tk.Label(root, image=logo, bg="#0d1b2a")
    lbl_logo.pack(pady=10)
except:
    lbl_logo = tk.Label(root, text="📦", font=("Arial", 40), bg="#0d1b2a", fg="white")
    lbl_logo.pack(pady=10)

# Título
titulo = tk.Label(root, text="Advanced Smart Logistics", font=("Segoe UI", 16, "bold"), fg="#ffffff", bg="#0d1b2a")
titulo.pack(pady=10)

# Usuario
lbl_usuario = tk.Label(root, text="Usuario:", fg="#ffffff", bg="#0d1b2a")
lbl_usuario.pack()
entry_usuario = tk.Entry(root, font=("Segoe UI", 12), width=30)
entry_usuario.pack(pady=5)

# Contraseña
lbl_clave = tk.Label(root, text="Contraseña:", fg="#ffffff", bg="#0d1b2a")
lbl_clave.pack()
entry_clave = tk.Entry(root, font=("Segoe UI", 12), show="*", width=30)
entry_clave.pack(pady=5)

# Botón de acceso
btn_login = tk.Button(root, text="Iniciar Sesión", font=("Segoe UI", 12, "bold"), bg="#1b263b", fg="white", width=20, command=iniciar_sesion)
btn_login.pack(pady=20)

# Pie
lbl_footer = tk.Label(root, text="© 2025 Advanced Smart Logistics", fg="#7f8fa6", bg="#0d1b2a", font=("Segoe UI", 8))
lbl_footer.pack(side="bottom", pady=10)

root.mainloop()