import tkinter as tk
from PIL import Image, ImageTk
import pygame
import requests
import urllib
import pyttsx3
import math as mt
import random
from tkinter import messagebox

cnt = 0
bx1 = "1"
bx2 = "2"
bx3 = "3"
bx4 = "4"
bx5 = "5"
bx6 = "6"
bx7 = "7"
bx8 = "8"
bx9 = "9"
player = 1

pygame.mixer.init()
main_api="https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=multiple"
json_data=requests.get(main_api).json()
questions=[]
answers=[

]
for i in range(0,10):
    json_q=json_data['results'][i]['question']
    questions.append(json_q)
    json_op0=json_data['results'][i]['correct_answer']
    json_op1=json_data['results'][i]['incorrect_answers'][0]
    json_op2=json_data['results'][i]['incorrect_answers'][1]
    json_op3=json_data['results'][i]['incorrect_answers'][2]

    answers.append([json_op0,json_op1,json_op2,json_op3])


speak=pyttsx3.init()

window=tk.Tk()
window.geometry("800x600+0+0")
window.title("Quiz Game")
window.iconbitmap("images/skull.ico")
#window.resizable(0,0)

txt=tk.StringVar()
expression=""
def main():
    
    def changef(e):
        pic1=tk.PhotoImage(file="images/main_1.png")
        btn.config(image=pic1)
        btn.image=pic1
    def change_backf(e):
        pic1=tk.PhotoImage(file="images/skull_1.png")
        btn.config(image=pic1)
        btn.image=pic1
    
    
    def ques(i,k):
        if i<10:
            if k==0:
                speak.say("Correct")
                speak.runAndWait()
                
            elif k!=0:                                
                gameover()
    
            optindex=[]
            while len(optindex)!=4:
                x = random.randint(0,3)
                if x in optindex:
                    continue
                else:
                    optindex.append(x)
            
            #print(optindex)
            lab_2.config(text=questions[i])
            opt_1.config(text=answers[i][optindex[0]],activebackground=color[optindex[0]],command=lambda:ques(i+1,optindex[0]))
            opt_2.config(text=answers[i][optindex[3]],activebackground=color[optindex[3]],command=lambda:ques(i+1,optindex[3]))
            opt_3.config(text=answers[i][optindex[2]],activebackground=color[optindex[2]],command=lambda:ques(i+1,optindex[2]))
            opt_4.config(text=answers[i][optindex[1]],activebackground=color[optindex[1]],command=lambda:ques(i+1,optindex[1]))
            
        else:
            speak.say("You Win")
            speak.runAndWait()
            opt_1['state']=tk.DISABLED
            opt_1.config(text="Game Over",font=("Arial",30),bg="#100F0D",activebackground="#100F0D",bd=0)
            opt_1.place(relx=0.1,rely=0.25,relheight=0.3,relwidth=0.8)
            opt_2.config(text="Click Here To Play Again",font=("Arial",20),wraplength=200,bg="#100F0D",activebackground="#100F0D",bd=0,command=play)
            opt_2.place(relx=0.1,rely=0.5,relheight=0.3,relwidth=0.8)
            opt_3.config(text="Main Menu",font=("Arial",20),wraplength=200,bg="#100F0D",activebackground="#100F0D",bd=0,command=main)
            opt_3.place(relx=0.1,rely=0.7,relheight=0.3,relwidth=0.8)
            opt_4.destroy()
            lab_2.destroy()

    def gameover():
        speak.say("Game Over")
        speak.runAndWait()
        opt_1['state']=tk.DISABLED
        opt_1.config(text="Game Over",font=("Arial",30),bg="#100F0D",activebackground="#100F0D",bd=0)
        opt_1.place(relx=0.1,rely=0.25,relheight=0.3,relwidth=0.8)
        opt_2.config(text="Click Here To Play Again",font=("Arial",20),wraplength=200,bg="#100F0D",activebackground="#100F0D",bd=0,command=play)
        opt_2.place(relx=0.1,rely=0.5,relheight=0.3,relwidth=0.8)
        opt_3.config(text="Main Menu",font=("Arial",20),wraplength=200,bg="#100F0D",activebackground="#100F0D",bd=0,command=main)
        opt_3.place(relx=0.1,rely=0.7,relheight=0.3,relwidth=0.8)
        opt_4.destroy()
        lab_2.destroy()



    def play():
        global lab_2,opt_1,opt_2,opt_3,opt_4,color
        lab_1.destroy()
        lab_3.destroy()
        lab_5.destroy()
        color=["green","red","red","red"]
        lab_2=tk.Label(f1,text=questions[0],fg="#edda76",bg="#100f0d",bd=0,wraplength=650,font=("Arial"))
        lab_2.place(relx=0.1,rely=0.3,relheight=0.3,relwidth=0.8)
        opt_1=tk.Button(f1,text=answers[0][0],fg="#edda76",activebackground="green",bg="#100f0d",bd=0,wraplength=200,font=("Arial"),command=lambda:ques(1,0))
        opt_1.place(relx=0,rely=0.5,relheight=0.2,relwidth=0.5)
        opt_2=tk.Button(f1,text=answers[0][1],fg="#edda76",activebackground="red",bg="#100f0d",bd=0,wraplength=200,font=("Arial"),command=gameover)
        opt_2.place(relx=0.5,rely=0.5,relheight=0.2,relwidth=0.5)
        opt_3=tk.Button(f1,text=answers[0][2],fg="#edda76",activebackground="red",bg="#100f0d",bd=0,wraplength=200,font=("Arial"),command=gameover)
        opt_3.place(relx=0,rely=0.7,relheight=0.2,relwidth=0.5)
        opt_4=tk.Button(f1,text=answers[0][3],fg="#edda76",activebackground="red",bg="#100f0d",bd=0,wraplength=200,font=("Arial"),command=gameover)
        opt_4.place(relx=0.5,rely=0.7,relheight=0.2,relwidth=0.5)


    def Tic():  
        def cleartic():
            global player,cnt,bx1,bx2,bx3,bx4,bx5,bx6,bx7,bx8,bx9
            cnt = 0
            bx1 = "1"
            bx2 = "2"
            bx3 = "3"
            bx4 = "4"
            bx5 = "5"
            bx6 = "6"
            bx7 = "7"
            bx8 = "8"
            bx9 = "9"
            player = 1

        def activate(box):
            
            global player,cnt,bx1,bx2,bx3,bx4,bx5,bx6,bx7,bx8,bx9
            cnt =cnt +1
            if box == 1 and player == 1:
                button1.config(text="O")
                player = 2
                bx1="O"
            elif box == 1 and player == 2:
                button1.config(text="X")
                player =1
                bx1="X"
            elif box == 2 and player == 1:
                button2.config(text="O")
                player = 2
                bx2="O"
            elif box == 2 and player == 2:
                button2.config(text="X")
                player =1
                bx2="X"
            elif box == 3 and player == 1:
                button3.config(text="O")
                player = 2
                bx3="O"
            elif box == 3 and player == 2:
                button3.config(text="X")
                player =1
                bx3="X"
            elif box == 4 and player == 1:
                button4.config(text="O")
                player = 2
                bx4="O"
            elif box == 4 and player == 2:
                button4.config(text="X")
                player =1
                bx4="X"
            elif box == 5 and player == 1:
                button5.config(text="O")
                player = 2
                bx5="O"
            elif box == 5 and player == 2:
                button5.config(text="X")
                player =1
                bx5="X"
            elif box == 6 and player == 1:
                button6.config(text="O")
                player = 2
                bx6="O"
            elif box == 6 and player == 2:
                button6.config(text="X")
                player =1
                bx6="X"
            elif box == 7 and player == 1:
                button7.config(text="O")
                player = 2
                bx7="O"
            elif box == 7 and player == 2:
                button7.config(text="X")
                player =1
                bx7="X"
            elif box == 8 and player == 1:
                button8.config(text="O")
                player = 2
                bx8="O"
            elif box == 8 and player == 2:
                button8.config(text="X")
                player =1
                bx8="X"
            elif box == 9 and player == 1:
                button9.config(text="O")
                player = 2
                bx9="O"
            elif box == 9 and player == 2:
                button9.config(text="X")
                player =1
                bx9="X"

            if bx1 == bx2 == bx3 =="O" or bx4 == bx5 == bx6 =="O" or bx7 == bx8 == bx9 =="O":
                player = "O"
                messagebox._show("Game end", "player: " + player + " wins")
                cleartic()
                #exit(0)
            elif bx1 == bx2 == bx3 =="X" or bx4 == bx5 == bx6 =="X" or bx7 == bx8 == bx9 =="X":
                player = "X"
                messagebox._show("Game end", "player: " + player + " wins")
                cleartic()
                #exit(0)
            elif bx1 == bx4 == bx7 =="O" or bx2 == bx5 == bx8 =="O" or bx3 == bx6 == bx9 =="O":
                player = "O"
                messagebox._show("Game end", "player: " + player + " wins")
                cleartic()
                #exit(0)
            elif bx1 == bx4 == bx7 =="X" or bx2 == bx5 == bx8 =="X" or bx3 == bx6 == bx9 =="X":
                player = "X"
                messagebox._show("Game end", "player: " + player + " wins")
                cleartic()
                #exit(0)
            elif bx1 == bx5 == bx9 =="O" or bx3 == bx5 == bx7 =="O":
                player = "O"
                messagebox._show("Game end", "player: " + player + " wins")
                cleartic()
                #exit(0)
            elif bx1 == bx5 == bx9 =="X" or bx3 == bx5 == bx7 =="X":
                player = "X"
                messagebox._show("Game end", "player: " + player + " wins")
                cleartic()
                #exit(0)
            elif cnt == 9:
                messagebox._show("Game end", "Draw")
                cleartic()
                #exit(0)

        root= tk.Toplevel(window)
        root.title("Tic-Tac-Toe")
        root.geometry("290x258")
        button1 = tk.Button(root, text = "  ",command = lambda: activate(1))
        button1.grid(row='0',column="0",ipadx="40",ipady="30")
        button2 = tk.Button(root, text = "  ",command = lambda: activate(2))
        button2.grid(row='0',column="1",ipadx="40",ipady="30")
        button3 = tk.Button(root, text = "  ",command = lambda: activate(3))
        button3.grid(row='0',column="2",ipadx="40",ipady="30")
        button4 = tk.Button(root, text = "  ",command = lambda: activate(4))
        button4.grid(row='1',column="0",ipadx="40",ipady="30")
        button5 = tk.Button(root, text = "  ",command = lambda: activate(5))
        button5.grid(row='1',column="1",ipadx="40",ipady="30")
        button6 = tk.Button(root, text = "  ",command = lambda: activate(6))
        button6.grid(row='1',column="2",ipadx="40",ipady="30")
        button7 = tk.Button(root, text = "  ",command = lambda: activate(7))
        button7.grid(row='2',column="0",ipadx="40",ipady="30")
        button8 = tk.Button(root, text = "  ",command = lambda: activate(8))
        button8.grid(row='2',column="1",ipadx="40",ipady="30")
        button9 = tk.Button(root, text = "  ",command = lambda: activate(9))
        button9.grid(row='2',column="2",ipadx="40",ipady="30")
        
        

        root.mainloop()



    def calc():
        root=tk.Toplevel(window)
        root.geometry("230x400")
        root.resizable(0,0)
        root.title("Calculator")

        
        def sqroot():
            add=mt.sqrt(float(expression))
            txt.set(add)

        def click(num):
            global expression
            expression=expression + str(num)
            txt.set(expression)

        def equal():
            try:
                global expression
                add=str(eval(expression))
                txt.set(add)

                expression=""
            except:
                txt.set("Error")
                expression=""

        def clr():
            global expression
            length=len(txt.get())
            e1.delete(length-1,'end')

        def clearall():
            global expression
            expression=""
            txt.set("")

        f_01=tk.Frame(root,width=390,height=100,bg="white")
        f_01.grid(row=0,column=0)
        #f_01.pack(side=TOP)
        f_02=tk.Frame(root,width=390,height=368,bg="grey")
        f_02.grid(row=1,column=0)
        #f_02.pack(side=BOTTOM)

        l1=tk.Label(f_01,text="My Calculator",font=("Arial Bold",20))
        l1.pack(side=tk.TOP,expand=tk.YES)

        e1=tk.Entry(f_01,textvariable=txt,width=23,bd=10,font=("Arial Bold",12),
                fg="black",bg="light grey",relief=tk.RIDGE,justify=tk.RIGHT)

        e1.pack(side=tk.TOP)
        e1.insert(0,"0")

        button_1=tk.Button(f_02,text="1",padx=20,pady=20,command=lambda:click(1))
        button_2=tk.Button(f_02,text="2",padx=20,pady=20,command=lambda:click(2))
        button_3=tk.Button(f_02,text="3",padx=20,pady=20,command=lambda:click(3))
        button_4=tk.Button(f_02,text="4",padx=20,pady=20,command=lambda:click(4))
        button_5=tk.Button(f_02,text="5",padx=20,pady=20,command=lambda:click(5))
        button_6=tk.Button(f_02,text="6",padx=20,pady=20,command=lambda:click(6))
        button_7=tk.Button(f_02,text="7",padx=20,pady=20,command=lambda:click(7))
        button_8=tk.Button(f_02,text="8",padx=20,pady=20,command=lambda:click(8))
        button_9=tk.Button(f_02,text="9",padx=20,pady=20,command=lambda:click(9))
        button_0=tk.Button(f_02,text="0",padx=20,pady=20,command=lambda:click(0))

        button_clr=tk.Button(f_02,text="clr",padx=17,pady=20,command=clr)
        button_clrall=tk.Button(f_02,text="clr/all",padx=8,pady=20,command=clearall)
        button_equal=tk.Button(f_02,text="=",padx=20,pady=20,command=equal)
        #button_clr=Button(f_02,text="clr",padx=80,pady=20,command=clr)

        button_add=tk.Button(f_02,text="+",padx=20,pady=20,command=lambda:click("+"))
        button_sub=tk.Button(f_02,text="-",padx=20,pady=20,command=lambda:click("-"))
        button_mul=tk.Button(f_02,text="*",padx=20,pady=20,command=lambda:click("*"))
        button_div=tk.Button(f_02,text="/",padx=20,pady=20,command=lambda:click("/"))
        button_dot=tk.Button(f_02,text=".",padx=20,pady=20,command=lambda:click("."))
        button_pow=tk.Button(f_02,text="^",padx=20,pady=20,command=lambda:click("**"))
        button_sqrot=tk.Button(f_02,text="√",padx=20,pady=20,command=sqroot)


        button_1.grid(row=3,column=0)
        button_2.grid(row=3,column=1)
        button_3.grid(row=3,column=2)

        button_4.grid(row=2,column=0)
        button_5.grid(row=2,column=1)
        button_6.grid(row=2,column=2)

        button_7.grid(row=1,column=0)
        button_8.grid(row=1,column=1)
        button_9.grid(row=1,column=2)

        button_add.grid(row=3,column=3)
        button_sub.grid(row=2,column=3)
        button_mul.grid(row=1,column=3)
        button_div.grid(row=0,column=3)
        button_dot.grid(row=4,column=2)
        button_pow.grid(row=0,column=1)
        button_sqrot.grid(row=0,column=2)


        button_0.grid(row=4,column=1)
        button_clr.grid(row=0,column=0)
        button_equal.grid(row=4,column=3)
        button_clrall.grid(row=4,column=0)

        root.mainloop()

    def clicked():
        global pic2,playpic,morepic,devpic,closepic,lab_3,lab_5,lab_1
        pygame.mixer.music.load("images/deeplaugh.mp3")
        pygame.mixer.music.play(loops=0)
        pic2=tk.PhotoImage(file="images/panel_1.png",)
        lab_0=tk.Label(f1,image=pic2,bd=0,bg="#100F0D")
        lab_0.place(relx=0.1,rely=0,relheight=0.3,relwidth=0.8)

        
        closepic=tk.PhotoImage(file="images/button_close.png")
        lab_c=tk.Button(f1,image=closepic,bg="#100F0D",activebackground="#100f0d",bd=0,command=exit)
        lab_c.place(relx=0.7,rely=0,relheight=0.2,relwidth=0.3)        

        playpic=tk.PhotoImage(file="images/button_play.png")
        lab_1=tk.Button(f1,image=playpic,bg="#100F0D",activebackground="#100F0D",bd=0,command=play)
        lab_1.place(relx=0.1,rely=0.3,relheight=0.3,relwidth=0.8)

        morepic=tk.PhotoImage(file="images/button_calc.png")
        lab_3=tk.Button(f1,image=morepic,bg="#100F0D",activebackground="#100f0d",bd=0,command=calc)
        lab_3.place(relx=0.1,rely=0.5,relheight=0.3,relwidth=0.8)

        devpic=tk.PhotoImage(file="images/button_tic.png")
        lab_5=tk.Button(f1,image=devpic,bg="#100F0D",activebackground="#100f0d",bd=0,command=Tic)
        lab_5.place(relx=0.1,rely=0.7,relheight=0.3,relwidth=0.8)

        btn.destroy()
     
    global f1
    f1=tk.Frame(window,bg="#100F0D")
    f1.place(relwidth=1,relheight=1)
    pic1=tk.PhotoImage(file="images/skull_1.png")

    btn=tk.Button(f1,image=pic1,bg="#100F0D",bd=0,command=clicked,activebackground="#100f0d")
    btn.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
    btn.bind("<Enter>",changef)
    btn.bind("<Leave>",change_backf)

    window.mainloop()

main()