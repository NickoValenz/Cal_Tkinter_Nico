import tkinter as tk

#muestreo de lo que se va ingresando a la entrada
def actualizar_entrada(valor):
    entrada.insert(tk.END, valor)

#validacion por si se pone algo no numerico o fallan las formulas
def evaluar():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "salio malo viejo")

#borra todo lo ingresado (vincular con el boton C despues pa que funke)
def limpiar():
    entrada.delete(0, tk.END)

#crear la ventana donde estaria todo
ventana = tk.Tk()
ventana.title("calcVario")

#espacio de la calculadora donde se van a mostrar los numeros ingresados
entrada = tk.Entry(ventana, width=16, font=("Trebuchet MS", 21), borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4)

#ponemos los botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

#con esto se ordenan los botones
for (texto, fila, columna) in botones:
    boton = tk.Button(ventana, text=texto, width=4, height=2, font=("Trebuchet MS", 15), command=lambda t=texto: actualizar_entrada(t))
    boton.grid(row=fila, column=columna)

#para sacar el resultado
boton_igual = tk.Button(ventana, text='=', width=4, height=2, font=("Trebuchet MS", 15), command=evaluar)
boton_igual.grid(row=4, column=3)

#el boton C para borrar todo lo puesto
boton_limpiar = tk.Button(ventana, text='C', width=4, height=2, font=("Trebuchet MS", 15), command=limpiar)
boton_limpiar.grid(row=5, column=0, columnspan=4, sticky='we')

#iniciar la app
ventana.mainloop()