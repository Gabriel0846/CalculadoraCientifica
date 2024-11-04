from gettext import textdomain
from idlelib.configdialog import font_sample_text
from tkinter import *
from tkinter import ttk
from tkinter import Label


from numpy.ma.extras import column_stack

cor1 = "#3b3b3b" # preta
cor2 = "#feffff" # branca
cor3 = "#37474F" # preta
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


# configurando frame tela
label_tela = Label(frame_tela, text='123456789', width=16, height=2,padx=7, anchor='e', bd=0, justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
label_tela.place(x=0, y=0)

# configurando flame cientifico
b_0 = Button(frame_cientifica,text='tan', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica,text='sin', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=0, y=0)
b_2 = Button(frame_cientifica,text='cos', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=0, y=0)
b_3 = Button(frame_cientifica,text='sqrt', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=0, y=0)

b_0 = Button(frame_cientifica,text='log', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica,text='log10', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=0, y=0)
b_2 = Button(frame_cientifica,text='e', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=0, y=0)
b_3 = Button(frame_cientifica,text='pow', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=0, y=0)

b_0 = Button(frame_cientifica,text='pi', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica,text=',', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=0, y=0)
b_2 = Button(frame_cientifica,text='(', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=0, y=0)
b_3 = Button(frame_cientifica,text=')', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=0, y=0)

b_0 = Button(frame_cientifica,text='C', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica,text='%', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=0, y=0)
b_2 = Button(frame_cientifica,text='/', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=0, y=0)
b_3 = Button(frame_cientifica,text='tan', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=0, y=0)

b_0 = Button(frame_cientifica,text='7', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica,text='8', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=0, y=0)
b_2 = Button(frame_cientifica,text='9', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=0, y=0)
b_3 = Button(frame_cientifica,text='*', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=0, y=0)

b_0 = Button(frame_cientifica,text='4', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica,text='5', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=0, y=0)
b_2 = Button(frame_cientifica,text='6', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=0, y=0)
b_3 = Button(frame_cientifica,text='-', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=0, y=0)

b_0 = Button(frame_cientifica,text='1', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica,text='2', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=0, y=0)
b_2 = Button(frame_cientifica,text='3', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=0, y=0)
b_3 = Button(frame_cientifica,text='+', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=0, y=0)

b_0 = Button(frame_cientifica,text='0', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica,text='.', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=0, y=0)
b_2 = Button(frame_cientifica,text='tan', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=0, y=0)
b_3 = Button(frame_cientifica,text='=', width=6, height=1,relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=0, y=0)


janela.mainloop()