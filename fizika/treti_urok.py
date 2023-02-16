from tkinter import *
from tkinter import messagebox
from funkcii import *


def main3():
    window = Toplevel()
    window.title("Задача за Движение по окръжност")
    window.resizable(False, False)
    window.iconbitmap('./assets/science_tech_lightbulb_idea_research_icon_233294.ico')

    label = Label(window, text="Частица започва да се движи по окръжност с постоянно ъглово ускорение ε = 3rad/s^2", font="Bold")
    label.pack(anchor=CENTER)
    label1 = Label(window, text="Задача: Колко обиколки n на окръжността ще направи частицата за 4сек.?", font="Bold")
    label1.pack(anchor=CENTER)

    def hint():
        messagebox.showinfo("Подсказка", "Формула за решение: φ = ε * t^2 / 2")

    hint = Button(window, text="Подсказка", activebackground='#345', activeforeground='white', padx=5, pady=5,command=hint)
    hint.pack()

    otgovor1 = Button(window, text="3,8 обиколки", activebackground='#345',activeforeground='white', padx=5, pady=5, command=pravilno)
    otgovor1.pack()
    otgovor2 = Button(window, text="4 обиколки", activebackground='#345', activeforeground='white',padx=5, pady=5, command=greshno)
    otgovor2.pack()
    otgovor3 = Button(window, text="2 обиколки", activebackground='#345', activeforeground='white', padx=5, pady=5, command=greshno)
    otgovor3.pack()
    otgovor4 = Button(window, text="5 обиколки", activebackground='#345', activeforeground='white', padx=5, pady=5, command=greshno)
    otgovor4.pack()

    quit = Button(window, text="Назад", activebackground='#345', activeforeground='white', padx=5, pady=5, command=window.destroy)
    quit.pack(side=LEFT)

    window.mainloop()


if __name__ == '__main__':
    main3()
