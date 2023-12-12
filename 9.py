from tkinter import *

def send():
    user_input = e.get()
    text.insert(END, "\nYou: " + user_input)
    if user_input == 'hi':
        text.insert(END, "\nBot: hello")
    elif user_input == 'hello':
        text.insert(END, "\nBot: hi")
    elif user_input == 'how are you?':
        text.insert(END, "\nBot: i'm fine and you?")
    elif user_input == "i'm fine too":
        text.insert(END, "\nBot: nice to hear that")
    else:
        text.insert(END, "\nBot: Sorry I didn't get it.")

root = Tk()
root.title('IT SOURCCODE SIMPLE CHATBOT')

text = Text(root, bg='light blue')
text.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=80)
e.grid(row=1, column=0)

send_button = Button(root, text='Send', bg='blue', width=20, command=send)
send_button.grid(row=1, column=1)

root.mainloop()
