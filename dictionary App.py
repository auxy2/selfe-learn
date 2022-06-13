from tkinter import *
from tkinter import messagebox
from PyDictinary import PyDdictionary


dictionary = PyDictionary


root = Tk()

root.geometry('4000x4000')
root.configure(bg='black')
root.title('Akanni`s dictionary')



def dict():
    

    

    meaning.config(text = dictionary.meaning(word.get())['Noun'][0]) 
    synonym.config(text = dictionary.synonym(word.get()))
    antonym.config(text = dictionary.antonym(word.get()))
    




Label(root, text = "YOU ARE WELCME", font = ('Halvetica 40 bold'),bg = 'black', fg = 'blue').pack(pady=10)

frame1 = Frame(root)
Label(frame1, text = "Type Word:- ", font = ("castelar 25 bold"), bg = 'black',fg = 'white').pack(side = LEFT)
word = Entry(frame1, font = ("castellar 20 bold"))
word.pack()
frame1.pack(pady = 10)

frame2 = Frame(root)
Label(frame2, text = "Meaning:-  ", font = ("Halvetica 20 bold"),fg = 'white', bg = 'black').pack(side = LEFT)
meaning = Label(frame2, text = "", font = ("Halvetica 20 bold"),fg = 'red', bg = 'black')
meaning.pack()
frame2.pack(pady = 60)

frame3 = Frame(root)
Label(frame3, text = "synonym:- ", font = ("Halvetica 20 bold"),fg = 'white', bg = 'black').pack(side = LEFT)
synonym = Label(frame3, text = "", font = ("Halvetica 20 bold"), fg = 'yellow',bg = 'black')
synonym.pack()
frame3.pack(pady = 60)

frame4 = Frame(root)
Label(frame4, text = "antonym:- ", font = ("Halvetica 20 bold"), fg = 'white', bg = 'black').pack(side = LEFT)
antonym = Label(frame4, text = "" 
, font = ("halvetica 20 bold"),fg = 'green', bg = 'black')
antonym.pack()
frame4.pack(pady = 60)


submit_button = Button(root, text = "Search", font = ("comic sans", 20),command = dict, activeforeground='red',activebackground='black').place(x = 1000, y = 125)



Label(root, text= "LOOK FOR SOMETHING TO EAT ?", font = ("Allura 30 bold"),fg = 'gray', bg = 'black',).place(x= 15, y = 300)
Label(root, text= "We Are Here For You", font = ("Allura 20"),bg = 'black', fg = 'white',).place(x = 150, y = 350)

# Food = ["pizza","hotdog","buugger"]

# # radiobutton = Radiobutton(file = 'auxy.jpg')

# x = IntVar()
# for index in range(len(Food)):
#     radiobutton = Radiobutton(root,text= Food[index], variable=x,value=index,padx = 25, pady= 500)
#     # radiobutton.config()
#     # radiobutton.config()
#     # radiobutton.config()
#     radiobutton.pack(anchor=W)


root.mainloop()