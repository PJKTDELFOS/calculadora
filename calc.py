import math
import tkinter as tk
from tkinter import messagebox


def calc_soma():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        resultado = calculadora_soma(x, y)
        result_var.set(f'Resultado{resultado}')
    except ValueError:
        messagebox.showerror("Erro", 'Insira valores numéricos válidos')


def calc_sub():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        resultado = calculadora_sub(x, y)
        result_var.set(f'Resultado{resultado}')
    except ValueError:
        messagebox.showerror("Erro", 'Insira valores numéricos válidos')


def calc_mult():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        resultado = calculadora_mult(x, y)
        result_var.set(f'Resultado{resultado}')
    except ValueError:
        messagebox.showerror("Erro", 'Insira valores numéricos válidos')


def calc_div():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        resultado = calculadora_div(x, y)
        result_var.set(f'Resultado{resultado}')
    except ZeroDivisionError:
        messagebox.showerror('Erro', 'Divisao por zero nao permitida')
    except ValueError:
        messagebox.showerror("Erro", 'Insira valores numéricos válidos')


def calc_exp():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        resultado = calculadora_exp(x, y)
        result_var.set(f'Resultado{resultado}')
    except ValueError:
        messagebox.showerror("Erro", 'Insira valores numéricos válidos')


def calc_raiz():
    try:
        x = float(entry1.get())
        resultado = raiz(x, )
        result_var.set(f'Resultado{resultado}')
    except ValueError:
        messagebox.showerror("Erro", 'Insira valores numéricos válidos')


def calc_baskara():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())
        resultado = bhaskara(a, b, c)
        if resultado:
            x1, x2 = resultado
            result_var.set(f"x1: {x1}, x2: {x2}")
        else:
            result_var.set('Delta Menor que zero, sem raizes Reais')
    except ValueError:
        messagebox.showerror('"Erro", "Insira valores numéricos válidos')


def calculadora_mult(x, y):
    resultado = x * y
    return resultado


def calculadora_soma(x, y):
    resultado = x + y
    return resultado


def calculadora_sub(x, y):
    resultado = x - y
    return resultado


def calculadora_div(x, y):
    if y == 0:
        raise ZeroDivisionError('Divisao por zero nao permitida')
    else:
        resultado = x / y
    return resultado


def calculadora_exp(x, y):
    resultado = x ** y
    return resultado


def raiz(x):
    resultado = math.sqrt(x)
    return resultado


def delta(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    return delta


def bhaskara(a, b, c):
    if a == 0:
        raise ValueError("O coeficiente 'a' não pode ser zero na fórmula de Bhaskara")
    d = delta(a, b, c)
    if d < 0:
        print('delta menor que zero ')
        return None
    else:
        x1 = ((-b) + math.sqrt(d)) / (2 * a)
        x2 = ((-b) - math.sqrt(d)) / (2 * a)
        return x1, x2


root = tk.Tk()
root.title('calculadora')

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

tk.Label(root, text='Valor 1').grid(row=0, column=0)
tk.Label(root, text='Valor 2').grid(row=1, column=0)
tk.Label(root, text='Coef. C (para Bhaskara)').grid(row=2, column=0)

tk.Button(root, text="Soma", command=calc_soma).grid(row=3, column=0)
tk.Button(root, text="Subtração", command=calc_sub).grid(row=3, column=1)
tk.Button(root, text="Multiplicação", command=calc_mult).grid(row=4, column=0)
tk.Button(root, text="Divisão", command=calc_div).grid(row=4, column=1)
tk.Button(root, text="Exponenciação", command=calc_exp).grid(row=5, column=0)
tk.Button(root, text="Raiz Quadrada", command=calc_raiz).grid(row=5, column=0)
tk.Button(root, text="Bhaskara", command=calc_baskara).grid(row=5, column=1)

result_var = tk.StringVar()
result_var.set('resultado')
tk.Label(root, textvariable=result_var).grid(row=6, column=0, columnspan=2)

root.mainloop()
