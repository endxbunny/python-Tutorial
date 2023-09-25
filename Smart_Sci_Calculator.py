from tkinter import *
import _tkinter as tk
import _tkinter
import math

def click(value):
    ex = entryField.get()  #789 ex[0:len(ex)-1]  
    amswer=''


    try:
      
      if value=='C':   # Using C Button 
        ex=ex[0:len(ex)-1]  #78
        entryField.delete(0,END)
        entryField.insert(0,ex)
        return

      elif value=='CE':   # Using CE Button
        entryField.delete(0,END)

      elif value=='√':    #using Square root
        answer= math.sqrt(eval(ex))

      elif value=='π ':   #using pi
        answer=math.pi

      elif value=='cosθ':
        answer=math.cos(math.radians(eval(ex)))
      
      elif value=='tanθ':
        answer=math.tan(math.radians(eval(ex)))
        return
      
      elif value=='sinθ':
        answer=math.sin(math.radians(eval(ex)))
      
      elif value=='2π ':
        answer=2*(math.pi)

      elif value =='cosh':
        answer =math.cosh(eval(ex))

      elif value =='tanh':
        answer =math.tanh(eval(ex))
      
      elif value =='sinh':
        answer =math.sinh(eval(ex))

      elif value == chr(8731):
        answer=eval(ex)**(1/3)

      elif value =='x\u02b8':   # 2**3 = 8
        entryField.insert(END, '**')
        return

      elif value == 'x\u00B3':
        answer=eval(ex)**3
        

      elif value == 'x\u00B2':  
        answer=eval(ex)**2

      elif value == 'ln':
        answer=math.log2(eval(ex))

      elif value == 'deg':
        answer=math.degrees(eval(ex))

      elif value == 'red':
        answer=math.radians(eval(ex))

      elif value == 'e':
        answer=math.e

      elif value == 'log10':
        answer=math.log10(eval(ex))

      elif value == 'x!':
        answer=math.factorial(ex)
        

      elif value == chr(247):
        entryField.insert(END, "/")
        return

      elif value == '=':
        answer=eval(ex)

      else:
        entryField.insert(END,value)
        return
      
        
      entryField.delete(0,END)
      entryField.insert(0,answer)

    except SyntaxError:
     pass
      

root=Tk()
root.title('Smart scintific Calculator') # This is Tittle 
root.config(bg='#E0EEEE') # This is background colour 
root.geometry('680x460+300+300')  # This is geometry

logoImage=PhotoImage(file='logo.png')
logolabel=Label(root,image=logoImage,bg='#008080')  # Incert the cal logo
logolabel.grid(row=0,column=0)

entryField=Entry(root,font=('arial',20,'bold'),bg='#00C5CD',fg='white',bd=10,relief=SUNKEN,width=30) # This is Entry Field Block
entryField.grid(row=0,column=0,columnspan=8)

#micImage=PhotoImage(file='th.png')
#
#micbutton=Button(root,image=micImage,bg='skyblue')  # Incert the mic logo
#micbutton.grid(row=0,column=7)

button_text_list=["C", "CE", "√", "+", " π ", "cosθ", "tanθ", "sinθ", # @ = py  and v = squareroot
                "1", "2", "3", ".", "2π ", "cosh", "tanh", "sinh",  # 2@ = 2py
                "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", # code
                "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                "0", ".","%", "=", "log10", "(", ")", "x!"]
rowvalue=1
columvalue=0                    

for i in button_text_list:

 button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='#00868B',fg='white',font=('arial',18,'bold'),activebackground='skyblue',command=lambda button=i: click(button))
 button.grid(row=rowvalue,column=columvalue,pady=1) # Bild the Button
 columvalue+=1
 if columvalue>7:
    rowvalue+=1
    columvalue=0


root.mainloop()