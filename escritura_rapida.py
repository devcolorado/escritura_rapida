# Los modulos que vamos a utilizar 
import tkinter as tk
import random
import time

def inicio():
 """Esta funcion arroja una frase aleatoria de la lista frases
 que despues es guardada en la variable frase y asu vez
 empieza a contabilizar el tiempo desde que es ejercutada"""
 frase.set(random.choice(frases))
 tiempo1.set(time.time())

def fin():
 """Esta funciona compruebra si la frase escrita es igual
 a la solicitada, y si este es el caso, imprime por pantalla
 cuando tiempo a trascurrido desde que inicio la prueba"""
 if frase.get() == frase_escrita.get() and frase.get():
  tiempo2 = time.time() 
  tiempo_final = str(tiempo2 - tiempo1.get())
  frase_escrita.set("")

  resultado = "Has tardado "+tiempo_final+" segundos"
  etiqueta2 = tk.Label(root,text=resultado)
  etiqueta2.place(x=130,y=300)
  etiqueta2.config(bg="gray5",font=("Normal 12"),fg="white")

# La ventana principal de la interfaz grafica
root = tk.Tk()
root.title("Prueba de escritura rapida")
root.geometry("600x400")
root.config(bd=20,bg="gray5")
root.resizable(0,0)

# Variables para almacenar los datos que usaremos en
# las diversas funciones del programa
frase = tk.StringVar()
frase_escrita = tk.StringVar()
tiempo1 = tk.DoubleVar()

# Lista de frases que se usaran para la prueba
frases = ["Que bellos arboles hay aqui","Que bien nada ese pez",
          "El gato se asusta facilmente"]

# Etiquetas con las indicaciones del la prueba
etiqueta1 = tk.Label(root,text="¡Bienvenido a la prueba de escritura rapida!")
etiqueta1.place(x=120,y=10)
etiqueta1.config(bg="gray5",font=("Normal 12"),fg="white")

etiqueta2 = tk.Label(root,
                      text="Pulsa el boton 'Iniciar' e intenta escribir la frase que aparezca \
                        \ntan rapido como puedas, cuando termines pulsa 'Terminar'.",
                      justify="left")
etiqueta2.place(x=80,y=30)
etiqueta2.config(bg="gray5",font=("Normal 12"),fg="white")

etiqueta3 = tk.Label(root,text="Escribe la frase de arriba:")
etiqueta3.place(x=190,y=150)
etiqueta3.config(bg="gray5",font=("Normal 12"),fg="white")

# Entrada para que el usuario vea una frase aleatoria de la lista frases
entrada1 = tk.Entry(root,bd=5,font="Normal 12",textvariable=frase,
                    width=22,bg="gray5",fg="white")
entrada1.place(x=170,y=100)

# Entrada para que el usuario escriba la frase 
entrada2 = tk.Entry(root,bd=5,font="Normal 12",textvariable=frase_escrita,
                    width=22,bg="gray5",fg="white")
entrada2.place(x=170,y=190)

# Boton para inciar la prueba
iniciar = tk.Button(root,text="Iniciar",font="Normal 10",bd=10,bg="gray5",
                   width=9,command=inicio,fg="white")
iniciar.place(x=170,y=240)

# Boton para terminar la prueba
terminar = tk.Button(root,text="Terminar",font="Normal 10",bd=10,bg="gray5",
                   width=9,command=fin,fg="white")
terminar.place(x=280,y=240)

# Iniciamos el bucle de eventos para que la ventana que se actualice mientras 
# El programa siga funcionando 
root.mainloop()