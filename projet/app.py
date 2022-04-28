from tkinter import *
from typing import List 
from container import Container

container = Container()
anna = container.anna()

window = Tk()

# Adding label
label = Label(window, text='Super search!')
label.pack()

# Adding input
value = StringVar()
value.set('What are you looking for?')
entree = Entry(window, textvariable=value)
entree.pack()

# Adding search button
def search():
    global result_list
    result_list.delete(0, END)
    search_text: str = entree.get()
    results: List[str] = anna.search(search_text)
    for index, result in enumerate(results):
        result_list.insert(index +1, result)

button = Button(window,text="Rechercher", command=search)
button.pack()

# Adding result list
result_list = Listbox(window)
result_list.pack()

window.mainloop()