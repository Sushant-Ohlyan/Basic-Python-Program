import tkinter
window=tkinter.Tk()
window.title("Image Viewer")
icon=tkinter.PhotoImage(file="C:/Users/sushant/Pictures/send ashish sir.png")
label=tkinter.Label(window, image= icon)
label.pack()
window.mainloop()