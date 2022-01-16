import tkinter as tk
from tkinter import filedialog,Text
import os

root=tk.Tk()
root.title("Sudden app starter")
apps=[]

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps=f.read()
        tempApps=tempApps.split(',')
        apps=[x for x in tempApps if x.strip()]
def addAPP():
    for widget in frame.winfo_children():
        widget.destroy()
    filename=filedialog.askopenfilename(initialdir="/",title="select File",filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:    
        label=tk.Label(frame,text=app,bg="grey")
        label.pack()

def runAPPs():
    for app in apps:
        os.startfile(app)

canvas= tk.Canvas(root, height=600, width=600,bg="#263d42")
canvas.pack()

frame=tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

openfile=tk.Button(root,text="open file",padx=10,pady=5,fg="white",bg="#263d42",command=addAPP)
openfile.pack()
runAPPs=tk.Button(root,text="runAPP",padx=10,pady=5,fg="white",bg="#263d42",command=runAPPs)
runAPPs.pack()

for app in apps:
    label=tk.Label(frame,text=app)
    label.pack()

root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app+',')