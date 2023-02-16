from tkinter import *
from tkinter import messagebox
from funkcii import *
from PIL import ImageTk, Image

def main1():

    window = Toplevel()
    window.title("Сноп съчки")
    window.resizable(False, False)
    window.iconbitmap('./assets/science_tech_lightbulb_idea_research_icon_233294.ico')
    img = Image.open("./assets/zad1.png")
    photo = ImageTk.PhotoImage(img)
    labelimg = Label(window, image=photo)
    labelimg.pack()
    labelimg.image = photo

    label = Label(window, text="На всички ни е известна легендата за 7-те пръчки.", font="Bold")
    label.pack(anchor=CENTER)
    label1 = Label(window, text="Хан Кубрат за да убеди синовете си да живеят задружно, бащата предложил на синовете си да счупят сноп от 7 пръчки.", font="Bold")
    label1.pack(anchor=CENTER)
    label2 = Label(window, text=" Синовете се опитали, но безуспешно. Тогава бащата взел единия сноп, развързал го и лесно счупил всяка пръчка една по една. ", font="Bold")
    label2.pack(anchor=CENTER)
    label3 = Label(window, text="Задача: Колко пъти по-лесно е било на хан Кубрат да счупи пръчките една по една, отколкото на синовете му целия сноп?", font="Bold")
    label3.pack()
    label4 = Label(window, text="Дадено: Диаметърът на снопа е 3 пъти по-голям от диаметъра на отделната пръчка.", font="Bold")
    label4.pack()

    def hint():
        messagebox.showinfo("Подсказка", "Формула за решение: p = 1/12 * (P * l^3) / (п * k * (3*r)^4) ")

                  
    hint = Button(window, text="Подсказка", activebackground='#345', activeforeground='white', padx=5, pady=5, command=hint)
    hint.pack()
    
    otgovor1 = Button(window, text="80 пъти по-голяма сила е нужна.",activebackground='#345', activeforeground='white', padx=5, pady=5, command=pravilno)
    otgovor1.pack()
    otgovor2 = Button(window, text="7 пъти по-голяма сила е нужна.",activebackground='#345', activeforeground='white', padx=5, pady=5, command=greshno)
    otgovor2.pack()
    otgovor3 = Button(window, text="25 пъти по-голяма сила е нужна.",activebackground='#345', activeforeground='white', padx=5, pady=5, command=greshno)
    otgovor3.pack()
    otgovor4 = Button(window, text="70 пъти по-голяма сила е нужна.", activebackground='#345', activeforeground='white', padx=5, pady=5, command=greshno)
    otgovor4.pack()

    quit = Button(window, text="Назад", activebackground='#345', activeforeground='white', padx=5, pady=5, command=window.destroy)
    quit.pack(side=LEFT)


    window.mainloop()

if __name__ == '__main__':
    main1()
