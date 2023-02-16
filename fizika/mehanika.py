from tkinter import *
from purvi_urok import main1
from vtori_urok import main2
from treti_urok import main3
from chetvurti_urok import main4
from peti_urok import main5

window = Tk()
window.title("Меню ПАРАДОКСИ")
window.resizable(False, False)
window.geometry("700x300")
window.iconbitmap('./assets/science_tech_lightbulb_idea_research_icon_233294.ico')

options = ["Изберете",
           "Задача за Сноп Съчки",
           "Задача за Центростремителна сила",
           "Задача за Движение по окръжност",
           "Задача за Принципите на механиката",
           "Задача за Импулс"]
default = StringVar(window)
default.set("Изберете")
menu = OptionMenu(window, default, *options)
menu.pack()

def purvi():
    main1()
def vtori():
    main2()
def treti():
    main3()
def chertvurti():
    main4()
def peti():
    main5()

def pusni():
    if default.get() == "Задача за Сноп Съчки":
        purvi()
    elif default.get() == "Задача за Центростремителна сила":
        vtori()
    elif default.get() == "Задача за Движение по окръжност":
        treti()
    elif default.get() == "Задача за Принципите на механиката":
        chertvurti()
    elif default.get() == "Задача за Импулс":
        peti()

button = Button(window, text="Пусни", command=pusni)
button.pack()


window.mainloop()
