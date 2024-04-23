import tkinter as tk
import random

def seleccionar_casilla(color):
    if color == mensaje_color.get():
        mensaje.set("¡Correcto! Ha seleccionado la casilla " + color)
        if nivel_actual == 3:
            mensaje_felicidades.set("¡Felicidades! Has completado todas las pruebas.")
        else:
            mensaje_felicidades.set("Pasa a la siguiente prueba.")
        etiqueta.config(fg="green", font=("Helvetica", 12, "bold"), text=mensaje.get())
        if nivel_actual < 3:
            boton_siguiente.config(state=tk.NORMAL)
    else:
        mensaje.set("Incorrecto. Seleccione la casilla: " + mensaje_color.get())
        etiqueta.config(fg="red", font=("Helvetica", 12), text=mensaje.get())
        boton_siguiente.config(state=tk.DISABLED)

def pasar_siguiente_nivel():
    global nivel_actual
    nivel_actual += 1
    mensaje_felicidades.set("Pasa a la siguiente prueba.")
    mensaje.set("")  # Limpiar el mensaje anterior
    mensaje_prueba.set("")  # Limpiar la prueba anterior
    mensaje_color.set("")  # Limpiar el color anterior
    boton_siguiente.config(state=tk.DISABLED)  # Deshabilitar el botón de siguiente nivel
    crear_botones()

def reiniciar():
    global nivel_actual
    nivel_actual = 0
    mensaje_felicidades.set("")
    mensaje.set("")
    mensaje_prueba.set("")
    mensaje_color.set("")
    boton_siguiente.config(state=tk.DISABLED)  # Deshabilitar el botón de siguiente nivel
    crear_botones()

def crear_botones():
    global frame_botones, frame_color
    for widget in frame_botones.winfo_children():
        widget.destroy()
    for widget in frame_color.winfo_children():
        widget.destroy()

    if nivel_actual == 0:
        pasar_siguiente_nivel()
        return

    if nivel_actual == 1:
        mensaje_prueba.set("1. Selecciona la casilla del color: " + generar_color())
        mensaje.set("Seleccione la casilla: " + generar_color())
        mensaje_color.set(generar_color())
        color_palabra = generar_fuente()
        while color_palabra == mensaje_color.get():
            color_palabra = generar_fuente()
    elif nivel_actual == 2:
        mensaje_prueba.set("2. Seleccione la fuente del texto: " + generar_color())
        mensaje.set("Seleccione la fuente: " + generar_color())
        mensaje_color.set(generar_color())
        color_palabra = generar_color()
        while color_palabra == mensaje_color.get():
            color_palabra = generar_color()
    elif nivel_actual == 3:
        mensaje_prueba.set("3. Selecciona el nombre del color: " + generar_color())
        mensaje.set("Seleccione el nombre: " + generar_color())
        mensaje_color.set(generar_color())
        color_palabra = generar_nombre()
        while color_palabra == mensaje_color.get():
            color_palabra = generar_nombre()

    for _ in range(4):
        texto_boton = generar_nombre()
        color_fuente = generar_color()  # Color de fuente aleatorio
        boton = tk.Button(frame_botones, text=texto_boton, command=lambda c=texto_boton: seleccionar_casilla(c), width=10, height=3)
        boton.config(fg=color_fuente)  # Color de fuente aleatorio
        boton.pack(side=tk.LEFT, padx=10)

def generar_color():
    colores = ["red", "blue", "green", "yellow"]
    return random.choice(colores)

def generar_nombre():
    nombres = ["red", "blue", "green", "yellow"]
    return random.choice(nombres)

root = tk.Tk()
root.title("Pruebas de Colores y Textos")

nivel_actual = 0
mensaje_prueba = tk.StringVar()
mensaje_color = tk.StringVar()
mensaje = tk.StringVar()
mensaje_felicidades = tk.StringVar()

frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

frame_color = tk.Frame(root)
frame_color.pack(pady=5)

etiqueta_prueba = tk.Label(root, textvariable=mensaje_prueba, font=("Helvetica", 12))
etiqueta_prueba.pack(pady=10)

etiqueta = tk.Label(root, textvariable=mensaje, font=("Helvetica", 12))
etiqueta.pack()

etiqueta_felicidades = tk.Label(root, textvariable=mensaje_felicidades, font=("Helvetica", 12, "bold"), fg="green")
etiqueta_felicidades.pack(pady=10)

boton_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar)
boton_reiniciar.pack(pady=10)

boton_siguiente = tk.Button(root, text="Siguiente Nivel", command=pasar_siguiente_nivel, state=tk.DISABLED)
boton_siguiente.pack(pady=10)

crear_botones()

root.mainloop()

