import string
import tkinter as tk
import tkinter.ttk as ttk
import os
import random
from tkinter import END
from PIL import ImageTk,Image

streak=0
life=8
tScore=0
def check():
    global streak
    global life
    global tScore
    global score
    val = e1.get().strip()
    if val=="":
        val=None
    global scvalue
    scvalue.set(" ")
    if val==l2['text']:
        e1.update()
        msglbl['text']="Correct Answer !"
        streak+=1
        print("streak= ",streak)
        print('life=',life)
        if streak % 3 == 0:
            if life==0:
                life1.config(state="active")
            if life == 1:
                life2.config(state="active")
            elif life == 2:
                life3.config(state="active")
            elif life == 3:
                life4.config(state="active")
            elif life == 4:
                life5.config(state="active")
            elif life == 5:
                life6.config(state="active")
            elif life == 6:
                life7.config(state="active")
            elif life == 7:
                life8.config(state="active")

            life=life+1
            print("after recover:",life)
        tScore+=1
    else :
        print("Wrong ans",l2['text'])
        e1.update()
        msglbl['text']="Wrong Answer !"
        streak=0

        if life==8:
            life8.config(state='disabled')
            life = life - 1
        elif life==7:
            life7.config(state='disabled')
            life=life-1
        elif life == 6:
            life6.config(state='disabled')
            life = life - 1
        elif life == 5:
            life5.config(state='disabled')
            life = life - 1
        elif life == 4:
            life4.config(state='disabled')
            life = life - 1
        elif life == 3:
            life3.config(state='disabled')
            life = life - 1
        elif life == 2:
           # root.config(bg="red")
            life2.config(state='disabled')
            life = life - 1
        elif life == 1:
            life1.config(state='disabled')
            life = life - 1
        elif life==0:
            root.destroy()

    score.set(tScore)


def operation(event):
    check()
    with open("data/WordHunter.txt", "r") as file:
        allText = file.read()
        word = list(map(str, allText.split()))
        txt=random.choice(word)
        l2['text']=txt
        # print random string
        del word
        e1.focus_set()






root=tk.Tk()

root.geometry("400x400")
root.title("Word Hunter")
root.config(bg="skyblue")

score=tk.StringVar()
times=tk.StringVar()

l1=tk.Label(root,text="Word Hunter",font=("lucida",'20','italic'),bg="violet")
l1.place(x=120,y=10)

l5=tk.Label(text="SCORE",font=('Times new roman','14','bold'),fg='red',bg="skyblue")
l5.place(x=10,y=16)

l3=tk.Label(text="0",textvar=score,font=('Times new roman','40','bold'),fg='red',bg="skyblue")
l3.place(x=30,y=50)


l4=tk.Label(text="TIME",font=('Times new roman','14','bold'),fg='red',bg="skyblue")
l4.place(x=300,y=16)

l2=tk.Label(root,text="Start",font=("timesnewroman",'30','bold'),fg="black",bg="skyblue",padx='10',pady="10",justify = tk.CENTER,width=9)
l2.place(x=90,y=60)

msglbl=tk.Label(root,text="Welcome",font=("lucida",'20','italic'),bg='skyblue',fg='green')
msglbl.place(x=120,y=200)



img=Image.open("data/heart1.png")
img = img. resize((30, 30), Image. ANTIALIAS)
my_img1= ImageTk. PhotoImage(img)


life1=tk.Label(root,width=30,height=30,image=my_img1)
life1.place(x=50,y=150)

life2=tk.Label(root,width=30,height=30,image=my_img1)
life2.place(x=90,y=150)

life3=tk.Label(root,width=30,height=30,image=my_img1)
life3.place(x=130,y=150)

life4=tk.Label(root,width=30,height=30,image=my_img1)
life4.place(x=170,y=150)

life5=tk.Label(root,width=30,height=30,image=my_img1)
life5.place(x=210,y=150)

life6=tk.Label(root,width=30,height=30,image=my_img1)
life6.place(x=250,y=150)

life7=tk.Label(root,width=30,height=30,image=my_img1)
life7.place(x=290,y=150)

life8=tk.Label(root,width=30,height=30,image=my_img1)
life8.place(x=330,y=150)






#
scvalue=tk.StringVar()
# update()
e1=tk.Entry(root,bg="skyblue",textvar=scvalue,font=('lucida','30','italic'), width = 15, bd = 2, justify = tk.CENTER)
e1.place(x=40,y=250)
e1.bind('<Return>',operation)
b1=tk.Button(root,text="SUBMIT",activebackground="red",bd=1,width=20,height=3,bg='yellowgreen',font=("timesnewroman",'10','bold'))
b1.place(x=120,y=330)
b1.bind('<Return>',operation)
b1.bind("<Button-1>",operation)


root.mainloop()