#  Kонвертер валют.

from tkinter import *
from tkinter import ttk


converter = Tk()
converter.title('Конвентер валют')
converter.geometry("600x450")

OPTIONS = {
    'USD': 60.2370,
    'EUR': 60.2842,
    'GBP': 70.1038,
    'TRY': 3.3121,
    'BYN': 23.6066,
    'SGD': 42.9926,
}


def ok():
    price = rub.get()
    answer = variable1.get()
    DICT = OPTIONS.get(answer, None)
    converted = float(DICT)*float(price)
    result.delete(1.0, END)
    result.insert(INSERT, 'Рублей в ', INSERT, answer,
                  INSERT, ' = ', INSERT, converted)


appName = Label(converter, text='Конвертер валют', font=('arial', 25, 'bold', 'underline'),
                fg='red3')
appName.place(x=150, y=10)

result = Text(converter, height=5, width=50, font=('arial', 10, 'bold'), bd=5)
result.place(x=125, y=60)

r = Label(converter, text='Количество рублей:',
          font=('arial', 12, 'bold'), fg='dark red')
r.place(x=30, y=165)

rub = Entry(converter, font=('arial', 20))
rub.place(x=200, y=160)

choice = Label(converter, text="Валюта:", font=(
    'arial', 12, 'bold'), fg='dark red')
choice.place(x=30, y=220)

variable1 = StringVar(converter)
variable1.set(None)
option = OptionMenu(converter, variable1, *OPTIONS)
option.place(x=100, y=210, width=100, height=40)

button = Button(converter, text='Конвертация', fg='green',
                font=('arial', 15), bg='powder blue', command=ok)
button.place(x=200, y=210, height=40, width=150)


converter.mainloop()
