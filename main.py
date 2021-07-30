import tkinter

window = tkinter.Tk()
window.title("Notepad")
window.geometry("640x480")
window.minsize(width=640, height=480)
text_area = tkinter.Text(window, font="Arial 15 bold", width=1280, height=720)
text_area.pack()

main_menu = tkinter.Menu(window)

file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New", command=None)
file_menu.add_command(label="Save", command=None)
file_menu.add_command(label="Save as...", command=None)
file_menu.add_command(label="Exit", command=window.quit)

main_menu.add_cascade(label="File", menu=file_menu)

window.config(menu=main_menu)
window.mainloop()