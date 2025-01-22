from tkinter import*
window=Tk()
window.geometry("400x300")
window.title("main")

def topwin():
    top=Toplevel()
    top.geometry("150x100")
    top.title("top window")

    label1=Label(top,text="Top window")
    label1.pack()

    top.mainloop()
label2=Label(window,text="main window")
label2.pack()
button=Button(window,text="clickhere", command=topwin)
button.pack()
window.mainloop()

