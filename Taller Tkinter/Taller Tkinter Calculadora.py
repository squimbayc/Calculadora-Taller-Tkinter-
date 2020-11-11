import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import *
from math import floor
from tkinter.ttk import Progressbar

def init_window():
    window = tk.Tk()
    window.title('Mi primera aplicacion')
    window.geometry('400x300')
    window.configure(bg='mint cream')

    label = tk.Label(window, text='Calculadora', font=('Arial bold', 15),bg='mint cream')
    label.grid(column=0, row=1)

    global entrada1
    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    entrada1.grid(column=1, row=2)
    entrada2.grid(column=1, row=3)

    label_entrada1 = tk.Label(window, text='Ingrese primer numero:', font=('Arial bold', 10), bg='mint cream')
    label_entrada1.grid(column=0, row=2)

    label_entrada2 = tk.Label(window, text='Ingrese segundo numero:', font=('Arial bold', 10),bg='mint cream')
    label_entrada2.grid(column=0, row=3)

    ttk.Combobox

    label_operador = tk.Label(window, text='Escoja un operador', font=('Arial bold', 10),bg='mint cream')
    label_operador.grid(column=0, row=4)

    combo_operadores = ttk.Combobox(window)

    combo_operadores['values'] = ['+', '-', '*', '/', 'pow']

    combo_operadores.current(0)

    combo_operadores.grid(column=1, row=4)

    tk.Button

    label_resultado = tk.Label(window, text='Resultado: ', font=('Arial bold', 15),bg='mint cream')
    label_resultado.grid(column=0, row=6)

    def calculadora(num1, num2, operador):
        global resultado
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = round(num1 / num2, 2)
        else:
            resultado = num1 ** num2


        return resultado

    def click_calcular(label, num1, num2, operador):
        valor1 = float(num1)
        valor2 = float(num2)

        res = calculadora(valor1, valor2, operador)
        label.configure(text='Resultado: ' + str(res))

    boton = tk.Button(window,
                      command=lambda: click_calcular(
                          label_resultado,
                          entrada1.get(),
                          entrada2.get(),
                          combo_operadores.get()),
                      text='Calcular',
                      bg="dark turquoise",
                      fg='black')
    boton.grid(column=1, row=5)

    espacio1 = Label(window, text='                  ', bg='mint cream')
    espacio1.grid(row=8, column=0)

    Seguir_calculando = Button(window, text="Seguir calculando con el resultado", command=calcular_resultado, bg = 'gold')
    Seguir_calculando.grid(row=7,column=1)

    Fecha_hoy = Button(window, text="Saber la fecha actual", command=fecha_hoy, bg = 'plum1')
    Fecha_hoy.grid(row=9,column=1)

    style = ttk.Style()

    style.theme_use('default')

    style.configure("black.Horizontal.TProgressbar", background='black')

    bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

    bar['value'] = 50

    bar.grid(column=0, row=0)


    window.mainloop()

def calcular_resultado():
    window = tk.Tk()
    window.title('Mi primera aplicacion')
    window.geometry('400x300')
    window.configure(bg='mint cream')

    label = tk.Label(window, text='Calculadora', font=('Arial bold', 15),bg='mint cream')
    label.grid(column=0, row=1)


    entrada2 = tk.Entry(window, width=10)


    entrada2.grid(column=1, row=3)

    label_entrada1 = tk.Label(window, text='El numero guardado es :', font=('Arial bold', 10),bg='mint cream')
    label_entrada1.grid(column=0, row=2)

    label_entrada2 = tk.Label(window, text='Ingrese segundo numero:', font=('Arial bold', 10),bg='mint cream')
    label_entrada2.grid(column=0, row=3)

    label_resultado1 = tk.Label(window, text=resultado, font=('Arial bold', 10),bg='mint cream')
    label_resultado1.grid(column=1, row=2)

    resultado1 = resultado

    ttk.Combobox

    label_operador = tk.Label(window, text='Escoja un operador', font=('Arial bold', 10),bg='mint cream')
    label_operador.grid(column=0, row=4)

    combo_operadores = ttk.Combobox(window)

    combo_operadores['values'] = ['+', '-', '*', '/', 'pow']

    combo_operadores.current(0)

    combo_operadores.grid(column=1, row=4)

    tk.Button

    label_resultado = tk.Label(window, text='Resultado: ', font=('Arial bold', 15),bg='mint cream')
    label_resultado.grid(column=0, row=6)

    def calculadora(num1, num2, operador):
        global resultado
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = round(num1 / num2, 2)
        else:
            resultado = num1 ** num2

        return resultado

    def click_calcular(label, num1, num2, operador):
        valor1 = float(num1)
        valor2 = float(num2)

        res = calculadora(valor1, valor2, operador)
        label.configure(text='Resultado: ' + str(res))

    boton = tk.Button(window,
                      command=lambda: click_calcular(
                          label_resultado,
                          resultado1,
                          entrada2.get(),
                          combo_operadores.get()),
                      text='Calcular',
                      bg="dark turquoise",
                      fg='black')
    boton.grid(column=1, row=5)

    style = ttk.Style()

    style.theme_use('default')

    style.configure("black.Horizontal.TProgressbar", background='black')

    bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

    bar['value'] = 90

    bar.grid(column=0, row=0)


def fecha_hoy():
    messagebox.showinfo ('Fecha y hora',datetime.now())

init_window()