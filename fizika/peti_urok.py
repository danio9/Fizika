from tkinter import *
from tkinter import messagebox
from funkcii import *


def main5():
    window = Toplevel()
    window.title("Задача за Импулс")
    window.resizable(False, False)
    window.iconbitmap('./assets/science_tech_lightbulb_idea_research_icon_233294.ico')

    label = Label(window, text="При изпълнение на сервис тенисист изпраща топка с тегло 60г. с начална скорост 30 m/s.", font="Bold")
    label.pack(anchor=CENTER)
    label1 = Label(window, text="Колко нютона е средната сила, с която ракетата действа на топката, ако продължителността на удара е 3ms?", font="Bold")
    label1.pack(anchor=CENTER)

    def hint():
        messagebox.showinfo("Подсказка", "Формула за решение: F = m * v^2 / t")

    hint = Button(window, text="Подсказка", activebackground='#345', activeforeground='white', padx=5, pady=5,command=hint)
    hint.pack()

    otgovor1 = Button(window, text="100N", activebackground='#345',activeforeground='white', padx=5, pady=5, command=greshno)
    otgovor1.pack()
    otgovor2 = Button(window, text="500N", activebackground='#345', activeforeground='white',padx=5, pady=5, command=greshno)
    otgovor2.pack()
    otgovor3 = Button(window, text="200N", activebackground='#345', activeforeground='white', padx=5, pady=5, command=greshno)
    otgovor3.pack()
    otgovor4 = Button(window, text="600N", activebackground='#345', activeforeground='white', padx=5, pady=5, command=pravilno)
    otgovor4.pack()

    quit = Button(window, text="Назад", activebackground='#345', activeforeground='white', padx=5, pady=5, command=window.destroy)
    quit.pack(side=LEFT)

    window.mainloop()


if __name__ == '__main__':
    main5()
