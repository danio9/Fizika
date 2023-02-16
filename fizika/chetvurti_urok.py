from tkinter import *
from tkinter import messagebox
from funkcii import *


def main4():
    window = Toplevel()
    window.title("Задача за Принципите на механиката")
    window.resizable(False, False)
    window.iconbitmap('./assets/science_tech_lightbulb_idea_research_icon_233294.ico')

    label = Label(window, text="Тяло с тегло 2кг. се движи праволинейно по хоризонтална равнина под действието на сила 5N,", font="Bold")
    label.pack(anchor=CENTER)
    label1 = Label(window, text="която сключва ъгъл 30° с хоризонта. Ускорението на тялото е?", font="Bold")
    label1.pack(anchor=CENTER)

    def hint():
        messagebox.showinfo("Подсказка", "Формула за решение: a = F * cos α / m")

    hint = Button(window, text="Подсказка", activebackground='#345', activeforeground='white', padx=5, pady=5,command=hint)
    hint.pack()

    otgovor1 = Button(window, text="3 m/s^2", activebackground='#345',activeforeground='white', padx=5, pady=5, command=greshno)
    otgovor1.pack()
    otgovor2 = Button(window, text="1,5 m/s^2", activebackground='#345', activeforeground='white',padx=5, pady=5, command=greshno)
    otgovor2.pack()
    otgovor3 = Button(window, text="2 m/s^2", activebackground='#345', activeforeground='white', padx=5, pady=5, command=greshno)
    otgovor3.pack()
    otgovor4 = Button(window, text="2,2 m/s^2", activebackground='#345', activeforeground='white', padx=5, pady=5, command=pravilno)
    otgovor4.pack()

    quit = Button(window, text="Назад", activebackground='#345', activeforeground='white', padx=5, pady=5, command=window.destroy)
    quit.pack(side=LEFT)

    window.mainloop()


if __name__ == '__main__':
    main4()
