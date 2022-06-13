from tkinter import *




def submit():
  food =  []
  for index in listbox.curselection():
        food.insert(index,listbox.get(index))
        for index in food:
            print("HELLO!")
            print("You have orderd "+ index)

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

root = Tk()

listbox = Listbox(root,bg='gray',font=("comicssans 40"),width=12,selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pastta")
listbox.insert(3,"garlic")
listbox.insert(4,"Bread&beans")

listbox.config(height=listbox.size())

entrybox = Entry(root,)
entrybox.pack()

addbutton = Button(root,text="Add",command=add)
addbutton.pack()


submitButton = Button(root,text="submit",command=submit)
submitButton.pack()

deletebutton = Button(root,text="del",command=delete)
deletebutton.pack()

root.mainloop()