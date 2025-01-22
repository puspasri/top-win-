from tkinter import*
from PIL import Image,ImageTk
window=Tk()
window.title("denomination calculator")
window.geometry("500x500")
window.configure(bg="green")
upload=Image.open("app_img_jpg")
upload.upload.resize(("200x200"))
image=ImageTk.PhotoImage(upload)

label=Label(window,image=Image)
label.place(x=160,z=30)
label1=Label(window,text="Denomination calculator")
label1.place(x=160,z=260,anchor=CENTER)
window.mainloop()