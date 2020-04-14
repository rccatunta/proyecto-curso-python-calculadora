# Calculadora con Interfaz Grafica
import tkinter as tk

root = tk.Tk()
numero1 = tk.StringVar()
numero2 = tk.StringVar()
resultado = tk.StringVar()
numero1.set('0')
numero2.set('0')
resultado.set('0')


# FUNCIONES
def suma():
    a = float(numero1.get())
    b = float(numero2.get())
    res = a + b
    res = str(round(res, 2))
    resultado.set(res)


def resta():
    a = float(numero1.get())
    b = float(numero2.get())
    res = a - b
    res = str(round(res, 2))
    resultado.set(res)


def multiplicacion():
    a = float(numero1.get())
    b = float(numero2.get())
    res = a * b
    res = str(round(res, 2))
    resultado.set(res)


def division():
    a = float(numero1.get())
    b = float(numero2.get())
    res = a / b
    res = str(round(res, 2))
    resultado.set(res)


# MAIN PROGRAM
color_fondo = "#087f23"
root.geometry('500x350')
root.title('Calculadora Python')
root.configure(bg=color_fondo)

# Titulo
titulo = tk.Label(root, text="CALCULADORA", bg=color_fondo, fg='white', font=('Verdana', 32))
titulo.place(x=90, y=10)
# Numero1
label_numero_1 = tk.Label(root, text="Numero 1", bg=color_fondo, fg='white', font=('Verdana', 16))
label_numero_1.place(x=10, y=80)
entry_numero_1 = tk.Entry(root, justify='center', textvariable=numero1, font=('Verdana', 12))
entry_numero_1.place(x=10, y=120)

# Numero2
label_numero_2 = tk.Label(root, text="Numero 2", bg=color_fondo, fg='white', font=('Verdana', 16))
label_numero_2.place(x=10, y=160)
entry_numero_2 = tk.Entry(root, justify='center', textvariable=numero2, font=('Verdana', 12))
entry_numero_2.place(x=10, y=200)

# Resultado
label_resultado = tk.Label(root, text="Resultado", bg=color_fondo, fg='white', font=('Verdana', 16))
label_resultado.place(x=10, y=240)
entry_resultado = tk.Entry(root, justify='center', textvariable=resultado, font=('Verdana', 12))
entry_resultado.place(x=10, y=280)

# BotonSuma
boton_suma = tk.Button(root, command=suma, text='+', bd=0, bg='#80e27e', fg='black', font=('Verdana', 20), width=3)
boton_suma.place(x=300, y=130)

# BotonResta
boton_suma = tk.Button(root, command=resta, text='-', bd=0, bg='#80e27e', fg='black', font=('Verdana', 20), width=3)
boton_suma.place(x=370, y=130)

# BotonMultiplicacion
boton_multiplicacion = tk.Button(root, command=multiplicacion, text='*', bd=0, bg='#80e27e', fg='black',
                                 font=('Verdana', 20), width=3)
boton_multiplicacion.place(x=300, y=200)

# BotonDivision
boton_multiplicacion = tk.Button(root, command=division, text='/', bd=0, bg='#80e27e', fg='black', font=('Verdana', 20),
                                 width=3)
boton_multiplicacion.place(x=370, y=200)
root.mainloop()
