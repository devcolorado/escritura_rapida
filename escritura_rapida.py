import tkinter as tk
import random
import time

def inicio():
 frase.set(random.choice(frases))
 tiempo1.set(time.time())

def fin():
 if frase.get() == frase_escrita.get() and frase.get():
  tiempo2 = time.time() 
  tiempo_final = str(tiempo2 - tiempo1.get())

  resultado = "Has tardado "+tiempo_final+" segundos"
  etiqueta2 = tk.Label(root,text=resultado)
  etiqueta2.place(x=130,y=230)
  etiqueta2.config(bg="gray63",font=("Normal 12"))


root = tk.Tk()
root.title("Prueba de escritura rapida")
root.geometry("600x400")
root.config(bd=20,bg="gray63")
root.resizable(0,0)

frase = tk.StringVar()
frase_escrita = tk.StringVar()
tiempo1 = tk.DoubleVar()


frases = ["Que bellos arboles hay aqui","Que bien nada ese pez",
          "El gato se asusta facilmente"]



etiqueta1 = tk.Label(root,text="Escribe la frase de arriba:")
etiqueta1.place(x=190,y=80)
etiqueta1.config(bg="gray63",font=("Normal 12"))

entrada1 = tk.Entry(root,bd=5,font="Normal 12",textvariable=frase,
                    width=22,state="readonly")
entrada1.place(x=170,y=20)

entrada2 = tk.Entry(root,bd=5,font="Normal 12",textvariable=frase_escrita,width=22)
entrada2.place(x=170,y=120)

iniciar = tk.Button(root,text="Iniciar",font="Normal 10",bd=10,bg="gray63",
                   width=9,command=inicio)
iniciar.place(x=170,y=160)

terminar = tk.Button(root,text="Terminar",font="Normal 10",bd=10,bg="gray63",
                   width=9,command=fin)
terminar.place(x=280,y=160)







root.mainloop()