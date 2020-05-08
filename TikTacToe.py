from tkinter import *
from tkinter import messagebox

wn = Tk()
wn.config (background='Light grey')
wn.geometry('280x280')

var1=StringVar()
var=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()

var.set('  x')
var1.set(' ')
var2.set(' ')
var3.set(' ')
var4.set(' ')
var5.set(' ')
var6.set(' ')
var7.set(' ')
var8.set(' ')
var9.set(' ')


 


def game ():

     wn2=Toplevel
     wn2=Toplevel(wn)
     wn2.geometry('280x280')
     wn2.configure(background='light grey')

     def OnButtonClick (Buttonid):
        if (Buttonid==1 and var.get()=='  x'):
            var1.set('x')
            var.set('  o')
            Label(wn2,textvariable=var1).place(x=130,y=100,width=30,height=30)
        elif (Buttonid==1 and var.get()=='  o'):
            var1.set('o')
            var.set('  x')
            Label(wn2,textvariable=var1).place(x=130,y=100,width=30,height=30)


        if (Buttonid==2 and var.get()=='  x'):
            var2.set('x')
            var.set('  o')
            Label(wn2,textvariable=var2).place(x=160,y=100,width=30,height=30)
        elif (Buttonid==2 and var.get()=='  o'):
            var2.set('o')
            var.set('  x')
            Label(wn2,textvariable=var2).place(x=160,y=100,width=30,height=30)

        if (Buttonid==3 and var.get()=='  x'):
            var3.set('x')
            var.set('  o')
            Label(wn2,textvariable=var3).place(x=100,y=100,width=30,height=30)
        elif (Buttonid==3 and var.get()=='  o'):
            var3.set('o')
            var.set('  x')
            Label(wn2,textvariable=var3).place(x=100,y=100,width=30,height=30)


        if (Buttonid==4 and var.get()=='  x'):
            var4.set('x')
            var.set('  o')
            Label(wn2,textvariable=var4).place(x=130,y=70,width=30,height=30)
        elif (Buttonid==4 and var.get()=='  o'):
            var4.set('o')
            var.set('  x')
            Label(wn2,textvariable=var4).place(x=130,y=70,width=30,height=30)


        if (Buttonid==5 and var.get()=='  x'):
            var5.set('x')
            var.set('  o')
            Label(wn2,textvariable=var5).place(x=160,y=70,width=30,height=30)
        elif (Buttonid==5 and var.get()=='  o'):
            var5.set('o')
            var.set('  x')
            Label(wn2,textvariable=var5).place(x=160,y=70,width=30,height=30)


        if (Buttonid==6 and var.get()=='  x'):
            var6.set('x')
            var.set('  o')
            Label(wn2,textvariable=var6).place(x=100,y=70,width=30,height=30)
        elif (Buttonid==6 and var.get()=='  o'):
            var6.set('o')
            var.set('  x')
            Label(wn2,textvariable=var6).place(x=100,y=70,width=30,height=30)


        if (Buttonid==7 and var.get()=='  x'):
            var7.set('x')
            var.set('  o')
            Label(wn2,textvariable=var7).place(x=130,y=40,width=30,height=30)
        elif (Buttonid==7 and var.get()=='  o'):
            var7.set('o')
            var.set('  x')
            Label(wn2,textvariable=var7).place(x=130,y=40,width=30,height=30)


        if (Buttonid==8 and var.get()=='  x'):
            var8.set('x')
            var.set('  o')
            Label(wn2,textvariable=var8).place(x=160,y=40,width=30,height=30)
        elif (Buttonid==8 and var.get()=='  o'):
            var8.set('o')
            var.set('  x')
            Label(wn2,textvariable=var8).place(x=160,y=40,width=30,height=30)


        if (Buttonid==9 and var.get()=='  x'):
            var9.set('x')
            var.set('  o')
            Label(wn2,textvariable=var9).place(x=100,y=40,width=30,height=30)
        elif (Buttonid==9 and var.get()=='  o'):
            var9.set('o')
            var.set('  x')
            Label(wn2,textvariable=var9).place(x=100,y=40,width=30,height=30)

        if (var1.get()=='x' and var2.get()=='x' and var3.get()=='x'):
             messagebox.showinfo('Success','player x won')
             var.set('  x')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             


        if (var1.get()=='o' and var2.get()=='o' and var3.get()=='o'):
             messagebox.showinfo('Success','player o won')
             var.set('  o')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var6.get()=='x' and var4.get()=='x' and var5.get()=='x'):
             messagebox.showinfo('Success','player x won')
             var.set('  x')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var6.get()=='o' and var4.get()=='o' and var5.get()=='o'):
             messagebox.showinfo('Success','player o won')
             var.set('  o')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var9.get()=='x' and var7.get()=='x' and var8.get()=='x'):
             messagebox.showinfo('Success','player x won')
             var.set('  x')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var9.get()=='o' and var7.get()=='o' and var8.get()=='o'):
             messagebox.showinfo('Success','player o won')
             var.set('  o')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var9.get()=='x' and var6.get()=='x' and var3.get()=='x'):
             messagebox.showinfo('Success','player x won')
             var.set('  x')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)


        
             

        if (var9.get()=='o' and var6.get()=='o' and var3.get()=='o'):
             messagebox.showinfo('Success','player o won')
             var.set('  o')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var7.get()=='x' and var4.get()=='x' and var1.get()=='x'):
             messagebox.showinfo('Success','player x won')
             var.set('  x')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var7.get()=='o' and var4.get()=='o' and var1.get()=='o'):
             messagebox.showinfo('Success','player o won')
             var.set('  o')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var8.get()=='x' and var5.get()=='x' and var2.get()=='x'):
             messagebox.showinfo('Success','player x won')
             var.set('  x')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var8.get()=='o' and var5.get()=='o' and var2.get()=='o'):
             messagebox.showinfo('Success','player o won')
             var.set('  o')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             
             
        if (var8.get()=='x' and var4.get()=='x' and var3.get()=='x'):
             messagebox.showinfo('Success','player x won')
             var.set('  x')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var8.get()=='o' and var4.get()=='o' and var3.get()=='o'):
             messagebox.showinfo('Success','player o won')
             var.set('  o')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var9.get()=='x' and var4.get()=='x' and var2.get()=='x'):
             messagebox.showinfo('Success','player x won')
             var.set('  x')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

        
             

        if (var9.get()=='o' and var4.get()=='o' and var2.get()=='o'):
             messagebox.showinfo('Success','player o won')
             var.set('  o')
             var1.set(' ')
             var2.set(' ')
             var3.set(' ')
             var4.set(' ')
             var5.set(' ')
             var6.set(' ')
             var7.set(' ')
             var8.set(' ')
             var9.set(' ')
             Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
             Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
             Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
             Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
             Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
             Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
             Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
             Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
             Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

     Entry(wn2,textvariable=var,font='Helvetica 10 bold').place(x=130,y=10,width=30,height=30)

     Button(wn2,textvariable=var1,command=lambda:OnButtonClick(1)).place(x=130,y=100,width=30,height=30)
     Button(wn2,textvariable=var2,command=lambda:OnButtonClick(2)).place(x=160,y=100,width=30,height=30)
     Button(wn2,textvariable=var3,command=lambda:OnButtonClick(3)).place(x=100,y=100,width=30,height=30)
     Button(wn2,textvariable=var4,command=lambda:OnButtonClick(4)).place(x=130,y=70,width=30,height=30)
     Button(wn2,textvariable=var5,command=lambda:OnButtonClick(5)).place(x=160,y=70,width=30,height=30)
     Button(wn2,textvariable=var6,command=lambda:OnButtonClick(6)).place(x=100,y=70,width=30,height=30)
     Button(wn2,textvariable=var7,command=lambda:OnButtonClick(7)).place(x=130,y=40,width=30,height=30)
     Button(wn2,textvariable=var8,command=lambda:OnButtonClick(8)).place(x=160,y=40,width=30,height=30)
     Button(wn2,textvariable=var9,command=lambda:OnButtonClick(9)).place(x=100,y=40,width=30,height=30)

     def refresh ():
         wn2.destroy()
         var.set('  x')
         var1.set(' ')
         var2.set(' ')
         var3.set(' ')
         var4.set(' ')
         var5.set(' ')
         var6.set(' ')
         var7.set(' ')
         var8.set(' ')
         var9.set(' ')
         game()

     Button(wn2,text='Reset',command=refresh).place(x=120,y=160,width=40,height=20)

     Label(wn2,text='User x').place(x=70,y=210,width=40,height=20)
     Label(wn2,text='V/S').place(x=121,y=210,width=30,height=20)
     Label(wn2,text='User o').place(x=170,y=210,width=40,height=20)
     
wn.title('TIC TAC TOE game made by Ishanth')
Button(wn,text='play',command=game).place(x=30,y=100,width=90,height=30)
Button(wn,text='exit',command=wn.destroy).place(x=160,y=100,width=90,height=30)
wn.mainloop()