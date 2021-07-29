import tkinter

window = tkinter.Tk()
window.title("Notepad")
window.geometry("640x480")
window.minsize(width=640, height=480)
text_area = tkinter.Text(window, font="Arial 15 bold")
text_area.pack()
window.mainloop()