from tkinter import *
from PIL import Image,ImageTk
import random
root = Tk()
root.iconbitmap('icons/scissors.ico')
root.config(bg='#F9F105')
score_you = 0
score_bot = 0
rock = ImageTk.PhotoImage(Image.open('rps/rock.png'))
paper = ImageTk.PhotoImage(Image.open('rps/paper.png'))
scissor = ImageTk.PhotoImage(Image.open('rps/scissor.png'))

def findWord(c):
    if c=='R':
        return 'Rock'
    elif c=='P':
        return 'Paper'
    elif c=='S':
        return 'Scissor'

def findWin(y):
    global score_bot
    global score_you
    global label_score_you
    global label_score_bot

    l = ['P', 'S', 'R']
    num = random.randint(1,10000)%3
    b = l[num]

    if score_you<9 and score_bot<9:
        if y=='R' and b=='S' or y=='P' and b=='R' or y=='S' and b=='P':
            score_you+=1
            label_score_you = Label(root, text=score_you, font=("Roboto", 70, "bold"), fg='#3B3B34', bg='#F9F105',pady=10).grid(row=2, column=0, columnspan=2)

        elif y=='R' and b=='P' or y=='P' and b=='S' or y=='S' and b=='R':
            score_bot+=1
            label_score_bot = Label(root, text=score_bot, font=("Roboto", 70, "bold"), fg='#3B3B34', bg='#F9F105',pady=10).grid(row=2, column=1, columnspan=2)

        elif y==b:
            pass

        label_score_you = Label(root, text=findWord(y), font=("Roboto", 20, "bold"), fg='#3B3B34', bg='#F9F105', pady=10, padx=25).grid(row=3, column=0, columnspan=2)
        label_score_bot = Label(root, text=findWord(b), font=("Roboto", 20, "bold"), fg='#3B3B34', bg='#F9F105', pady=10, padx=25).grid(row=3, column=1, columnspan=2)

    else:
        if y=='R' and b=='S' or y=='P' and b=='R' or y=='S' and b=='P':
            score_you+=1
            label_score_you = Label(root, text=score_you, font=("Roboto", 80, "bold"), fg='#3B3B34', bg='#F9F105',pady=10).grid(row=2, column=0, columnspan=2)

        elif y=='R' and b=='P' or y=='P' and b=='S' or y=='S' and b=='R':
            score_bot+=1
            label_score_bot = Label(root, text=score_bot, font=("Roboto", 80, "bold"), fg='#3B3B34', bg='#F9F105',pady=10).grid(row=2, column=1, columnspan=2)

        elif y==b:
            pass
        button_rock = Button(root, image=rock, height=250, width=250, command=lambda: findWin('R'), state=DISABLED).grid(row=4,column=0)
        button_paper = Button(root, image=paper, height=250, width=250, command=lambda: findWin('P'), state=DISABLED).grid(row=4,column=1)
        button_scissor = Button(root, image=scissor, height=250, width=250, command=lambda: findWin('S'), state=DISABLED).grid(row=4,column=2)

        if score_you > score_bot:
            label_result = Label(root, text='You Won!',font=("Roboto",30,"bold"), fg='#46DB37', bg='#F9F105', padx=30, pady=20).grid(row=4,column=0,columnspan=3)
        elif score_you < score_bot:
            label_result = Label(root, text='You Lost!', font=("Roboto", 30, "bold"), fg='#EF1F1F', bg='#F9F105', padx=30, pady=20).grid(row=4, column=0, columnspan=3)
        elif score_you == score_bot:
            label_result = Label(root, text='DRAW', font=("Roboto", 30, "bold"), fg='#3B3B34', bg='#F9F105', padx=30, pady=20).grid(row=4, column=0, columnspan=3)


label_title = Label(root, text='Rock Paper Scissor', font=("Roboto",40,"bold"), fg='#3B3B34', bg='#F9F105', padx=130, pady=20).grid(row=0,column=0,columnspan=3)
label_ai = Label(root, text='Bot', fg='#3B3B34', bg='#F9F105', font=("Roboto",20,"bold"), padx=200).grid(row=1,column=1,columnspan=2)
label_player = Label(root, text='You', fg='#3B3B34', bg='#F9F105', font=("Roboto",20,"bold"), padx=200).grid(row=1,column=0,columnspan=2)

label_score_you = Label(root, text=score_you, font=("Roboto",70,"bold"), fg='#3B3B34', bg='#F9F105', pady=10).grid(row=2,column=0,columnspan=2)
label_score_bot = Label(root, text=score_bot, font=("Roboto",70,"bold"), fg='#3B3B34', bg='#F9F105', pady=10).grid(row=2,column=1,columnspan=2)

button_rock = Button(root, image=rock, height=250, width=250, command=lambda: findWin('R')).grid(row=4,column=0)
button_paper = Button(root, image=paper, height=250, width=250, command=lambda: findWin('P')).grid(row=4,column=1)
button_scissor = Button(root, image=scissor, height=250, width=250, command=lambda: findWin('S')).grid(row=4,column=2)


root.mainloop()