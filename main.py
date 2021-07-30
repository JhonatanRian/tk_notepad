"""
    author: Jhonatan Rian
    Github: https://github.com/JhonatanRian
    
    - tk_notepad
    - Notepad with python and tkinter
"""

import tkinter
from tkinter.constants import LEFT

def new_file():
    """Creating new file"""
    text_area.delete(1.0, "end")

def save():
    """save files"""
    all_text = text_area.get(1.0, "end")
    with open("notepad.txt", "w") as file:
        file.write(all_text)
    
def Open():
    """open the created file"""
    with open("notepad.txt", "r") as file:
        all_text = file.read()
        text_area.insert(1.0, all_text)
        
def update_font():
    """updates font and size"""
    size = spin_caracter_size.get()
    font = spin_font.get()
    text_area.config(font="{} {}".format(font, size))


#  Creating window
window = tkinter.Tk()
window.title("Notepad") #  setting the window name
window.geometry("640x480")  #  setting size of window
window.minsize(width=640, height=480)  #  Setting minimum size

#  creating butons
frame = tkinter.Frame(window, height=30)
frame.pack(fill="x")

#  Creating label for text font
font_text = tkinter.Label(frame, text=" Font:  ")
font_text.pack(side=LEFT)
spin_font = tkinter.Spinbox(frame, values=("Arial", "Verdana", "Times", "Helvetica"))
spin_font.pack(side="left")

#  Creating label for font size
font_size = tkinter.Label(frame, text=" Size:  ")
font_size.pack(side=LEFT)
spin_caracter_size = tkinter.Spinbox(frame, from_=1, to=60)
spin_caracter_size.pack(side="left")

#  update font
button_update = tkinter.Button(frame, text="UP", command=update_font)
button_update.pack(side="left")

#  setting text area
text_area = tkinter.Text(window, font="Arial 15 bold", width=1280, height=720)
text_area.pack()

#  creating menu and commands
main_menu = tkinter.Menu(window)  #  creating menu
file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="open", command=Open)
file_menu.add_command(label="Exit", command=window.quit)
main_menu.add_cascade(label="File", menu=file_menu)
window.config(menu=main_menu)

window.mainloop()