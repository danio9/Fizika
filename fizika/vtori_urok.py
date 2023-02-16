from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from funkcii import *

def main2():
   window = Toplevel()
   window.title("Задача за Центростремителна сила")
   window.resizable(False, False)
   window.iconbitmap('./assets/science_tech_lightbulb_idea_research_icon_233294.ico')

   label = Label(window, text="Момиче с тегло 50кг. се вози на влакче в увеселителен парк.", font="Bold")
   label.pack(anchor=CENTER)
   label1 = Label(window, text="Пресметнете центростремителната сила, която действа на момичето в момента, когато влакчето се движи със 72км/ч", font="Bold")
   label1.pack(anchor=CENTER)
   label2 = Label(window, text=" по дъга на окръжност с радиус 20 метра.", font="Bold")
   label2.pack(anchor=CENTER)

   def hint():
      messagebox.showinfo("Подсказка", "Формула за решение: F = m * v^2 / r ")

   hint = Button(window, text="Подсказка", activebackground='#345', activeforeground='white', padx=5, pady=5,command=hint)
   hint.pack()

   otgovor1 = Button(window, text="100N", activebackground='#345', activeforeground='white', padx=5, pady=5, command=greshno)
   otgovor1.pack()
   otgovor2 = Button(window, text="250N", activebackground='#345', activeforeground='white', padx=5, pady=5, command=greshno)
   otgovor2.pack()
   otgovor3 = Button(window, text="1000N", activebackground='#345', activeforeground='white', padx=5, pady=5, command=pravilno)
   otgovor3.pack()
   otgovor4 = Button(window, text="500N", activebackground='#345', activeforeground='white', padx=5, pady=5, command=greshno)
   otgovor4.pack()

   quit = Button(window, text="Назад", activebackground='#345', activeforeground='white', padx=5, pady=5, command=window.destroy)
   quit.pack(side=LEFT)
   
   window.mainloop()

if __name__ == '__main__':
    main2()




