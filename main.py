from tkinter import *
from tkinter import ttk

from numpy.ma.extras import column_stack

cor1 = "#3b3b3b" # preta
cor2 = "#feffff" # branca
cor3 = "#424345" # preta
cor4 = "#eceff1" # cinza
cor5 = "#ffab40" # laranja

# janela principal
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x289")
janela.config(bg=cor1)

# criando frames
frame_tela = Frame(janela, width=300, height=56, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_cientifica = Frame(janela, width=300, height=86)
frame_cientifica.grid(row=1, column=0)

frame_corpo = Frame(janela, width=300, height=340)
frame_corpo.grid(row=2, column=0)

janela.mainloop()