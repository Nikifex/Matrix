import tkinter as tk
import numpy as np
global matr
matsize = np.array([5,5])
matr = np.random.randint(100,size=(matsize))
global metr
metr = matr.copy()

def rota90():
  global numers
  global rotmatr
  global rotmatr1
  global rotmatr2
  global c
  if c == 0:
    rotmatr = np.rot90(metr, k=-1)
    labl2_2['text'] = rotmatr
    c+=1
  elif c== 1:
     rotmatr1 = np.rot90(metr, k=-2)
     labl2_2['text'] = rotmatr1
     c += 1
  elif c==2:
     rotmatr2 = np.rot90(metr, k=-3)
     labl2_2['text'] = rotmatr2
     c += 1
  else :
     labl2_2['text'] = metr
     c-=3
c=0

def butsdviga1():
    global numers
    #global razi
    if c==0:
        numers = list(metr[1].flatten())
        for i in range(1):
            k = numers.pop()
            numers = [k] + numers
        metr[1] = numers
        labl2_2['text'] = metr

    elif c==1:
        numers = list(rotmatr[1].flatten())
        for i in range(1):
          k = numers.pop()
          numers = [k] + numers
        rotmatr[1] = numers
        labl2_2['text'] = rotmatr

    elif c==2:
        numers = list(rotmatr1[1].flatten())
        for i in range(1):
            k = numers.pop()
            numers = [k] + numers
        rotmatr1[1] = numers
        labl2_2['text'] = rotmatr1

    else:
        numers = list(rotmatr2[1].flatten())
        for i in range(1):
            k = numers.pop()
            numers = [k] + numers
        rotmatr2[1] = numers
        labl2_2['text'] = rotmatr2

def buttdel():
    #global razi
    global c
    #metr = matr.copy()
    metr[1]=matr[1].copy()
    labl2_2['text']=''
    c=0


window=tk.Tk()
#window.geometry('600x400')
labl0=tk.Label(text=' ')                                             #пустой label для разметки слева
labl0_1=tk.Label(text=' ')                                           #пустой label для разметки справа
labl1=tk.Label(text='Исходная матрица:')
labl1_1=tk.Label(text=matr,bg="black",fg="green",width=20,height=10) #поле вывода слева
labl2=tk.Label(text='Полученная матрица:')
labl2_2=tk.Label(bg="black",fg="green",width=20,height=10)           #поле вывода справа

#здесь размещение label
labl1.grid(row=1,column= 2,columnspan=2)
labl1_1.grid(row=2,column=2,columnspan=2)
labl2.grid(row=1,column=5)
labl2_2.grid(row=2,column=5,columnspan=2)
labl0.grid(row=1,column=1)
labl0_1.grid(row=1,column=7)

#здесь кнопки
but90=tk.Button(text='Поворот на 90',command= rota90)
butdel=tk.Button(text='Удаление результата',command=buttdel)
butsdvig1=tk.Button(text='Сдвинуть вторую строчку на 1',command=butsdviga1)

#здесь размещение кнопок
but90.grid(row=3,column=4)
butdel.grid(row=5,column=4)
butsdvig1.grid(row=4,column=4)
window.mainloop()