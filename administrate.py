import tkinter  
import tkinter as tk
from tkinter import *  

def quitw ():
    log_ok = 1
    root.destroy()

def logging ():
    login = entry1.get()
    password = entry2.get()
    log1 = 'pidor'
    pas1 = '123'
    x = tx_info_pas.get(1.0,END)
    if login == log1 and password == pas1 :
        print(login,password, 'Вы вошли')
        quitw()
    if login != log1 and password != pas1 :
        tx_info_pas.configure(state=tk.NORMAL)
        if x != None:
            tx_info_pas.delete(1.0,END)
        tx_info_pas.insert(1.0,'Неправильный Имя и Пароль')
        tx_info_pas.configure(state=tk.DISABLED)
    if login != log1 and password == pas1:
        tx_info_pas.configure(state=tk.NORMAL)
        if x != None:
            tx_info_pas.delete(1.0,END)
        tx_info_pas.insert(1.0,'Неправильное Имя')
        tx_info_pas.configure(state=tk.DISABLED)
    if login == log1 and password != pas1 :
        tx_info_pas.configure(state=tk.NORMAL)
        if x != None:
            tx_info_pas.delete(1.0,END)
        tx_info_pas.insert(1.0,'Неправильное Пароль')
        tx_info_pas.configure(state=tk.DISABLED)

def support ():
    newWin = tk.Toplevel(root)
    newWin.iconbitmap('image//rao_inc.ico')
    newWin.title("Справка")   
    tx_info = Text(newWin,font=('times',12), wrap = WORD,bg = '#DEF7FE',fg = 'red')
    tx_info.pack()
    tx_info.configure(state=tk.NORMAL)
    tx_info.insert(1.0,'Справка 0010    "Вход в систему."')
    tx_info.insert(2.0,'    \n  Введите первичное имя и пароль для получения прав администратора.Все данные идут вместе с пакетом программы. При входе на правах администратора Вы можете изменять сетевые настройки и "Главную странницу" СКАДА-системы для добавления новых елементов. Так же Вы получаете права добавить новых пользователей Вашей системы автоматизации. ')
    tx_info.configure(state=tk.DISABLED)
def beging_on ():
    global root
    root=tk.Tk()
    x=1
    root.iconbitmap('image//rao_inc.ico')
    root.title("Вход в систему")   
    root['bg'] = '#DEF7FE'
    root.update_idletasks()
    s = root.geometry()
    s = s.split('+')
    s = s[0].split('x')
    width_root = int(s[0])
    height_root = int(s[1])
 
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2
    h = h // 2 
    w = (w - width_root // 2)-200
    h = (h - height_root // 2)-200
    root.geometry('+{}+{}'.format(w, h))

    f_top = LabelFrame(root,text='Имя',bg='#DEF7FE')
    f_bot = LabelFrame(root,text='Пароль',bg='#DEF7FE')

    but1 = tkinter.Button(root,text="Ок",width=10,command = logging)

    but2 = tkinter.Button(root,text="Отмена",width=10,command = quitw)

    but3 = tkinter.Button(root,text="Справка",width=10,command = support)
    global tx_info_pas
    tx_info_pas = Text(root,font=('times',12), wrap = WORD,bg = '#DEF7FE',fg = 'black',width = 30,height = 1,state=tk.DISABLED)
    tx_info_pas.pack()

    f_top.pack()
    global entry1
    entry1 = tk.Entry(f_top,width=30)
    entry1.pack(side = LEFT,padx = 5, pady = 5)
    f_bot.pack()
    global entry2
    entry2 = tk.Entry(f_bot,width=30)
    entry2.pack(side = LEFT,padx = 5, pady = 5)
    but3.pack(side = LEFT,padx = 5, pady = 5)
    but2.pack(side = LEFT,padx = 5, pady = 5)
    but1.pack(side = LEFT,padx = 5, pady = 5)

    root.mainloop()


