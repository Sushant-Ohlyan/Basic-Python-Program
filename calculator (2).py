from tkinter import*
from tkinter.ttk import Button,Entry
root=Tk()
class main():
    def __init__(self,parent):
        self.parent=parent
        self.parent.title('Calculator')
        self.mText=StringVar()
        self.createWidgets()
    
    def createWidgets(self):
        Entry(self.parent,textvariable=self.mText,width=50).grid( columnspan=4)
        Button(self.parent,text='7',command=lambda:self.settext('7')).grid()
        Button(self.parent,text='4',command=lambda:self.settext('4')).grid()
        Button(self.parent,text='1',command=lambda:self.settext('1')).grid()
        Button(self.parent,text='0',command=lambda:self.settext('0')).grid()
        Button(self.parent,text='8',command=lambda:self.settext('8')).grid(row=1,column=1)
        Button(self.parent,text='5',command=lambda:self.settext('5')).grid(row=2,column=1)
        Button(self.parent,text='2',command=lambda:self.settext('2')).grid(row=3,column=1)
        Button(self.parent,text='.',command=lambda:self.settext('.')).grid(row=4,column=1)
        Button(self.parent,text='9',command=lambda:self.settext('9')).grid(row=1,column=2)
        Button(self.parent,text='6',command=lambda:self.settext('6')).grid(row=2,column=2)
        Button(self.parent,text='3',command=lambda:self.settext('3')).grid(row=3,column=2)
        Button(self.parent,text='=',command=self.calc).grid(row=4,column=2)
        Button(self.parent,text='+',command=lambda:self.settext('+')).grid(row=1,column=3)
        Button(self.parent,text='-',command=lambda:self.settext('-')).grid(row=2,column=3)
        Button(self.parent,text='*',command=lambda:self.settext('*')).grid(row=3,column=3)
        Button(self.parent,text='/',command=lambda:self.settext('/')).grid(row=4,column=3)
        Button(self.parent,text='AC',command=self.reset).grid(row=5,column=1)
        Button(self.parent,text='<--',command=self.delete).grid(row=5,column=2)
    def delete(self):
        self.mText.set(self.mText.get()[:-1])
    def reset(self):
        self.mText.set('')
    def settext(self,text):
        curtext=self.mText.get()
        if curtext=='error':
            self.mText.set(text)
        else:
            self.mText.set(curtext+text)
    def calc(self):
        try:
            self.mText.set(eval(self.mText.get()))
        except:
            self.mText.set('error')
if __name__ == "__main__":
    main(root)
    root.mainloop()