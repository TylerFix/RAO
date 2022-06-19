# Ниже приведены условные метки для комфортного перемещения между функций. Выделяем, вместе с "//" и латиницей вызываем поиск "Ctrl+F".
# Для дальнейшего удобство всем новым функциям назначаем номер метки, либо уже существующий номер(если это дополнение), либо новый(если это абсолютно новый блок).
# Такая же копия меток лежит в корне в текстовом документе.
#//M001 - Параметризация окна и работы с окном ткинтера.
#//M002 - Любые меню.
#//M003 - Тулбар.
#//M004 - Стили виджетов.
#//M005 - Окно добавления новых изображений на осн.окно
#//M006 - Окна параметров создаваемых объектов и процес их отрисовки на холсте основного окна.
#//M007 - BackUp.
#//M008 - Ивенты/виджеты/вызов функций при инициализации
#//M009 - Фокус на виджетах основного окна.
#//M010 - Сохранение проекта.
#//M011 - Загрузка проекта.

#//M100 - Основное окно, появление, параметризация.
#//M101 - Лейбл в потоке на основном окне.
#//M102 - Окна созданий виджетов на осн.окно.
#//M103 - Создание виджетов.
#//M104 - Пины на отправку в пакет.
#//M105 - Воссоздание загружаемых виджетов.
#//M106 - Перемещение виджетов осн.окна.
#//M107 - Удаление виджетов осн.окна.

#//M200 - Сети, появление, параметризация.
#//M201 - Создание стартового сервера(изображение), сетевые конфиги.
#//M202 - Сервер.
#//M203 - Запуск отдельных потоков.(нужно найти все.)
#//M204 - Создание объектов сетей.
#//M205 - Ввосоздание загруженных объектов сетей.
#//M206 - Дополнительные линии/перемещение объектов в сетях.
#//M207 - Удаление объектов из сетей.
#//M208 - Линии в сетях.
#//M209 - Удаление линий в сетях.
#//M210 - Окна создания объектов в сетях.

#//M300 - Логика,создание,параметризация.

#//M400 - Тренды.

#//M500 - Таблица символов.

#//M000 - Тестовая метка.


from tkinter import *                # Библиотека окон и внутриоконных виджетов
import tkinter                      # Дублируем
import socket                       # Библиотека сетевых сокетов, для создания связей между сервером и клиентом
import time                         # Библиотека времени для торможения отдельных блоков и их уход в "сон"
import threading                    # Библиотека многопоточности
import os                           # Библиотека для работы с операционной системой(создание папок и т.д.)
import shutil                       # Библиотека создании архивов
from os import path
from time import sleep
import tkinter as tk
from functools import partial
import pickle                       # Библиотека для консервации и шифровании данных
import matplotlib.pyplot as plt     # Библиотека для создания окон с трендами
from datetime import datetime       # Библиотека времени и даты
from tkinter import ttk
from tkinter import filedialog as fd
import random                       # Рандомные числа
import math                         # Математический модуль
from shutil import make_archive
from _thread import start_new_thread# Ещё один модуль многопоточности
import tkinter.ttk as ttk
from PIL import Image, ImageTk      # Библиотека для работы с изображениями(кросплатформа)
from subprocess import call
#import testing_06_08
import administrate as adm

global x1 
global y1
import regex                        # Библиотека для конвертации строк в int


class raoconnect:
    def __init__(self):
        # Параметры первичного окна //M001
        self.window = tkinter.Tk()                                                              # Создаем окно
        self.window.title("RAOconnect1.0.5.7")                                                  # Версия программы в шапке
        self.window.iconbitmap('image//rao_inc.ico')
        self.window['bg'] = '#DEF7FE'                                                           # цвет основного окна, не работает если есь notebook
        mainmenu = Menu(self.window,background = '#28444d')                                     # Всё, что ниже относится к созданию меню
        self.window.config(menu=mainmenu)
        self.redk = 'Редактирование ВКЛ'
        # Меню внутри окна self.window //M002
        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Открыть",command = self.insert_text)
        filemenu.add_command(label="Новый")
        filemenu.add_command(label="Сохранить",command = self.saveprog)
        filemenu.add_command(label='Сохранить как...',command = self.extract_text)
        filemenu.add_command(label="Загрузить",command = self.loadprog)
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command = self.quitw)
        helpmenu = Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="Помощь")
        helpmenu.add_command(label="О программе")
        mainmenu.add_cascade(label="Файл",menu=filemenu)
        mainmenu.add_cascade(label="Справка",menu=helpmenu)

        filemenu3 = Menu(mainmenu, tearoff=0)
        filemenu3.add_command(label="Add page " ,command = self.add_new_page)
        mainmenu.add_cascade(label="Инструменты",menu=filemenu3)
        filemenu3.add_command(label="Add ... " ,command = self.win_inst)
        # Туллбар //M003
        self.toolbar = Frame(self.window, bg='#28444d',bd = 1, relief=RAISED)
        self.img = Image.open('image//power_off.png')
        eimg = ImageTk.PhotoImage(self.img)
        exitButton = Button(self.toolbar, image=eimg, relief=FLAT,bg = '#28444d',command = self.quitw) # Временная кнопка в тулбаре на таблицу символов
        exitButton.image = eimg
        exitButton.pack(side=LEFT, padx=2, pady=2)
        self.toolbar.pack(side=TOP, fill=X)
        self.id_image_ic = Image.open('image//RAOminitoolbaRSS.png')
        ic_image = ImageTk.PhotoImage(self.id_image_ic)
        icon = Button(self.toolbar,image=ic_image, relief=FLAT,bg='#28444d')
        icon.image = ic_image
        icon.pack(side=RIGHT,padx=2,pady=2)
        # Кнопка символьной таблицы //M003
        self.img_symv_table = Image.open('image//sym_tab.png')
        symv_eimg = ImageTk.PhotoImage(self.img_symv_table)
        symvButton = Button(self.toolbar,image=symv_eimg,relief=FLAT,bg ='#28444d',command = self.addfuntrd_training)
        symvButton.image = symv_eimg
        symvButton.pack(side=LEFT,padx=2,pady=2)
        # Кнопка таблицы тегов //M003
        self.img_tag_table = Image.open('image//tag_tab.png')
        tag_eimg = ImageTk.PhotoImage(self.img_tag_table)
        tagButton = Button(self.toolbar,image=tag_eimg,relief=FLAT,bg ='#28444d' )
        tagButton.image = tag_eimg
        tagButton.pack(side=LEFT,padx=2,pady=2)
        # Кнопка добавления новой страницы //M003
        self.img_new_page = Image.open('image//new_page.png')
        page_eimg = ImageTk.PhotoImage(self.img_new_page)
        pageButton = Button(self.toolbar,image=page_eimg,relief=FLAT,bg='#28444d')
        pageButton.image = page_eimg
        pageButton.pack(side=LEFT,padx=2,pady=2)
        # Кнопка вызова трендов //M003
        self.img_tool_trend = Image.open('image//trend.png')
        trend_eimg = ImageTk.PhotoImage(self.img_tool_trend)
        trendButton = Button(self.toolbar,image=trend_eimg,relief=FLAT,bg='#28444d',command = self.trd)
        trendButton.image = trend_eimg
        trendButton.pack(side=LEFT,padx=2,pady=2)
        # Кнопка администратора //M003
        self.img_tool_admin = Image.open('image//administrator.png')
        admin_eimg = ImageTk.PhotoImage(self.img_tool_admin)
        adminButton = Button(self.toolbar,image=admin_eimg,relief=FLAT,bg='#28444d',command = self.administrate_on)
        adminButton.image = admin_eimg
        adminButton.pack(side=RIGHT,padx=2,pady=2)
        # Кнопка окна информации //M003
        self.img_tool_info = Image.open('image//info.png')
        info_eimg = ImageTk.PhotoImage(self.img_tool_info)
        infoButton = Button(self.toolbar,image=info_eimg,relief=FLAT,bg='#28444d')
        infoButton.image = info_eimg
        infoButton.pack(side=RIGHT,padx=2,pady=2)
        
        # Включение полноэкранного режима дефолт //M001
        self.window.attributes('-fullscreen', True)
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        # Создание собственных стилей виджетов//M004
        style = ttk.Style()
        gui_style = ttk.Style()
        gui_style.configure('My.TFrame', background='#334353')
        mygreen = "#3d6a78"
        myred = '#DEF7FE'#"#3D856E"

        style.theme_create( "yummy", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 2, 2, 0],"background": mygreen } },
                "TNotebook.Tab": {
                "configure": {"padding": [25, 7], "background": mygreen },
                "map":       {"background": [("selected", myred)],
                              "expand": [("selected", [1, 1, 1, 1])] } } } )

        style.theme_use("yummy")
        # Координаты окна/разрешение монитора //M001
        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()      # Получаем координы монитора и заедаем постоянные переменные для анализа геометрии объектов, в будущем нужно все объекты подвести под этот параметр
        self.window.geometry("%dx%d+0+0" % (self.w, self.h))                                    # Задаем геометрию окна исходя из кода выше
        self.xex = self.window.winfo_pointerx ()                                        
        self.yey = self.window.winfo_pointery ()
        # Функциональный переход между страницами //M001
        self.notebook=ttk.Notebook(self.window,width=self.w, height=self.h)                     # Создаем вкладки и указываем, где они должны находится
        print (self.w,'sf', self.h)
        # Основное окно //M100
        self.frame1 = ttk.Frame(self.notebook,style='My.TFrame')
        # Холст Основного окна //M100
        self.canvas1=Canvas(self.frame1,width=self.w,height=self.h,bg='#DEF7FE')
        # Вкладка "Сети" //M200
        self.frame2 = ttk.Frame(self.notebook,style='My.TFrame')
        # Вкладка "Логика" //M300
        self.frame3 = ttk.Frame(self.notebook,style='My.TFrame')
        # //M100
        self.notebook.add(self.frame1,text='Основное окно')
        # //M200
        self.notebook.add(self.frame2,text='Сеть')
        # //M300
        self.notebook.add(self.frame3,text='Логика')
        self.notebook.pack()
        # Холст окна "Сети" // M200
        self.canvas=Canvas(self.frame2,width=self.w,height=self.h,bg='#DEF7FE')
        # Холст окна "Логика" // M300
        self.canvas2=Canvas(self.frame3,width=self.w,height=self.h,bg='#DEF7FE')
        # Объявление/инициализация переменных int/str //M001
        self.test = 0
        self.confx = 0
        self.confy = 0
        self.canvas2.grid()
        self.canvas.grid()                                                                      # хуйня этот ваш грид, нужно по-другому как-то, но пока что так
        self.canvas1.grid()
        self.counter = 0                                                                        # Не помню для чего я создавал этот счётчик
        self.papi = 1
        self.x = int                                                                            # Ниже тестовые координаты
        self.y = int
        self.x1 = 80
        self.y1 = 80
        self.go = False                                                                         # Состояние для показа массива данных от контроллера(кнопка), потом будет убран
        self.result = int                                                                       # Важная хуйня, строка данных от клиента. С неё берем все елементы массива для указания тегов
        self.pin2 = 0                                                                           # Тестовые теги
        self.pin3 = 0
        self.pin4 = 0
        self.pin5 = 0
        self.pin6 = 0
        self.pin7 = 0
        self.pin8 = 0
        self.pin9 = 0
        self.pin10 = 0
        self.pin11 = 0
        self.pin12 = 0 
        self.pin13 = 0
        self.knop =  '0'                                                                        # Устанавливаем в строку 0, поскольку в другом случае, при устанавливании новой кнопки первое значение будет состояние переменной str
        self.num_widget = '0'
        self.cmd = str
        self.count1 = 0 
        self.count = 0                                                                          # Два счётчика учавствуют в сохранении и выгрузке созданных кнопок, взводятся каждый раз, когда появляется новая кнопка и указывает елемент массива, в который мы записали информацию и кнопке
        self.count2 = 0
        self.countl = 0
        self.counte = 0
        self.counts = 0
        self.cntb = 0
        self.cnte = 0
        self.cntl = 0
        self.cnts = 0
        self.exp = '0'                                                                          # То же самое, что и с self.knop
        self.UNI_count = 0
        self.UNI_1_count = 0
        self.nano_count = 0
        self.mega_count = 0
        self.ethernet_count = 0
        self.server_count = 0
        self.cnt_UNI = 0
        self.cnt_UNI_1 = 0
        self.cnt_nano = 0
        self.cnt_mega = 0
        self.cnt_ethernet = 0
        self.cnt_server = 0 
        self.ms = 0
        self.line_ethernet_kordy = 0
        self.line_wifi_kordy = 0
        self.dop_line_ethernet_count = 0
        self.num_line_ethernet = 0
        self.dop_line_wifi_count = 0
        self.main_line_ethernet_count = 0
        self.main_line_wifi_count = 0
        self.pov = 0
        self.t_name = 0
        self.t_ip = 0
        self.count_conn = -1
        self.count_soc = 0
        self.test_sock_count = 0
        self.main_link_test = 0
        # Счётчики дополнительных фреймов //M001
        self.count_page_2 = 0
        self.count_page = 0
        self.del_dop_line_ethernet = 0
        self.del_dop_line_wifi = 0
        # Счетчик на создание бака
        self.count_tank_creater = 0
        # Счетчик на создание аварии
        self.count_globalalarm_creater = 0
        # Счетчик на создание предупреждения
        self.count_attention_creater = 0
        # Счетчик на создание мотора
        self.count_engine_creater = 0
        # Счетчик на создание ламп
        self.count_lamp_creater = 0
        # Счётчик на создание контактора
        self.count_contact_creater = 0
        # Счётчик на создание концевого
        self.count_konc_creater = 0
        # Счётчик на создание реле
        self.count_rele_creater = 0
        # Счётчик на создание клапана
        self.count_valve_creater = 0

        self.comment_symv_number = 0

        self.tag_symv_number = 0
        # Счётчик кол-ва серверов
        self.server_data_count = 0

        # Объявление/инициализация пустых списков
        self.error = ''
        self.mist = []                                                                          # Пошли создание пустых массивов, в которых хранятся информация и новосозданных объектах данный массив - тег кнопки
        self.pidr = []                                                                          # Имя кнопки
        self.kordx = []                                                                         # Координата кнопки х
        self.kordy = []                                                                         # Координата кнопки у
        self.zap = []                                                                           # Данные с датчика, которые нужны тренду на координате y
        self.nowz = []                                                                          # Данные времени, которые нужны тренду на координате х
        self.prr = 0                                                                            # Для воссоздания ранее созданных кнопок, указывает ячейки координат для кнопок
        self.kordxl =[]
        self.kordyl = []
        self.textl =[]
        self.kordxs = []
        self.kordys = []
        self.nachs = []
        self.konchs = []
        self.kordxe = []
        self.kordye = []
        self.tage = []
        self.UNI_mass = []
        self.UNI_1_mass = []
        self.nano_mass = []
        self.mega_mass = []
        self.ethernet_mass = []
        self.server_mass = []
        self.UNI_kordx = []
        self.UNI_1_kordx = []
        self.nano_kordx = []
        self.mega_kordx = []
        self.ethernet_kordx = []
        self.server_kordx = []
        self.UNI_kordy = []
        self.UNI_1_kordy = []
        self.nano_kordy = []
        self.mega_kordy = []
        self.ethernet_kordy = []
        self.server_kordy = []
        self.dop_line_ethernet_mass = []
        self.dop_line_wifi_mass = []
        self.wid_line_ethernet_mass = []
        self.wid_line_wifi_mass = []
        self.line_tag = []
        self.line_tag_wifi = []
        self.ethernet_prov = []
        self.wifi_prov = []
        self.line_ethernet_kordy_mass = []
        self.line_wifi_kordy_mass = []
        self.test_mass = []
        self.test_mass2 = []
        self.test_sock = []
        self.test_table_mas=['uno2',3,1,' ']
        self.table_matrix = []
        self.matrix_table = []
        self.name_page = []
        self.dop_ethernet_x =[]
        self.dop_ethernet_y = []
        self.dop_wifi_x = []
        self.dop_wifi_y = []
        # Массивы на изображения бака
        self.tank_kordx = []
        self.tank_kordy = []
        self.id_image_tank = []
        self.tank_image = []
        # Массивы на изображение Аварии
        self.globalalarm_kordx = []
        self.globalalarm_kordy = []
        self.id_image_globalalarm = []
        self.globalalarm_image = []
        # Массивы на изображение Предупреждения
        self.attention_kordx = []
        self.attention_kordy = []
        self.id_image_attention = []
        self.attention_image = []
        # Массивы на изображение Мотора
        self.engine_kordx = []
        self.engine_kordy = []
        self.id_image_engine = []
        self.engine_image = []
        # Массивы на изображение лампочки
        self.lamp_kordx = []
        self.lamp_kordy = []
        self.id_image_lamp = []
        self.lamp_image = []
        # Массивы на изображение контактора
        self.contact_kordx = []
        self.contact_kordy = []
        self.id_image_contact = []
        self.contact_image = []
        # Массивы на изображение концевого
        self.konc_kordx = []
        self.konc_kordy = []
        self.id_image_konc = []
        self.konc_image = []
        # Массивы на изображение реле
        self.rele_kordx = []
        self.rele_kordy = []
        self.id_image_rele = []
        self.rele_image = []
        # массивы на изображение клапана
        self.valve_kordx = []
        self.valve_kordy = []
        self.id_image_valve = []
        self.valve_image = []
        # Массивы настроек уно вайфай "сети"
        self.name_uno_wifi = []
        self.ip_uno_wifi = []
        # Массивы настроек уно "сети"
        self.name_uno = []
        self.ip_uno = []
        # Массивы настроек нано "сети"
        self.name_nano = []
        self.ip_nano = []
        # Массивы настроек мега "сети"
        self.name_mega = []
        self.ip_mega = []
        
        self.id_image_main_win = []
        # Матрица данных с серверов
        self.result_tab = [[]]
        self.result_tab = self.result_tab*10

        self.comments_symv = ['','','','','','','','','','','','','','','','','','']

        self.tag_symv_tab = ['','','','','','','','','','','','','','','','','','']
        # Временные кнопки/ивенты/текстовой виджет событий //M008
        self.button = tkinter.Button(self.frame2,text = 'Включить сообщения', command = self.button_press) # Кнопка для активации постоянного обновления строки данных от клиента, далее будет работать сразу при старте сервера
        self.button.place(x=30, y=30)
        self.butard = tkinter.Button(self.canvas1,text = 'Загрузить Ардуино Уно', command = self.open_arduino_uno) # Кнопка для активации постоянного обновления строки данных от клиента, далее будет работать сразу при старте сервера
        self.butard.place(x=150, y=150)
        self.label2 =tkinter.Label(self.canvas1,background='#28444d',fg='white',width=(self.w-1645),justify=LEFT,text = self.result) # Контрольная метка главного потока и приема данных (self.w-1645)
        self.label2.place(x=0 ,y=(self.h/2)+473)
        self.tx_error = Text(self.frame2,font=('times',12),width = 6000,height = 10, wrap = WORD,bg = '#28444d',fg = 'white',state=tk.DISABLED)  # Текстовый виджет для сообщений ошибок,предупреждений и т.д. bd = 'black'
        self.tx_error.place (x=0,y=(self.h/2)+303)
        #self.line_tx_error = self.canvas.create_line(0,self.h-302,self.w,self.h-302,width=5,fill='#DEF7FE',border = 'black')
        self.tx_error.configure(state=tk.NORMAL)
        self.tx_error.insert(1.0,str(datetime.now())+': Запуск инициализации...\n')
        self.tx_error.configure(state=tk.DISABLED)
        self.canvas1.bind("<Button-3>",self.adddlist)                                           # Запускаем меню добавления
        self.canvas.bind('<Button-3>',self.adddlist2)
        self.now = datetime.now()                                                               # Узнаем текущее время и присваиваем переменной
        self.yu=0                                                                               # Хуй его знает зачем я это создал  
        self.button_press()
        self.canvas.bind_all('<B3-Motion>',self.moved1)
        self.window.bind_all("<B2-Motion>",self.confb)                                          # Говорим, что окно создано
        self.window.bind_all('<q>',self.deletew)
        self.canvas.bind_all('<q>',self.deletenet)
        self.window.bind_all('<Motion>',self.fff)
        self.frame2.bind_all('<Button-3>',self.menus)
        self.loadprog()
        self.test_server_main()
        self.window.mainloop()

    def administrate_on (self,event = None):
        self.tx_error.config(state=tk.NORMAL)
        self.tx_error.insert(1.0,str(datetime.now())+': Попытка входа пользователя..\n')
        self.tx_error.config(state=tk.DISABLED)
        adm.beging_on()
        
    def open_arduino_uno (self,event = None):
        o_a = os.startfile('ArduinoProj\ArduinoRAOKlient1.0.0.7\ArduinoRAOKlient1.0.0.7/ArduinoRAOKlient1.0.0.7.ino')  
    # Две функции смены полноэкранного режима //M001
    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
    # Окно добавления новых изображений вызываемый из основного меню //M005
    def win_inst (self,event = None):
        self.win_instr = tk.Toplevel(self.window)
        self.win_instr.iconbitmap('image//rao_inc.ico')
        self.win_instr.geometry("%dx%d+0+0" % (600, 600))
        self.inst_canvas=Canvas(self.win_instr,width=600,height=600,bg='#DEF7FE')
        self.inst_canvas.grid()
        self.in_image_1 = Image.open('image//tank_100.png')
        self.in_image_2 = Image.open('image//global_alarm.png')
        self.in_image_3 = Image.open('image//attention.png')
        self.in_image_4 = Image.open('image//engine_off.png')
        self.in_image_5 = Image.open('image//lamp_off.png')
        self.in_image_6 = Image.open('image//contact_off.png')
        self.in_image_7 = Image.open('image//konc_off.png')
        self.in_image_8 = Image.open('image//rele_off.png')
        self.in_image_9 = Image.open('image//valve_on.png')
        in_im_1 = ImageTk.PhotoImage(self.in_image_1)
        in_im_2 = ImageTk.PhotoImage(self.in_image_2)
        in_im_3 = ImageTk.PhotoImage(self.in_image_3)
        in_im_4 = ImageTk.PhotoImage(self.in_image_4)
        in_im_5 = ImageTk.PhotoImage(self.in_image_5)
        in_im_6 = ImageTk.PhotoImage(self.in_image_6)
        in_im_7 = ImageTk.PhotoImage(self.in_image_7)
        in_im_8 = ImageTk.PhotoImage(self.in_image_8)
        in_im_9 = ImageTk.PhotoImage(self.in_image_9)
        icon1 = Button(self.win_instr,image=in_im_1, relief=FLAT, bg = '#DEF7FE',command = self.create_win_tank)
        icon2 = Button(self.win_instr,image=in_im_2, relief=FLAT, bg = '#DEF7FE',command = self.create_win_globalalarm)
        icon3 = Button(self.win_instr,image=in_im_3, relief=FLAT, bg = '#DEF7FE',command = self.create_win_attention)
        icon4 = Button(self.win_instr,image=in_im_4, relief=FLAT, bg = '#DEF7FE',command = self.create_win_engine)
        icon5 = Button(self.win_instr,image=in_im_5, relief=FLAT, bg = '#DEF7FE',command = self.create_win_lamp)
        icon6 = Button(self.win_instr,image=in_im_6, relief=FLAT, bg = '#DEF7FE',command = self.create_win_contact)
        icon7 = Button(self.win_instr,image=in_im_7, relief=FLAT, bg = '#DEF7FE',command = self.create_win_konc)
        icon8 = Button(self.win_instr,image=in_im_8, relief=FLAT, bg = '#DEF7FE',command = self.create_win_rele)
        icon9 = Button(self.win_instr,image=in_im_9, relief=FLAT, bg = '#DEF7FE',command = self.create_win_valve)
        icon1.image = in_im_1
        icon2.image = in_im_2
        icon3.image = in_im_3
        icon4.image = in_im_4
        icon5.image = in_im_5
        icon6.image = in_im_6
        icon7.image = in_im_7
        icon8.image = in_im_8
        icon9.image = in_im_9
        icon1.place(x=15,y=120)
        icon2.place(x=200,y=20)
        icon3.place(x=20,y=20)
        icon4.place(x=400,y=20)
        icon5.place(x=400,y=120)
        icon6.place(x=500,y=120)
        icon7.place(x=500,y=220)
        icon8.place(x=500,y=320)
        icon9.place(x=500,y=420)
        print('pf')

    # Новое окно создания клапана //M006
    def create_win_valve(self,event = None):
        self.win_valve = tk.Toplevel(self.window)
        self.win_valve.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.win_valve,text='Имя')
        f_bot = LabelFrame(self.win_valve,text='Тег')
        label_valve = tk.Label(self.win_valve, text = "Новый контактор")
        name = tk.Label(f_top,text="Введите имя:")
        self.name_valve = tk.Entry(f_top,width=30)
        #name_2 = tk.Label(f_bot,text="Введите тег:")
        name_3  = tk.Label(f_bot,text='Выберите тег :')
        self.tag_valve = ttk.Combobox(f_bot,values = self.tag_symv_tab)
        button_valve = tk.Button(self.win_valve, text = "Создать",command = self.create_valve_init)

        f_top.pack(padx=10,pady=10)
        name.pack(side = LEFT,padx = 5, pady = 5)
        self.name_valve.pack(side = LEFT,padx = 5, pady = 5)
        f_bot.pack(padx=10,pady=10)
        #name_2.pack(side = LEFT,padx = 5, pady = 5)
        name_3.pack(side = LEFT,padx = 5, pady = 5)
        self.tag_valve.pack(side = LEFT,padx = 5, pady = 5)
        button_valve.pack(side = BOTTOM,padx = 5, pady = 5)
        label_valve.pack(side = BOTTOM,padx = 5, pady = 5)
        
    #Cоздания тегового изображения на основном окне реле //M006
    def create_valve_init(self):
        self.xex = self.window.winfo_pointerx ()                                            
        self.valve_kordx.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.valve_kordy.append(self.yey)
        self.valve_image.append(PhotoImage(file='image\\ссс.png'))
        self.id_image_main_win.append(self.canvas1.create_image(self.xex,self.yey,image=self.valve_image[self.count_valve_creater],tag=('valve'+str(self.count_valve_creater))))
        self.canvas1.tag_bind('valve'+str(self.count_valve_creater),'<Double-Button-1>',self.create_win_valve)
        self.count_valve_creater +=1
        print(self.count_valve_creater,'Кортеж - ',self.id_image_valve)        
        self.win_valve.destroy()


    # Новое окно создания реле //M006
    def create_win_rele(self,event = None):
        self.win_rele = tk.Toplevel(self.window)
        self.win_rele.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.win_rele,text='Имя')
        f_bot = LabelFrame(self.win_rele,text='Тег')
        label_rele = tk.Label(self.win_rele, text = "Новый контактор")
        name = tk.Label(f_top,text="Введите имя:")
        self.name_rele = tk.Entry(f_top,width=30)
        #name_2 = tk.Label(f_bot,text="Введите тег:")
        name_3  = tk.Label(f_bot,text='Выберите тег :')
        self.tag_rele = ttk.Combobox(f_bot,values = self.tag_symv_tab)
        button_rele = tk.Button(self.win_rele, text = "Создать",command = self.create_rele_init)

        f_top.pack(padx=10,pady=10)
        name.pack(side = LEFT,padx = 5, pady = 5)
        self.name_rele.pack(side = LEFT,padx = 5, pady = 5)
        f_bot.pack(padx=10,pady=10)
        #name_2.pack(side = LEFT,padx = 5, pady = 5)
        name_3.pack(side = LEFT,padx = 5, pady = 5)
        self.tag_rele.pack(side = LEFT,padx = 5, pady = 5)
        button_rele.pack(side = BOTTOM,padx = 5, pady = 5)
        label_rele.pack(side = BOTTOM,padx = 5, pady = 5)
        
    #Cоздания тегового изображения на основном окне реле //M006
    def create_rele_init(self):
        self.xex = self.window.winfo_pointerx ()                                            
        self.rele_kordx.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.rele_kordy.append(self.yey)
        self.rele_image.append(PhotoImage(file='image\\rele_off.png'))
        self.id_image_main_win.append(self.canvas1.create_image(self.xex,self.yey,image=self.rele_image[self.count_rele_creater],tag=('rele'+str(self.count_rele_creater))))
        self.canvas1.tag_bind('rele'+str(self.count_rele_creater),'<Double-Button-1>',self.create_win_rele)
        self.count_rele_creater +=1
        print(self.count_rele_creater,'Кортеж - ',self.id_image_rele)        
        self.win_rele.destroy()

    # Новое окно создания концевого //M006
    def create_win_konc(self,event = None):
        self.win_konc = tk.Toplevel(self.window)
        self.win_konc.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.win_konc,text='Имя')
        f_bot = LabelFrame(self.win_konc,text='Тег')
        label_konc = tk.Label(self.win_konc, text = "Новый контактор")
        name = tk.Label(f_top,text="Введите имя:")
        self.name_konc = tk.Entry(f_top,width=30)
        #name_2 = tk.Label(f_bot,text="Введите тег:")
        name_3  = tk.Label(f_bot,text='Выберите тег :')
        self.tag_konc = ttk.Combobox(f_bot,values = self.tag_symv_tab)
        button_konc = tk.Button(self.win_konc, text = "Создать",command = self.create_konc_init)

        f_top.pack(padx=10,pady=10)
        name.pack(side = LEFT,padx = 5, pady = 5)
        self.name_konc.pack(side = LEFT,padx = 5, pady = 5)
        f_bot.pack(padx=10,pady=10)
        #name_2.pack(side = LEFT,padx = 5, pady = 5)
        name_3.pack(side = LEFT,padx = 5, pady = 5)
        self.tag_konc.pack(side = LEFT,padx = 5, pady = 5)
        button_konc.pack(side = BOTTOM,padx = 5, pady = 5)
        label_konc.pack(side = BOTTOM,padx = 5, pady = 5)
        
    #Cоздания тегового изображения на основном окне концевого //M006
    def create_konc_init(self):
        self.xex = self.window.winfo_pointerx ()                                            
        self.konc_kordx.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.konc_kordy.append(self.yey)
        self.konc_image.append(PhotoImage(file='image\\konc_off.png'))
        self.id_image_main_win.append(self.canvas1.create_image(self.xex,self.yey,image=self.konc_image[self.count_konc_creater],tag=('konc'+str(self.count_konc_creater))))
        self.canvas1.tag_bind('konc'+str(self.count_konc_creater),'<Double-Button-1>',self.create_win_konc)
        self.count_konc_creater +=1
        print(self.count_konc_creater,'Кортеж - ',self.id_image_konc)        
        self.win_konc.destroy()
    
        
    # Новое окно создания контактора //M006
    def create_win_contact(self,event = None):
        self.win_contact = tk.Toplevel(self.window)
        self.win_contact.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.win_contact,text='Имя')
        f_bot = LabelFrame(self.win_contact,text='Тег')
        label_contact = tk.Label(self.win_contact, text = "Новый контактор")
        name = tk.Label(f_top,text="Введите имя:")
        self.name_contact = tk.Entry(f_top,width=30)
        #name_2 = tk.Label(f_bot,text="Введите тег:")
        name_3  = tk.Label(f_bot,text='Выберите тег :')
        self.tag_contact = ttk.Combobox(f_bot,values = self.tag_symv_tab)
        button_contact = tk.Button(self.win_contact, text = "Создать",command = self.create_contact_init)

        f_top.pack(padx=10,pady=10)
        name.pack(side = LEFT,padx = 5, pady = 5)
        self.name_contact.pack(side = LEFT,padx = 5, pady = 5)
        f_bot.pack(padx=10,pady=10)
        #name_2.pack(side = LEFT,padx = 5, pady = 5)
        name_3.pack(side = LEFT,padx = 5, pady = 5)
        self.tag_contact.pack(side = LEFT,padx = 5, pady = 5)
        button_contact.pack(side = BOTTOM,padx = 5, pady = 5)
        label_contact.pack(side = BOTTOM,padx = 5, pady = 5)
        
    #Cоздания тегового изображения на основном окне контакта //M006
    def create_contact_init(self):
        self.xex = self.window.winfo_pointerx ()                                            
        self.contact_kordx.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.contact_kordy.append(self.yey)
        self.contact_image.append(PhotoImage(file='image\\contact_off.png'))
        self.id_image_main_win.append(self.canvas1.create_image(self.xex,self.yey,image=self.contact_image[self.count_contact_creater],tag=('contact'+str(self.count_contact_creater))))
        self.canvas1.tag_bind('contact'+str(self.count_contact_creater),'<Double-Button-1>',self.create_win_contact)
        self.count_contact_creater +=1
        print(self.count_contact_creater,'Кортеж - ',self.id_image_contact)        
        self.win_contact.destroy()
    
        
    # Новое окно создания бака //M006
    def create_win_tank(self,event = None):
        self.win_tank = tk.Toplevel(self.window)
        self.win_tank.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.win_tank,text='Имя')
        f_bot = LabelFrame(self.win_tank,text='Тег')
        label_tank = tk.Label(self.win_tank, text = "Новый бак")
        name = tk.Label(f_top,text="Введите имя:")
        self.name_tank = tk.Entry(f_top,width=30)
        #name_2 = tk.Label(f_bot,text="Введите тег:")
        name_3  = tk.Label(f_bot,text='Выберите тег :')
        self.tag_tank = ttk.Combobox(f_bot,values = self.tag_symv_tab)
        button_tank = tk.Button(self.win_tank, text = "Создать",command = self.create_tank_init)

        f_top.pack(padx=10,pady=10)
        name.pack(side = LEFT,padx = 5, pady = 5)
        self.name_tank.pack(side = LEFT,padx = 5, pady = 5)
        f_bot.pack(padx=10,pady=10)
        #name_2.pack(side = LEFT,padx = 5, pady = 5)
        name_3.pack(side = LEFT,padx = 5, pady = 5)
        self.tag_tank.pack(side = LEFT,padx = 5, pady = 5)
        button_tank.pack(side = BOTTOM,padx = 5, pady = 5)
        label_tank.pack(side = BOTTOM,padx = 5, pady = 5)
        
    #Cоздания тегового изображения на основном окне бака //M006
    def create_tank_init(self):
        self.xex = self.window.winfo_pointerx ()                                            
        self.tank_kordx.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.tank_kordy.append(self.yey)
        self.tank_image.append(PhotoImage(file='image\\tank_0.png'))
        self.id_image_main_win.append(self.canvas1.create_image(self.xex,self.yey,image=self.tank_image[self.count_tank_creater],tag=('tank'+str(self.count_tank_creater))))
        self.canvas1.tag_bind('tank'+str(self.count_tank_creater),'<Double-Button-1>',self.create_win_tank)
        self.count_tank_creater +=1
        print(self.count_tank_creater,'Кортеж - ',self.id_image_tank)        
        self.win_tank.destroy()
        
    # Новое окно создания аварии ТЕСТЫ //M006
    def create_win_globalalarm(self, event = None):
        self.win_globalalarm = tk.Toplevel(self.window)
        self.win_globalalarm.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.win_globalalarm,text='Имя')
        f_bot = LabelFrame(self.win_globalalarm,text='Тег')        
        label_globalalarm = tk.Label(self.win_globalalarm, text = "Новый аварийный сигнал")
        name = tk.Label(f_top,text="Введите имя:")
        self.name_globalalarm = tk.Entry(f_top,width=30)
        name_2 = tk.Label(f_bot,text="Выберете тег:")
        self.tag_globalalarm = ttk.Combobox(f_bot,values = self.tag_symv_tab)
        button_globalalarm = tk.Button(self.win_globalalarm, text = "Создать",command = self.create_globalalarm_init)

        f_top.pack(padx=10,pady=10)
        name.pack(side = LEFT,padx = 5, pady = 5)                                                                             
        self.name_globalalarm.pack(side = LEFT,padx = 5, pady = 5)

        f_bot.pack(padx=10,pady=10)
        name_2.pack(side = LEFT,padx = 5, pady = 5)
        self.tag_globalalarm.pack(side = LEFT,padx = 5, pady = 5)
        label_globalalarm.pack(padx = 5, pady = 5)
        button_globalalarm.pack()
    # Создание тегового изображения на основном окне аварии //M006
    def create_globalalarm_init(self):
        self.xex = self.window.winfo_pointerx ()                                            
        self.globalalarm_kordx.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.globalalarm_kordy.append(self.yey)
        self.globalalarm_image.append(PhotoImage(file='image\\global_alarm.png'))
        self.id_image_main_win.append(self.canvas1.create_image(self.xex,self.yey,image=self.globalalarm_image[self.count_globalalarm_creater],tag=('globalalarm'+str(self.count_globalalarm_creater))))
        self.canvas1.tag_bind('globalalarm'+str(self.count_globalalarm_creater),'<Double-Button-1>',self.create_win_globalalarm)
        self.count_globalalarm_creater +=1
        print(self.count_globalalarm_creater,'Кортеж - ',self.id_image_globalalarm)        
        self.win_globalalarm.destroy()
            
    # Новое окно создания предупреждения //M006
    def create_win_attention(self,event = None):
        self.win_attention = tk.Toplevel(self.window)
        self.win_attention.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.win_attention,text='Имя')
        f_bot = LabelFrame(self.win_attention,text='Тег')
        
        label_attention = tk.Label(self.win_attention, text = "Новый сигнал опастности")
        name = tk.Label(f_top,text="Введите имя:")
        self.name_attention = tk.Entry(f_top,width=30)
        name_2 = tk.Label(f_bot,text="Введите тег:")
        self.tag_attention = ttk.Combobox(f_bot,values = self.tag_symv_tab)
        button_attention = tk.Button(self.win_attention, text = "Создать",command = self.create_attention_init)
        
        f_top.pack(padx=10,pady=10)
        name.pack(side = LEFT,padx = 5, pady = 5)                                                                             
        self.name_attention.pack(side = LEFT,padx = 5, pady = 5)
        
        f_bot.pack(padx=10,pady=10)
        name_2.pack(side = LEFT,padx = 5, pady = 5)
        self.tag_attention.pack(side = LEFT,padx = 5, pady = 5)
        label_attention.pack(padx = 5, pady = 5)
        button_attention.pack()
        
    # Создание тегового изображения на основном окне предупреждения //M006
    def create_attention_init(self):
        self.win_attention.destroy()
        self.xex = self.window.winfo_pointerx ()                                            
        self.attention_kordx.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.attention_kordy.append(self.yey)
        self.attention_image.append(PhotoImage(file='image\\attention.png'))
        tag_attention = ('attention'+str(self.count_attention_creater))
        self.id_image_main_win.append(self.canvas1.create_image(self.xex,self.yey,image=self.attention_image[self.count_attention_creater],tag=str(tag_attention)))#str(tag_attention)))
        self.canvas1.tag_bind(str(tag_attention),'<Double-Button-1>',self.create_win_attention)
        self.count_attention_creater +=1
        print(tag_attention)
        print(self.count_attention_creater,'Кортеж - ',self.id_image_attention)        
        #self.win_attention.destroy()
        
    # Новое окно создания мотора //M006
    def create_win_engine(self,event = None):
        self.win_engine = tk.Toplevel(self.window)
        self.win_engine.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.win_engine,text='Имя')
        f_bot = LabelFrame(self.win_engine,text='Тег')
        
        label_engine = tk.Label(self.win_engine, text = "Новый двигатель")
        name = tk.Label(f_top,text="Введите имя:")
        self.name_engine = tk.Entry(f_top,width=30)
        name_2 = tk.Label(f_bot,text="Введите тег:")
        self.tag_engine = ttk.Combobox(f_bot,values = self.tag_symv_tab)
        button_engine = tk.Button(self.win_engine, text = "Создать", command = self.create_engine_init)

        f_top.pack(padx=10,pady=10)
        name.pack(side = LEFT,padx = 5, pady = 5)                                                                             
        self.name_engine.pack(side = LEFT,padx = 5, pady = 5)

        f_bot.pack(padx=10,pady=10)
        name_2.pack(side = LEFT,padx = 5, pady = 5)
        self.tag_engine.pack(side = LEFT,padx = 5, pady = 5)
        label_engine.pack(padx = 5, pady = 5)
        button_engine.pack()
    # Создание тегового изображения на основном окне мотора //M006
    def create_engine_init(self):
        self.xex = self.window.winfo_pointerx ()                                            
        self.engine_kordx.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.engine_kordy.append(self.yey)
        self.engine_image.append(PhotoImage(file='image\\engine_off.png'))
        self.id_image_main_win.append(self.canvas1.create_image(self.xex,self.yey,image=self.engine_image[self.count_engine_creater],tag=('engine'+str(self.count_engine_creater))))
        self.canvas1.tag_bind('engine'+str(self.count_engine_creater),'<Double-Button-1>',self.create_win_engine)
        self.count_engine_creater +=1
        print(self.count_engine_creater,'Кортеж - ',self.id_image_engine)        
        self.win_engine.destroy()
    # Лампочка //M006
    def create_win_lamp(self,event = None):
        self.win_lamp = tk.Toplevel(self.window)
        self.win_lamp.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.win_lamp,text='Имя')
        f_bot = LabelFrame(self.win_lamp,text='Тег')
        
        label_lamp = tk.Label(self.win_lamp, text = "Новая лампочка")
        name = tk.Label(f_top,text="Введите имя:")
        self.name_lamp = tk.Entry(f_top,width=30)
        name_2 = tk.Label(f_bot,text="Введите тег:")
        self.tag_lamp = ttk.Combobox(f_bot,values = self.tag_symv_tab) 
        button_lamp = tk.Button(self.win_lamp, text = "Создать", command = self.create_lamp_init)

        f_top.pack(padx=10,pady=10)
        name.pack(side = LEFT,padx = 5, pady = 5)                                                                             
        self.name_lamp.pack(side = LEFT,padx = 5, pady = 5)
        
        f_bot.pack(padx=10,pady=10)
        name_2.pack(side = LEFT,padx = 5, pady = 5)
        self.tag_lamp.pack(side = LEFT,padx = 5, pady = 5)
        label_lamp.pack(padx = 5, pady = 5)
        button_lamp.pack()
    # Создание тегового изображения на основном окне лампочки //M006
    def create_lamp_init(self):
        self.xex = self.window.winfo_pointerx ()                                            
        self.lamp_kordx.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.lamp_kordy.append(self.yey)
        self.lamp_image.append(PhotoImage(file='image\\lamp_off.png'))
        self.id_image_main_win.append(self.canvas1.create_image(self.xex,self.yey,image=self.lamp_image[self.count_lamp_creater],tag=('lamp'+str(self.count_lamp_creater))))
        self.canvas1.tag_bind('lamp'+str(self.count_lamp_creater),'<Double-Button-1>',self.create_win_lamp)
        self.count_lamp_creater +=1
        print(self.count_lamp_creater,'Кортеж - ',self.id_image_lamp)        
        self.win_lamp.destroy()
        
    # Воссоздание доп.линий езернет//M206//M208
    def re_dop_line_ethernet (self,event = None):
        self.pov = self.iuw+self.iu+self.iun+self.ium+self.iue+self.ius
        #self.ethernet_prov = self.ethernet_prov*self.pov
        print ('self.ethernet_prov :',self.ethernet_prov)
        print('ПРОБУЮ')
        y = 0
        for y in range(self.dop_line_ethernet_count):
            print('skras')
            self.dop_line_ethernet_mass.append(self.canvas.create_line(self.dop_ethernet_x[y],self.line_ethernet_kordy_mass[0],self.dop_ethernet_x[y],self.dop_ethernet_y[y],width=3,tag=str(self.line_tag[y]),fill='#2F4F4F')) 
            y +=1
    # Воссоздание дополнительных линий вай фай//M206//M208
    def re_dop_line_wifi (self,event = None):
        self.pov = self.iuw+self.iu+self.iun+self.ium+self.iue+self.ius
        #self.wifi_prov = self.wifi_prov*self.pov
        print ('self.ethernet_prov :',self.wifi_prov)
        #self.wifi_prov = self.wifi_prov*self.pov
        print('ПРОБУЮ')
        y = 0
        for y in range(self.dop_line_wifi_count):
            print('skras')
            self.dop_line_wifi_mass.append(self.canvas.create_line(self.dop_wifi_x[y],self.line_wifi_kordy_mass[0],self.dop_wifi_x[y],self.dop_wifi_y[y],width=3,tag=str(self.line_tag_wifi[y]),fill='#E9967A')) 
            y +=1

    def add_new_page (self,event = None):#
        
        self.newWindow_9 = tk.Toplevel(self.window)                                               
        labelExample = tk.Label(self.newWindow_9, text = "Новая страница")
        namm = tk.Label(self.newWindow_9,text="Имя:")
        self.show= tk.Entry(self.newWindow_9,width=30)
        buttonExample = tk.Button(self.newWindow_9, text = "Создать",command = self.add_new_page_part_2)
        namm.pack()                                                                             
        self.show.pack()
        labelExample.pack()
        buttonExample.pack()
      

    def add_new_page_part_2 (self,event = None):#   
        self.name_page_str = self.show.get()
        self.frameN = ttk.Frame(self.notebook)#
        self.notebook.add(self.frameN,text= str(self.name_page_str))# self.www[self.count]
        self.canvasN=Canvas(self.frameN,width=self.w,height=self.h,bg='#DEF7FE')#
        self.canvasN.grid()#
        self.count_page += 1
        self.name_page.append(self.name_page_str)
        self.newWindow_9.destroy()
        

    def re_page_part_3 (self,event = None):#   
        while self.count_page_2 <= self.count_page-1:
            self.frameN = ttk.Frame(self.notebook)#
            self.notebook.add(self.frameN,text= self.name_page[self.count_page_2])# self.www[self.count]
            self.canvasN=Canvas(self.frameN,width=self.w,height=self.h,bg='#DEF7FE')#
            self.canvasN.grid()#
            self.count_page_2 += 1
        self.re_dop_line_ethernet()

# Тесты с изображениями и конвертацией//M000
    def conversion (self,evebt = None):
        b = str(self.testing_conv[14])+str(self.testing_conv[15])+str(self.testing_conv[16])
        print(b)
        if 220 >= int(b) <= 255:
            self.lvl_image = PhotoImage(file='image\\tank_100.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
        if 190 >= int(b) <= 220:
            self.lvl_image = PhotoImage(file='image\\tank_90.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
        if 150 >= int(b) <= 190:
            self.lvl_image = PhotoImage(file='image\\tank_80.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
        if 130 >= int(b) <= 150:
            self.lvl_image = PhotoImage(file='image\\tank_70.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
        if 100 >= int(b) <= 130:
            self.lvl_image = PhotoImage(file='image\\tank_60.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
        if 80 >= int(b) <= 100:
            self.lvl_image = PhotoImage(file='image\\tank_50.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
        if 60 >= int(b) <= 80:
            self.lvl_image = PhotoImage(file='image\\tank_40.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
        if 40 >= int(b) <= 60:
            self.lvl_image = PhotoImage(file='image\\tank_30.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
        if 20 >= int(b) <= 40:
            self.lvl_image = PhotoImage(file='image\\tank_20.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
        if 0 > int(b) <= 20:
            self.lvl_image = PhotoImage(file='image\\tank_10.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
        if int(b) == 0:
            self.lvl_image = PhotoImage(file='image\\tank_empty.png')
            self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
    #//M203
    def addfuntrd_training (self,event = None):
            self.th_training = threading.Thread(target = self.table_symv)
            self.th_training.start()
    #//M203
    def addfuntrd_training_1 (self,event = None):
            self.th_training_1 = threading.Thread(target = self.training_table_mas)
            self.th_training_1.start()

    # Подготовка матрицы для символьной таблице//M500 
    def training_table_mas (self):
        while True:
            self.testing_conv = a = regex.findall(r'\X', str(self.result)) # конвертируем пакет в int
            mas = [a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],(a[14],a[15],a[16]),(a[17],a[18],a[19]),(a[20],a[21],a[22]),(a[23],a[24],a[25]),(a[26],a[27],a[28]),(a[29],a[30],a[31])] # Формируем массив таблицы из результата сервера
            count = len(mas)
            count_1 = 0
            mas_1 = ['']
            for count_1 in range(count):
                mas_1 = mas[count_1]
                self.matrix_table.append([(a[50],a[51],a[52]),'1.'+str(count_1),mas_1,self.tag_symv_tab[count_1],self.comments_symv[count_1]])
                count_1 +=1
            b = str(self.testing_conv[14])+str(self.testing_conv[15])+str(self.testing_conv[16])
            inter = ((1/1023)*(int(b)+1))*100 # шкалирование от 0 до 100
            #print(inter)
            
            if 90 <= inter or inter >=100:
                    self.lvl_image = PhotoImage(file='image\\tank_100.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            if 80 <= inter <=90:
                    self.lvl_image = PhotoImage(file='image\\tank_90.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            if 70 <= inter <=80:
                    self.lvl_image = PhotoImage(file='image\\tank_80.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            if 60 <= inter <=70:
                    self.lvl_image = PhotoImage(file='image\\tank_70.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            if 50 <= inter <=60:
                    self.lvl_image = PhotoImage(file='image\\tank_60.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            if 40 <= inter <=50:
                    self.lvl_image = PhotoImage(file='image\\tank_50.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            if 30 <= inter <=40:
                    self.lvl_image = PhotoImage(file='image\\tank_40.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            if 20 <= inter <=30:
                    self.lvl_image = PhotoImage(file='image\\tank_30.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            if 10 <= inter <=20:
                    self.lvl_image = PhotoImage(file='image\\tank_20.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            if 0 <= inter <=10:
                    self.lvl_image = PhotoImage(file='image\\tank_10.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            if inter ==0:
                    self.lvl_image = PhotoImage(file='image\\tank_0.png')
                    self.water_lvl = self.canvas1.create_image(150,150,anchor=NW,image =self.lvl_image)
            time.sleep(0.1)
            self.matrix_table.clear()
        #self.table_symv()

# Таблица символов//M500 
    def table_symv (self,parent=None):
        root = tk.Toplevel(self.window)
        root.iconbitmap('image//rao_inc.ico')
        root.title('Таблица символов')
        headings=('Имя контроллера', 'Номер контакта', 'Значение','Тег','Комментарий')
        self.table = ttk.Treeview(root, show="headings", selectmode="browse")
        self.table["columns"]=headings
        self.table["displaycolumns"]=headings
        for head in headings:
            self.table.heading(head, text=head, anchor=tk.CENTER)
            self.table.column(head, anchor=tk.CENTER)

        for row in self.matrix_table:
            
            self.table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(root, command=self.table.yview)
        self.table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(expand=tk.YES, fill=tk.BOTH)
        self.table.bind('<Button-3>',self.add_list_symv)
        self.th_table_symv = threading.Thread(target = self.table_tr)
        self.th_table_symv.start()
                    
    def table_tr (self):
        while True:
            x = self.table.get_children()
            for item,rows in zip(x,self.matrix_table): 
                self.table.item(item, values=tuple(rows))
            time.sleep(0.1)
# Добавление новых коментариев в символьную таблицу//M500 
    def edit_comment_symv(self,event = None):
        foor = self.table.focus()
        print(foor)
        t = str(foor)
        t = t.replace('I00','')
        t = t.replace('I0','')
        print(t)
        if t == '':
            t = '0'
        else: d = int(t,16)
        self.comment_symv_number = d -1
        print(d)
        self.new_window = tk.Toplevel(self.window)
        self.new_window.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.new_window,text='Имя')
        f_bot = LabelFrame(self.new_window,text='Текст')  
        labelExample = tk.Label(self.new_window, text = "Редактировать")
        namm = tk.Label(f_bot,text="Введите комментарий:")
        self.show10 = tk.Entry(f_bot,width=30)
        buttonExample1 = tk.Button(self.new_window, text = "Принять",command = self.edit_fin_comment)
        f_bot.pack(padx=10,pady=10)
        namm.pack(side = LEFT,padx = 5, pady = 5)                                                                          
        self.show10.pack(side = LEFT,padx = 5, pady = 5)
        labelExample.pack(padx = 5, pady = 5)
        buttonExample1.pack()

    def edit_fin_comment (self,event = None):
        q = self.show10.get()
        self.comments_symv[self.comment_symv_number] = q
        self.new_window.destroy()
        
# Интересная попытка добавления, оставлю пока что            
        #for selection in self.table.selection():
        #    poor = self.table.item(selection)
        #    pop,pip,pup = poor["values"][0:3]
        #    text = "Выбор: {}, {} <{}>"
        #    piir = [pop,pip,pup]
        #    piir.append('pizdec')
        #    print(piir)
        #    self.table.item(foor, values=piir)
            #print(text.format(last_name, first_name, email))
        #print(poor)
    # Добавление новых тегов в таблицу символов,слудющая функция - продолжение //M500        
    def edit_tag_symv(self,event = None):
        foor = self.table.focus()
        print(foor)
        t = str(foor)
        t = t.replace('I00','')
        t = t.replace('I0','')
        print(t)
        if t == '':
            t = '0'
        else: d = int(t,16)
        self.tag_symv_number = d -1
        print(d)
        self.new_window = tk.Toplevel(self.window)
        self.new_window.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.new_window,text='Имя')
        f_bot = LabelFrame(self.new_window,text='Текст')  
        labelExample = tk.Label(self.new_window, text = "Редактировать")
        namm = tk.Label(f_bot,text="Введите тег:")
        self.show11 = tk.Entry(f_bot,width=30)
        buttonExample1 = tk.Button(self.new_window, text = "Принять",command = self.edit_fin_tag)
        f_bot.pack(padx=10,pady=10)
        namm.pack(side = LEFT,padx = 5, pady = 5)                                                                          
        self.show11.pack(side = LEFT,padx = 5, pady = 5)
        labelExample.pack(padx = 5, pady = 5)
        buttonExample1.pack()

    def edit_fin_tag (self,event = None):
        q = self.show11.get()
        self.tag_symv_tab[self.tag_symv_number] = q
        self.new_window.destroy()
#Меню таблицу//M002
    def add_list_symv (self,event = None):
        print('Меню символьной таблицы')
        self.add_menu3 = Menu(tearoff = 0)
        #self.add_menu3.add_command (label = self.redk, command = self.blocked)
        self.add_menu3.add_command (label = 'Редактировать тег', command = self.edit_tag_symv)
        self.add_menu3.add_command (label = 'Редактировать комментарий', command = self.edit_comment_symv)
        self.menu_list_symv()

# Вызов меню символьной таблицы по координате//M002
    def menu_list_symv(self):
        global xex
        global yey
        self.xex = self.window.winfo_pointerx()
        self.yey = self.window.winfo_pointery()
        self.add_menu3.post(self.xex,self.yey)
        
# Основной и первый компьютер //M201
    def test_server_main (self):

        self.server_obj_main = PhotoImage(file='image\\server.png')
        self.id_img1 = self.canvas.create_image(((self.w/2)-80),75,image=self.server_obj_main,tag='mainserver')
        self.canvas.tag_bind('mainserver','<Double-Button-1>',self.server_win)

# Имя и ip сервера        //M201
    def test_ip (self):
        self.t_name = socket.getfqdn()
        print(self.t_name)
        self.t_ip = socket.gethostbyname(socket.getfqdn())
        print (self.t_ip)

# Создание окна сервера//M210
    def server_win (self,event):
        self.serverwindow = tk.Toplevel(self.window)
        self.serverwindow.iconbitmap('image//rao_inc.ico')# Иконка в углу окна
        self.win_server_can = Canvas(self.serverwindow,width=450,height=600,bg='#DEF7FE')
        self.win_server_can.grid()
        self.t_name = socket.getfqdn()
        print(self.t_name)
        self.t_ip = socket.gethostbyname(socket.getfqdn()) # Получаем имя и ip хоста
        print (self.t_ip)
        self.label_host =tkinter.Label(self.win_server_can,background='#DEF7FE',fg='black',justify=LEFT,text = ('Host : ',self.t_name),font = 'Arial 16')
        self.label_host.place(x= 25,y = 100)
        self.win_server_can.create_line(28,135,300,135,width=2,fill = 'black')
        self.label_ip = tkinter.Label(self.win_server_can,background='#DEF7FE',fg='black',justify=LEFT,text = ('IP server : ',self.t_ip),font = 'Arial 16')
        self.label_ip.place(x = 25,y = 170)
        self.button_diagnostic = tkinter.Button(self.win_server_can,text = 'Диагностика')
        self.button_diagnostic.place(x = 100,y = 450)
        self.button_ip_actual = tkinter.Button(self.win_server_can,text = 'Активные сети')
        self.button_ip_actual.place(x = 270, y = 450)
        self.btn = Button(self.win_server_can, text="Включить сервер",command=lambda: threading.Thread(target=self.raos, daemon=True).start()) # Кнопка запуска сервера сделана через тред, чтобы окно тКинтера не висло при бесконечном цикле
        self.btn.place(x = 170,y = 540)
        if self.main_link_test == 1 :
            self.btn.config(bg='green')
        else :
            self.btn.config(bg='grey95')
        self.button = tkinter.Button(self.win_server_can,text = 'Включить сообщения', command = self.button_press) # Кнопка для активации постоянного обновления строки данных от клиента, далее будет работать сразу при старте сервера
        self.win_server_can.create_line(28,205,300,205,width=2,fill = 'black')

# Создание окна контроллера уно //M210
    def UNO_win (self,event = None):
        self.unowindow = tk.Toplevel(self.window)
        self.unowindow.iconbitmap('image//rao_inc.ico')
        self.win_uno_can = Canvas(self.unowindow,width=450,height=600,bg='#DEF7FE')
        self.win_uno_can.grid()
        self.UNO_obj = PhotoImage(file="image\\UNO.png")   
        self.circle2 = self.win_uno_can.create_oval(375,450,385,460,fill='red')
        self.circle3 = self.win_uno_can.create_oval(375,445,385,435,fill='red')
        self.circle4 = self.win_uno_can.create_oval(375,430,385,420,fill='red')
        self.circle5 = self.win_uno_can.create_oval(375,415,385,405,fill='red')
        self.circle6 = self.win_uno_can.create_oval(375,400,385,390,fill='red')
        self.circle7 = self.win_uno_can.create_oval(375,385,385,375,fill='red')
        self.circle8 = self.win_uno_can.create_oval(375,360,385,350,fill='red')
        self.circle9 = self.win_uno_can.create_oval(375,345,385,335,fill='red')
        self.circle10 = self.win_uno_can.create_oval(375,330,385,320,fill='red')
        self.circle11 = self.win_uno_can.create_oval(375,315,385,305,fill='red')
        self.circle12 = self.win_uno_can.create_oval(375,300,385,290,fill='red')
        self.circle13 = self.win_uno_can.create_oval(375,285,385,275,fill='red')
        self.img_uno = self.win_uno_can.create_image(50,50,anchor=NW,image=self.UNO_obj)
    # Меню добавления/удаления ethernet/wifi доп. линий //M002
    def menulist4 (self):
        global xex
        global yey
        self.xex = self.window.winfo_pointerx()
        self.yey = self.window.winfo_pointery()
        self.addmenus.post(self.xex,self.yey)
    #//M002
    def menus (self,event = None):
        if self.papi == 0:
            h = str(self.num_widget)
            h = h.replace('.!notebook.!frame2.!canvas.!canvas','')
            if h == '':
                h = '0'
            else : h = int(h)-1
            if int(h) >= 0:
                print ('выполнил условие')
                self.addmenus = Menu(tearoff = 0)
                self.addmenus.add_command (label='Добавить к сети ethernet', command = self.line_dop_ethernet)
                self.addmenus.add_command (label='Добавить к сети wifi',command = self.line_dop_wifi)
                self.addmenus.add_command (label='Удалить с сети ethernet', command = self.delete_dop_line_ethernet)
                self.addmenus.add_command (label='Удалить с сети wifi', command = self.delete_dop_line_wifi)
                self.menulist4()
# Удаление доп.езернет линий//M206//M209  
    def delete_dop_line_ethernet (self,event = None):
        ez = str(self.num_widget)
        ez = ez.replace('.!notebook.!frame2.!canvas.!canvas','')
        if ez == '':
            ez = 0
        else : ez = int(ez)-1
        print(ez,'- намер езернет',self.num_widget,'- реальное')
        self.canvas.delete(self.dop_line_ethernet_mass[ez])
        self.ethernet_prov[ez] = 0
        self.wid_line_ethernet_mass[ez] = '-'
        self.line_tag[ez] = '-'
        self.dop_ethernet_x[ez] = '-'
        self.dop_ethernet_y[ez] = '-'
        self.dop_line_ethernet_count = self.dop_line_ethernet_count - 1
        self.del_dop_line_ethernet +=1
        #self.dop_line_ethernet_mass[ez] = '-'
        

        
# Удаление доп.вайфай линий  //M206//M209      
    def delete_dop_line_wifi (self,event = None):
        wf = str(self.num_widget)
        wf = wf.replace('.!notebook.!frame2.!canvas.!canvas','')
        if wf == '':
            wf = 0
        else : wf = int(wf)-1
        print(wf,'- номер езернет',self.num_widget,'- реальное')
        self.canvas.delete(self.dop_line_wifi_mass[wf])
        self.wifi_prov[wf] = 0
        self.wid_line_wifi_mass[wf] = '-'
        self.line_tage_wifi[wf] = '-'
        self.dop_wifi_x[wf] = '-'
        self.dop_wifi_y[wf] = '-'
        self.dop_line_wifi_count = self.dop_line_wifi_count - 1
        self.del_dop_line_wifi +=1
        #self.dop_line_wifi_mass[wf] = '-'
        
        
# Создание дополнительных езернет линий//M206//M208
    def line_dop_ethernet (self,event = None):
        self.confx = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        self.confy = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()         
        tag_dop_line = 'dug'+str(self.dop_line_ethernet_count)
        self.dop_line_ethernet_mass.append(self.canvas.create_line(self.confx,self.line_ethernet_kordy,self.confx,self.confy,width=3,tag=str(tag_dop_line),fill='#2F4F4F')) #tag=str(self.dop_line_ethernet_count)
        self.dop_ethernet_x.append(self.confx)
        self.dop_ethernet_y.append(self.confy)
        print(tag_dop_line)
        print(self.dop_line_ethernet_mass)
        d = str(self.num_widget)
        d = d.replace('.!notebook.!frame2.!canvas.!canvas','')
        if d == '':
            d = 0
        else : d = int(d)-1
        self.num_line_ethernet = d
        print('я вижу канвас',d)
        print(self.num_line_ethernet)
        self.line_tag.append(tag_dop_line)
        self.wid_line_ethernet_mass.append(self.num_line_ethernet)
        self.ethernet_prov[d] = 1
        self.dop_line_ethernet_count +=1
# Создание дополнительных вайфай линий //M206//M208       
    def line_dop_wifi (self):
        self.confx = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        self.confy = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()            
        tag_dop_line = 'pug'+str(self.dop_line_wifi_count)
        self.dop_line_wifi_mass.append(self.canvas.create_line(self.confx,self.line_wifi_kordy,self.confx,self.confy,width=3,tag=str(tag_dop_line),fill='#E9967A'))
        self.dop_wifi_x.append(self.confx)
        self.dop_wifi_y.append(self.confy)
        t = str(self.num_widget)
        t = t.replace('.!notebook.!frame2.!canvas.!canvas','')
        if t == '':
            t = 0
        else: t = int(t)-1
        self.num_line_wifi = t
        self.line_tag_wifi.append(tag_dop_line)
        self.wid_line_wifi_mass.append(self.num_line_wifi)
        self.wifi_prov[t] = 1
        self.dop_line_wifi_count +=1
# Создание основного езернет канала  //M206//M208  
    def line_ethernet (self):
        self.confx = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        self.confy = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        self.canvas.create_line(0,self.confy,self.w,self.confy,tag='bich',width=5,fill = '#2F4F4F')
        self.line_ethernet_kordy = self.confy
        self.line_ethernet_kordy_mass.append(self.line_ethernet_kordy)
        self.main_line_ethernet_count +=1
# Создаие основного вай фай канала//M206//M208
    def line_wifi (self):
        self.confx = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        self.confy = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        self.canvas.create_line(0,self.confy,self.w,self.confy,width=5,fill = '#E9967A')
        self.line_wifi_kordy = self.confy
        self.line_wifi_kordy_mass.append(self.line_wifi_kordy)
        self.main_line_wifi_count +=1
# Воссоздание главных езернет линий//M206//M208
    def re_line_ethernet (self):
        ethernet_count = 0
        while ethernet_count <= int(self.main_line_ethernet_count)-1 : 
            self.canvas.create_line(0,self.line_ethernet_kordy_mass[ethernet_count],self.w,self.line_ethernet_kordy_mass[ethernet_count],width=5,fill = '#2F4F4F')
            ethernet_count +=1
        self.re_line_wifi()
        
# Воссоздание основных вайфай линий//M206//M208
    def re_line_wifi (self):
        wifi_count = 0
        while wifi_count <= int(self.main_line_wifi_count)-1 : 
            self.canvas.create_line(0,self.line_wifi_kordy_mass[wifi_count],self.w,self.line_wifi_kordy_mass[wifi_count],width=5,fill = '#E9967A')
            wifi_count +=1
        self.re_page_part_3()
    

# Перемещение объектов сетей//M206
    def moved1 (self,event):
        if self.papi == 0:
            self.focnet = str(self.focused_widget)
            ind = 0
            b = str(self.focnet)
            b = b.replace('.!notebook.!frame2.!canvas.!canvas','')
            if b == '' :
                b = str(0)
            else : b = int(b)-1
            self.confx = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
            self.confy = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
            event.widget.place(x=self.confx,y=self.confy)
            print ('Проверка',self.wid_line_ethernet_mass)
            if int(b) < self.iuw:  
                self.UNI_kordx[int(b)]=self.confx
                self.UNI_kordy[int(b)]=self.confy
                if self.ethernet_prov[int(b)] == 1:
                
                    ind = self.wid_line_ethernet_mass.index(int(b))
                    print (ind)
                    print (self.dop_line_ethernet_mass)
                    print(str(self.line_tag))
                    self.canvas.coords(self.line_tag[ind],self.confx+50,self.line_ethernet_kordy_mass[0],self.confx+50,self.confy)
                    print('перемещаю',self.confx,self.line_ethernet_kordy,self.confx,self.confy)
                    self.dop_ethernet_x[int(b)] = self.confx+50
                    print (self.dop_ethernet_x)
                    self.dop_ethernet_y[int(b)] = self.confy
                    print (self.dop_ethernet_y)
                if self.wifi_prov[int(b)] == 1:
                    indw = self.wid_line_wifi_mass.index(int(b))
                    self.canvas.coords(self.line_tag_wifi[indw],self.confx+70,self.line_wifi_kordy,self.confx+70,self.confy)
                    self.dop_wifi_x[int(b)] = self.confx+50
                    self.dop_wifi_y[int(b)] = self.confy
                        
            if self.iuw <= int(b) < self.iu+self.iuw: 
                self.ms = int(b)- self.iuw
                self.UNI_1_kordx[self.ms]=self.confx
                self.UNI_1_kordy[self.ms]=self.confy
                if self.ethernet_prov[int(b)] == 1:
                    ind = self.wid_line_ethernet_mass.index(int(b))
                    print (ind)
                    print (self.dop_line_ethernet_mass)
                    print(str(self.line_tag))
                    self.canvas.coords(self.line_tag[ind],self.confx+50,self.line_ethernet_kordy_mass[0],self.confx+50,self.confy)
                    self.dop_ethernet_x[int(b)] = self.confx+50
                    print (self.dop_ethernet_x)
                    self.dop_ethernet_y[int(b)] = self.confy
                    print (self.dop_ethernet_y)
                    print('перемещаю nene?',self.confx,self.line_ethernet_kordy,self.confx,self.confy)
                if self.wifi_prov[int(b)] == 1:
                    indw = self.wid_line_wifi_mass.index(int(b))
                    self.canvas.coords(self.line_tag_wifi[indw],self.confx+70,self.line_wifi_kordy+20,self.confx+70,self.confy)
                    self.dop_wifi_x[int(b)] = self.confx+50
                    self.dop_wifi_y[int(b)] = self.confy
                else: print('Ничего')
                
                
            if self.iuw+self.iu <= int(b) < self.iuw+self.iu+self.iun :
                self.ms = int(b)- (self.iuw+self.iu)
                self.nano_kordx[self.ms]=self.confx
                self.nano_kordy[self.ms]=self.confy
                if self.ethernet_prov[int(b)] == 1:
                    ind = self.wid_line_ethernet_mass.index(int(b))
                    print (ind)
                    print (self.dop_line_ethernet_mass)
                    print(str(self.line_tag))
                    self.canvas.coords(self.line_tag[ind],self.confx+50,self.line_ethernet_kordy_mass[0],self.confx+50,self.confy)
                    self.dop_ethernet_x[int(b)] = self.confx+50
                    print (self.dop_ethernet_x)
                    self.dop_ethernet_y[int(b)] = self.confy
                    print (self.dop_ethernet_y)
                    print('перемещаю',self.confx,self.line_ethernet_kordy,self.confx,self.confy)
                if self.wifi_prov[int(b)] == 1:
                    indw = self.wid_line_wifi_mass.index(int(b))
                    self.canvas.coords(self.line_tag_wifi[indw],self.confx+70,self.line_wifi_kordy+20,self.confx+70,self.confy)
                    self.dop_wifi_x[int(b)] = self.confx+50
                    self.dop_wifi_y[int(b)] = self.confy
                
            if self.iuw+self.iu+self.iun <= int(b) < self.iuw+self.iu+self.iun+self.ium:
                self.ms = int(b) - (self.iuw+self.iu+self.iun)
                self.mega_kordx[self.ms]=self.confx
                self.mega_kordy[self.ms]=self.confy
                if self.ethernet_prov[int(b)] == 1:
                    ind = self.wid_line_ethernet_mass.index(int(b))
                    print (ind)
                    print (self.dop_line_ethernet_mass)
                    print(str(self.line_tag))
                    self.canvas.coords(self.line_tag[ind],self.confx+50,self.line_ethernet_kordy_mass[0],self.confx+50,self.confy)
                    self.dop_ethernet_x[int(b)] = self.confx+50
                    print (self.dop_ethernet_x)
                    self.dop_ethernet_y[int(b)] = self.confy
                    print (self.dop_ethernet_y)
                    print('перемещаю',self.confx,self.line_ethernet_kordy,self.confx,self.confy)
                if self.wifi_prov[int(b)] == 1:
                    indw = self.wid_line_wifi_mass.index(int(b))
                    self.canvas.coords(self.line_tag_wifi[indw],self.confx+70,self.line_wifi_kordy+20,self.confx+70,self.confy)
                    self.dop_wifi_x[int(b)] = self.confx+50
                    self.dop_wifi_y[int(b)] = self.confy
# Нахожу коммутатор               
            if self.iuw+self.iu+self.iun+self.ium <= int(b) < self.iuw+self.iu+self.iun+self.ium+self.iue:
                self.ms = int(b) - (self.iuw+self.iu+self.iun+self.ium)
                self.ethernet_kordx[self.ms]=self.confx
                self.ethernet_kordy[self.ms]=self.confy
                if self.ethernet_prov[int(b)] == 1:
                    ind = self.wid_line_ethernet_mass.index(int(b))
                    print (ind)
                    print (self.dop_line_ethernet_mass)
                    print(str(self.line_tag))
                    self.canvas.coords(self.line_tag[ind],self.confx+100,self.line_ethernet_kordy_mass[0],self.confx+100,self.confy)
                    self.dop_ethernet_x[int(b)] = self.confx+50
                    print (self.dop_ethernet_x)
                    self.dop_ethernet_y[int(b)] = self.confy
                    print (self.dop_ethernet_y)
                    print('перемещаю',self.confx,self.line_ethernet_kordy,self.confx,self.confy)
                if self.wifi_prov[int(b)] == 1:
                    indw = self.wid_line_wifi_mass.index(int(b))
                    self.canvas.coords(self.line_tag_wifi[indw],self.confx+130,self.line_wifi_kordy,self.confx+130,self.confy)
                    self.dop_wifi_x[int(b)] = self.confx+50
                    self.dop_wifi_y[int(b)] = self.confy
                
# Нахожу сервер                
            if self.iuw+self.iu+self.iun+self.ium+self.iue <= int(b) < self.iuw+self.iu+self.iun+self.ium+self.iue+self.ius:
                self.ms = int(b) - (self.iuw+self.iu+self.iun+self.ium+self.iue)
                self.server_kordx[self.ms]=self.confx
                self.server_kordy[self.ms]=self.confy
                if self.ethernet_prov[int(b)] == 1:
                    ind = self.wid_line_ethernet_mass.index(int(b))
                    print (ind)
                    print (self.dop_line_ethernet_mass)
                    print(str(self.line_tag))
                    self.canvas.coords(self.line_tag[ind],self.confx+100,self.line_ethernet_kordy_mass[0],self.confx+100,self.confy)
                    self.dop_ethernet_x[int(b)] = self.confx+50
                    print (self.dop_ethernet_x)
                    self.dop_ethernet_y[int(b)] = self.confy
                    print (self.dop_ethernet_y)
                    print('перемещаю',self.confx,self.line_ethernet_kordy,self.confx,self.confy)
                if self.wifi_prov[int(b)] == 1:
                    indw = self.wid_line_wifi_mass.index(int(b))
                    self.canvas.coords(self.line_tag_wifi[indw],self.confx+130,self.line_wifi_kordy,self.confx+130,self.confy)
                    self.dop_wifi_x[int(b)] = self.confx+50
                    self.dop_wifi_y[int(b)] = self.confy


# Удаление виджетов вкладки "сети" //M207               
    def deletenet (self,event):
        self.focnet = str(self.focused_widget)
        b = str(self.focnet)
        b = b.replace('.!notebook.!frame2.!canvas.!canvas','')
        s = 0
        if b == '' :
            b = '0'
        else : b = int(b)-1
        print('смотрю на',b)            
        if int(b) < self.iuw:  
            if self.papi == 0:
                print('удаляю uno wifi..')
                event.widget.place_forget()
                print(event.widget)
                self.UNI_kordx[int(b)]='-'
                self.UNI_kordy[int(b)]='-'
                self.UNI_count = self.UNI_count-1
                self.cnt_UNI +=1
                print(self.cnt_UNI_1)
        if self.iuw <= int(b) < self.iu+self.iuw: 
            if self.papi == 0:
                s = int(b)- self.iuw
                print('удаляю uno')
                print(s)
                event.widget.place_forget()
                print(event.widget)
                self.UNI_1_kordx[int(s)]='-'
                self.UNI_1_kordy[int(s)]='-'
                self.UNI_1_count =self.UNI_1_count-1            
                self.cnt_UNI_1 +=1
        if self.iuw+self.iu <= int(b) < self.iuw+self.iu+self.iun :
            if self.papi == 0:
                s = int(b)- (self.iuw+self.iu)
                print('удаляю nano')
                print(s)
                event.widget.place_forget()
                print(event.widget)
                self.nano_kordx[int(s)]= '-'
                self.nano_kordy[int(s)]= '-'
                self.nano_count = self.nano_count-1
                self.cnt_nano +=1
        if self.iuw+self.iu+self.iun <= int(b) < self.iuw+self.iu+self.iun+self.ium:
            if self.papi == 0:
                s = int(b) - (self.iuw+self.iu+self.iun)
                print('удаляю mega')
                print(s)
                event.widget.place_forget()
                print(event.widget)
                self.mega_kordx[int(s)]='-'
                self.mega_kordy[int(s)]='-'
                self.mega_count = self.mega_count-1
                self.cnt_mega +=1
        if self.iuw+self.iu+self.iun+self.ium <= int(b) < self.iuw+self.iu+self.iun+self.ium+self.iue:
            if self.papi == 0:
                s = int(b) - (self.iuw+self.iu+self.iun+self.ium)
                print('удаляю ethernet')
                print(s)
                event.widget.place_forget()
                print(event.widget)
                self.ethernet_kordx[int(s)]='-'
                self.ethernet_kordy[int(s)]='-'
                self.ethernet_count = self.ethernet_count-1
                self.cnt_ethernet +=1
        if self.iuw+self.iu+self.iun+self.ium+self.iue <= int(b) < self.iuw+self.iu+self.iun+self.ium+self.iue+self.ius:
            if self.papi == 0:
                s = int(b) - (self.iuw+self.iu+self.iun+self.ium+self.iue)
                print('удаляю server')
                print (s)
                event.widget.place_forget()
                print(event.widget)
                self.server_kordx[int(s)]='-'
                self.server_kordy[int(s)]='-'
                self.server_count = self.server_count-1
                self.cnt_server +=1

# Воссоздание (UNO WIFI)//M205
        
    def reimage1 (self):
        print ('Загружаю uno wifi..')
        self.iuw = 0
        while self.iuw <= int(self.UNI_count)-1 :                                                         
            self.UNI_can=Canvas(self.canvas,width=100,height=100,bg='#DEF7FE')
            self.UNI_can.place(x=int(self.UNI_kordx[self.iuw]),y=int(self.UNI_kordy[self.iuw]))
            self.UNI_wifi_obj = PhotoImage(file='image\\unowifi.png')
            self.UNI_mass.append(self.UNI_wifi_obj)
            self.id_img1 = self.UNI_can.create_image(50,50,image=self.UNI_mass[self.iuw])
            print(self.UNI_count,'bcb',self.iuw)
            self.iuw+=1
        self.reimage2()

# (UNO)//M205

    def reimage2 (self):
        print ('Загружаю uno..')
        self.iu = 0
        while self.iu <= int(self.UNI_1_count)-1 :                                                         
            self.UNI_1_can=Canvas(self.canvas,width=100,height=100,bg='#DEF7FE')
            self.UNI_1_can.place(x=int(self.UNI_1_kordx[self.iu]),y=int(self.UNI_1_kordy[self.iu]))
            self.UNI_1_obj = PhotoImage(file='image\\UNO1.png')
            self.UNI_1_mass.append(self.UNI_1_obj)
            self.id_img1 = self.UNI_1_can.create_image(50,50,image=self.UNI_1_mass[self.iu])
            print(self.UNI_1_count,'bcb',self.iu)
            self.UNI_1_can.bind('<Double-Button-1>',self.UNO_win)
            print(self.ethernet_prov)
            self.iu+=1
        self.reimage3()

# (NANO)//M205

    def reimage3 (self):
        print ('Загружаю nano..')
        self.iun = 0
        while self.iun <= int(self.nano_count)-1 :                                                         
            self.nano_can=Canvas(self.canvas,width=100,height=100,bg='#DEF7FE')
            self.nano_can.place(x=int(self.nano_kordx[self.iun]),y=int(self.nano_kordy[self.iun]))
            self.nano_obj = PhotoImage(file='image\\nano.png')
            self.nano_mass.append(self.nano_obj)
            self.id_img1 = self.nano_can.create_image(50,50,image=self.nano_mass[self.iun])
            print(self.nano_count,'bcb',self.iun)
            self.iun+=1
        self.reimage4()

# (MEGA)//M205

    def reimage4 (self):
        print ('Загружаю mega..')
        self.ium = 0
        while self.ium <= int(self.mega_count)-1 :                                                         
            self.mega_can=Canvas(self.canvas,width=100,height=100,bg='#DEF7FE')
            self.mega_can.place(x=int(self.mega_kordx[self.ium]),y=int(self.mega_kordy[self.ium]))
            self.mega_obj = PhotoImage(file='image\\mega.png')
            self.mega_mass.append(self.mega_obj)
            self.id_img1 = self.mega_can.create_image(50,50,image=self.mega_mass[self.ium])
            print(self.mega_count,'bcb',self.ium)
            self.ium+=1
        self.reimage5()

# (ETHERNET)//M205

    def reimage5 (self):
        print ('Загружаю ethernet..')
        self.iue = 0
        while self.iue <= int(self.ethernet_count)-1 :                                                         
            self.ethernet_can=Canvas(self.canvas,width=200,height=100,bg='#DEF7FE')
            self.ethernet_can.place(x=int(self.ethernet_kordx[self.iue]),y=int(self.ethernet_kordy[self.iue]))
            self.ethernet_obj = PhotoImage(file='image\\ethernet.png')
            self.ethernet_mass.append(self.ethernet_obj)
            self.id_img1 = self.ethernet_can.create_image(100,50,image=self.ethernet_mass[self.iue])
            print(self.ethernet_count,'bcb',self.iue)
            self.iue+=1
        self.reimage6()

# (SERVER)//M205

    def reimage6 (self):
        print ('Загружаю server..')
        self.ius = 0
        while self.ius <= int(self.server_count)-1 :                                                         
            self.server_can=Canvas(self.canvas,width=200,height=150,bg='#DEF7FE')
            self.server_can.place(x=int(self.server_kordx[self.ius]),y=int(self.server_kordy[self.ius]))
            self.server_obj = PhotoImage(file='image\\server.png')
            self.server_mass.append(self.server_obj)
            self.id_img1 = self.server_can.create_image(100,75,image=self.server_mass[self.ius])
            print(self.server_count,'bcb',self.ius)
            self.server_can.bind('<Double-Button-1>')
            self.ius+=1
            self.pov = self.iuw+self.iu+self.iun+self.ium+self.iue+self.ius
            self.ethernet_prov = self.ethernet_prov*self.pov
            print ('self.ethernet_prov :',self.ethernet_prov)
            self.wifi_prov = self.wifi_prov*self.pov
            print(self.wifi_prov)
        self.re_line_ethernet()

    def createNewWindow_uno_wifi_win(self):
        self.newWindow1 = tk.Toplevel(self.window)
        self.newWindow1.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.newWindow1,text='Имя')
        f_bot = LabelFrame(self.newWindow1,text='Ip адресс')  
        labelExample = tk.Label(self.newWindow1, text = "Новый текст")
        namm = tk.Label(f_top,text="Введите имя :")
        self.show2 = tk.Entry(f_top,width=30)
        namn_2 = tk.Label(f_bot,text='Введите ip адресс :')
        self.show20 = tk.Entry(f_bot,width=30)
        buttonExample1 = tk.Button(self.newWindow1, text = "Контроллер UNO_wifi",command = self.image1)
        f_top.pack(padx=10,pady=10)
        f_bot.pack(padx=10,pady=10)
        namm.pack(side = LEFT,padx = 5, pady = 5)                                                                          
        self.show2.pack(side = LEFT,padx = 5, pady = 5)
        namn_2.pack(side = LEFT,padx = 5, pady = 5)
        self.show20.pack(side = LEFT,padx = 5, pady = 5)
        labelExample.pack(padx = 5, pady = 5)
        buttonExample1.pack()
                

# Создание объектов во фрейме "сети"(UNO WIFI)//M204
    def image1 (self):
        global xex
        global yey
        self.xex = self.canvas.winfo_pointerx()- self.canvas.winfo_rootx()
        self.yey = self.canvas.winfo_pointery()- self.canvas.winfo_rooty()
        self.name_uno_wifi.append(self.show2.get())
        self.ip_uno_wifi.append(self.show20.get())
        self.UNI_can=Canvas(self.canvas,width=100,height=100,bg='#DEF7FE')
        self.UNI_can.place(x=self.xex,y=self.yey)
        self.UNI_kordx.append(self.xex)
        self.UNI_kordy.append(self.yey)
        self.UNI_wifi_obj = PhotoImage(file='image\\unowifi.png')
        self.UNI_mass.append(self.UNI_wifi_obj)
        self.id_img1 = self.UNI_can.create_image(50,50,image=self.UNI_mass[self.UNI_count])
        self.wifi_prov.append(0)
        self.newWindow1.destroy()
        self.UNI_count +=1

    def createNewWindow_uno_win(self):
        self.newWindow1 = tk.Toplevel(self.window)
        self.newWindow1.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.newWindow1,text='Имя')
        f_bot = LabelFrame(self.newWindow1,text='Ip адресс')  
        labelExample = tk.Label(self.newWindow1, text = "Новый текст")
        namm = tk.Label(f_top,text="Введите имя :")
        self.show2 = tk.Entry(f_top,width=30)
        namn_2 = tk.Label(f_bot,text='Введите ip адресс :')
        self.show20 = tk.Entry(f_bot,width=30)
        buttonExample1 = tk.Button(self.newWindow1, text = "Контроллер UNO",command = self.image2)
        f_top.pack(padx=10,pady=10)
        f_bot.pack(padx=10,pady=10)
        namm.pack(side = LEFT,padx = 5, pady = 5)                                                                          
        self.show2.pack(side = LEFT,padx = 5, pady = 5)
        namn_2.pack(side = LEFT,padx = 5, pady = 5)
        self.show20.pack(side = LEFT,padx = 5, pady = 5)
        labelExample.pack(padx = 5, pady = 5)
        buttonExample1.pack()
        
# (UNO) //M204
    def image2 (self):
        global xex
        global yey
        self.xex = self.canvas.winfo_pointerx()- self.canvas.winfo_rootx()
        self.yey = self.canvas.winfo_pointery()- self.canvas.winfo_rooty()
        self.name_uno.append(self.show2.get())
        self.ip_uno.append(self.show20.get())
        print(self.ip_uno)
        self.UNI_1_can=Canvas(self.canvas,width=100,height=100,bg='#DEF7FE')
        self.UNI_1_can.place(x=self.xex,y=self.yey)
        self.UNI_1_kordx.append(self.xex)
        self.UNI_1_kordy.append(self.yey)
        self.UNI_1_obj = PhotoImage(file='image\\UNO1.png')
        self.UNI_1_mass.append(self.UNI_1_obj)
        self.id_img1 = self.UNI_1_can.create_image(50,50,image=self.UNI_1_mass[self.UNI_1_count])
        self.UNI_1_count +=1
        self.ethernet_prov.append(0)
        self.newWindow1.destroy()
        print(self.ethernet_prov)

    def createNewWindow_nano_win(self):
        self.newWindow1 = tk.Toplevel(self.window)
        self.newWindow1.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.newWindow1,text='Имя')
        f_bot = LabelFrame(self.newWindow1,text='Ip адресс')  
        labelExample = tk.Label(self.newWindow1, text = "Новый текст")
        namm = tk.Label(f_top,text="Введите имя :")
        self.show2 = tk.Entry(f_top,width=30)
        namn_2 = tk.Label(f_bot,text='Введите ip адресс :')
        self.show20 = tk.Entry(f_bot,width=30)
        buttonExample1 = tk.Button(self.newWindow1, text = "Контроллер NANO",command = self.image3)
        f_top.pack(padx=10,pady=10)
        f_bot.pack(padx=10,pady=10)
        namm.pack(side = LEFT,padx = 5, pady = 5)                                                                          
        self.show2.pack(side = LEFT,padx = 5, pady = 5)
        namn_2.pack(side = LEFT,padx = 5, pady = 5)
        self.show20.pack(side = LEFT,padx = 5, pady = 5)
        labelExample.pack(padx = 5, pady = 5)
        buttonExample1.pack()
        
        
# (NANO)//M204
    def image3 (self):
        global xex
        global yey
        self.xex = self.canvas.winfo_pointerx()- self.canvas.winfo_rootx()
        self.yey = self.canvas.winfo_pointery()- self.canvas.winfo_rooty()
        self.name_nano.append(self.show2.get())
        self.ip_nano.append(self.show20.get())
        self.nano_can=Canvas(self.canvas,width=100,height=100,bg='#DEF7FE')
        self.nano_can.place(x=self.xex,y=self.yey)
        self.nano_kordx.append(self.xex)
        self.nano_kordy.append(self.yey)
        self.nano_obj = PhotoImage(file='image\\nano.png')
        self.nano_mass.append(self.nano_obj)
        self.id_img1 = self.nano_can.create_image(50,50,image=self.nano_mass[self.nano_count])
        self.newWindow1.destroy()
        self.nano_count +=1
        self.ethernet_prov.append(0)

    def createNewWindow_mega_win(self):
        self.newWindow1 = tk.Toplevel(self.window)
        self.newWindow1.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.newWindow1,text='Имя')
        f_bot = LabelFrame(self.newWindow1,text='Ip адресс')  
        labelExample = tk.Label(self.newWindow1, text = "Новый текст")
        namm = tk.Label(f_top,text="Введите имя :")
        self.show2 = tk.Entry(f_top,width=30)
        namn_2 = tk.Label(f_bot,text='Введите ip адресс :')
        self.show20 = tk.Entry(f_bot,width=30)
        buttonExample1 = tk.Button(self.newWindow1, text = "Контроллер MEGA",command = self.image4)
        f_top.pack(padx=10,pady=10)
        f_bot.pack(padx=10,pady=10)
        namm.pack(side = LEFT,padx = 5, pady = 5)                                                                          
        self.show2.pack(side = LEFT,padx = 5, pady = 5)
        namn_2.pack(side = LEFT,padx = 5, pady = 5)
        self.show20.pack(side = LEFT,padx = 5, pady = 5)
        labelExample.pack(padx = 5, pady = 5)
        buttonExample1.pack()
        
# (MEGA)//M204
    def image4 (self):
        global xex
        global yey
        self.xex = self.canvas.winfo_pointerx()- self.canvas.winfo_rootx()
        self.yey = self.canvas.winfo_pointery()- self.canvas.winfo_rooty()
        self.name_mega.append(self.show2.get())
        self.ip_mega.append(self.show20.get())
        self.mega_can=Canvas(self.canvas,width=100,height=100,bg='#DEF7FE')
        self.mega_can.place(x=self.xex,y=self.yey)
        self.mega_kordx.append(self.xex)
        self.mega_kordy.append(self.yey)
        self.mega_obj = PhotoImage(file='image\\mega.png')
        self.mega_mass.append(self.mega_obj)
        self.id_img1 = self.mega_can.create_image(50,50,image=self.mega_mass[self.mega_count])
        self.newWindow1.destroy()
        self.mega_count +=1
        self.ethernet_prov.append(0)
        
# (Коммутатор)//M204
    def image5 (self):
        global xex
        global yey
        self.xex = self.canvas.winfo_pointerx()- self.canvas.winfo_rootx()
        self.yey = self.canvas.winfo_pointery()- self.canvas.winfo_rooty()
        self.ethernet_can=Canvas(self.canvas,width = 200,height = 100,bg='#DEF7FE')
        self.ethernet_can.place(x = self.xex,y = self.yey)
        self.ethernet_kordx.append(self.xex)
        self.ethernet_kordy.append(self.yey)
        self.ethernet_obj = PhotoImage(file='image\\ethernet.png')
        self.ethernet_mass.append(self.ethernet_obj)
        self.id_img1 = self.ethernet_can.create_image(100,50,image=self.ethernet_mass[self.ethernet_count])
        self.ethernet_count +=1
        self.ethernet_prov.append(0)
        
# (Сервер)//M204
    def image6 (self):
        global xex
        global yey
        a = 0
        self.xex = self.canvas.winfo_pointerx()- self.canvas.winfo_rootx()
        self.yey = self.canvas.winfo_pointery()- self.canvas.winfo_rooty()
        self.server_can=Canvas(self.canvas,width=200,height=150,bg='#DEF7FE')
        self.server_can.place(x = self.xex,y = self.yey)
        self.server_kordx.append(self.xex)
        self.server_kordy.append(self.yey)
        self.server_obj = PhotoImage(file='image\\server.png')
        self.server_mass.append(self.server_obj)
        self.id_img1 = self.server_can.create_image(100,75,image=self.server_mass[self.server_count])
        self.server_count +=1
        self.ethernet_prov.append(0)
        
# (Меню во вкладке "сети") //M002        
    def adddlist2 (self,event = None):
        print('меню 2')
        self.addmenu3 = Menu(tearoff = 0)
        self.addmenu4 = Menu(self.addmenu3,tearoff = 0)
        self.addmenu5 = Menu(self.addmenu4,tearoff = 0)
        self.addmenu5.add_command (label='Arduino Uno', command = self.createNewWindow_uno_win)
        self.addmenu5.add_command (label='Arduino Uno WiFi',command = self.createNewWindow_uno_wifi_win)
        self.addmenu5.add_command (label='Arduino Nano', command = self.createNewWindow_nano_win)
        self.addmenu5.add_command (label='Arduino Mega',command = self.createNewWindow_mega_win)
        self.addmenu4.add_command (label="Сеть Ethernet",command = self.line_ethernet)
        self.addmenu4.add_command (label="Сеть WiFi",command = self.line_wifi)
        self.addmenu4.add_command (label='Сервер',command = self.image6)
        self.addmenu4.add_command (label='Ethernet коммутатор',command = self.image5)
        self.addmenu4.add_cascade (label='Контроллер',menu = self.addmenu5)
        self.addmenu3.add_cascade (label='Добавить',menu = self.addmenu4)
        self.addmenu3.add_command (label = self.redk, command = self.blocked)
        self.addmenu3.add_command (label='Отмена')
        self.addmenu3.add_separator()
        self.addmenu3.add_command (label='Выход',command = self.quitw)
        self.menulist2()
        
    #//M007
    def insert_text(self):
        file_name = fd.askopenfilename(
                        filetypes=(("ZIP files", "*.zip"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
        f = open(file_name)
        shutil.unpack_archive(str(file_name),'data')
        f.close()
        self.window.destroy()
        self.__init__()
 
# Создание бэкапа //M007
    def extract_text(self):
        file_name = fd.asksaveasfilename(initialfile='backup',
            filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")))
    
        print(file_name)
        shutil.make_archive(str(file_name),'zip','data')
        
# Тестовый индикатор //M103
    def createOval (self):
        ovalx = self.canvas1.winfo_pointerx() - self.canvas1.winfo_rootx()
        ovaly = self.canvas1.winfo_pointery() - self.canvas1.winfo_rooty()
        self.newcircle = self.canvas1.create_oval(ovalx,ovaly,ovalx+10,ovaly+10,fill='red')

# меню //M002
    def adddlist (self,event = None):
        self.addmenu = Menu(tearoff = 0)
        self.addmenu2 = Menu(self.addmenu,tearoff = 0)
        self.addmenu2.add_command (label="Кнопку", command = self.createNewWindow)
        self.addmenu2.add_command (label="Шкалу", command = self.createNewWindow3)
        self.addmenu2.add_command (label='Текст', command = self.createNewWindow1)
        self.addmenu2.add_command (label='Окно ввода', command = self.createNewWindow2)
        self.addmenu2.add_command (label='Индикатор(тест)', command = self.createOval)
        self.addmenu2.add_command (label='Шкала бака')
        self.addmenu.add_cascade (label='Добавить',menu = self.addmenu2)
        self.addmenu.add_command (label = self.redk, command = self.blocked)
        self.addmenu.add_command (label='Отмена')
        self.addmenu.add_separator()
        self.addmenu.add_command (label='Выход',command = self.quitw)
        self.menulist()
        
# Блокировка изменений //M001
    def blocked (self):
        if self.papi == 0:
            self.papi = 1
            self.redk = 'Редактирование ВКЛ'
            print(self.redk)
        else:
            self.papi = 0
            self.redk = 'Редактирование ВЫКЛ'
            print (self.redk)
# Создание меню через нажатие на мышку //M002
    def menulist(self):
        global xex
        global yey
        self.xex = self.window.winfo_pointerx ()                                                
        self.yey = self.window.winfo_pointery ()
        self.addmenu.post(self.xex,self.yey)
#//M002
    def menulist2(self):
        global xex
        global yey
        self.xex = self.window.winfo_pointerx()
        self.yey = self.window.winfo_pointery()
        self.addmenu3.post(self.xex,self.yey)
        
# Выходим с программы //M001
    def quitw (self):
        quit()

# Устанавливаю фокус элемменту, на который навожусь //M009
    def fff (self,event):
        if self.papi == 0:
            event.widget.focus_set()
            self.focused_widget = self.window.focus_get()
            print(self.focused_widget)
            self.num_widget = self.focused_widget

# Удаляю элемент в фокусе(пока что только временнно, нужно выловить id и чистить список) //M107
    def deletew (self,event):
        print(self.papi)
        self.focdef = str(self.focused_widget)
        a = str(self.focdef)
        b = str(self.focdef)
        b = b.replace('.!notebook.!frame.!canvas.!button','')
        b = b.replace('.!notebook.!frame.!canvas.!entry','')
        b = b.replace('.!notebook.!frame.!canvas.!scale','')
        b = b.replace('.!notebook.!frame.!label','')
        a = a.replace('.!notebook.!frame.!canvas.!','')
        a = a.replace('.!notebook.!frame.!','')
        a = a.replace('0','')
        a = a.replace('1','')
        a = a.replace('2','')
        a = a.replace('3','')
        a = a.replace('4','')
        a = a.replace('5','')
        a = a.replace('6','')
        a = a.replace('7','')
        a = a.replace('8','')
        a = a.replace('9','')
        print('записанно :',a)
        print('номер :',b)
        if b == '' :
            b = '0'
        else : b = int(b)-1
        print(b)
        if a == 'button':
            if self.papi == 0:
                print('удаляю кнопку')
                event.widget.place_forget()
                print(event.widget)
                self.kordx[int(b)]='-'
                self.kordy[int(b)]='-'
                self.mist[int(b)]='-'
                self.pidr[int(b)]='-'
                self.count = self.count-1
                self.count1 = self.count1-1
                self.cntb +=1
                print(self.count,self.count1)
        if a == 'entry':
            if self.papi == 0:
                print('удаляю окно ввода')
                event.widget.place_forget()
                print(event.widget)
                self.kordxe[int(b)]='-'
                self.kordye[int(b)]='-'
                self.counte = self.counte-1
                self.tage[int(b)]='-'             
                self.cnte +=1
        if a == 'scale':
            if self.papi == 0:
                print('удаляю шкалу')
                event.widget.place_forget()
                print(event.widget)
                self.kordxs[int(b)]= '-'
                self.kordys[int(b)]= '-'
                self.konchs[int(b)]='-'
                self.nachs[int(b)]= '-'
                self.counts = self.counts-1
                self.cnts +=1
        if a == 'label':
            if self.papi == 0:
                print('удаляю надпись')
                event.widget.place_forget()
                print(event.widget)
                self.kordxl[int(b)-1]='-'
                self.kordyl[int(b)-1]='-'
                self.textl[int(b)-1]='-'
                self.countl = self.countl-1
                self.cntl +=1
# Создание шкалы //M103
    def newScale (self):
        global xex
        global yey
        print ('окно ввода')
        self.xex = self.window.winfo_pointerx ()                                            
        self.kordxs.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.kordys.append(self.yey)
        self.do = self.show4.get()                                                           
        self.nachs.append(self.do)
        self.posle = self.show5.get()
        self.konchs.append(self.posle)
        self.newScale1 = tk.Scale(self.frame1, orient='horizontal',resolution=0.1,bg = '#DEF7FE',from_=self.do,to=self.posle)            
        self.newScale1.place(x =self.xex, y =self.yey)
        self.counts +=1
        self.newWindow3.destroy()
    #//M106
    def confb (self,event):                                                                     # Перемещение любого виджета на ткинтере
        print(self.papi)
        if self.papi == 0:
            self.focdef = str(self.focused_widget)
            a = str(self.focdef)
            b = str(self.focdef)
            b = b.replace('.!notebook.!frame.!canvas.!button','')
            b = b.replace('.!notebook.!frame.!canvas.!entry','')
            b = b.replace('.!notebook.!frame.!canvas.!scale','')
            b = b.replace('.!notebook.!frame.!label','')
            a = a.replace('.!notebook.!frame.!canvas.!','')
            a = a.replace('.!notebook.!frame.!','')
            a = a.replace('0','')
            a = a.replace('1','')
            a = a.replace('2','')
            a = a.replace('3','')
            a = a.replace('4','')
            a = a.replace('5','')
            a = a.replace('6','')
            a = a.replace('7','')
            a = a.replace('8','')
            a = a.replace('9','')
            print('записанно :',a)
            print('номер :',b)
            if b == '' :
                b = '0'
            else : b = int(b)-1
            print(b)
            self.confx = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
            self.confy = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
            event.widget.place(x=self.confx,y=self.confy)
            if a == 'button':
                self.kordx[int(b)]=self.confx
                self.kordy[int(b)]=self.confy
            if a == 'entry':
                self.kordxe[int(b)]=self.confx
                self.kordye[int(b)]=self.confy
            if a == 'scale':
                self.kordxs[int(b)]=self.confx
                self.kordys[int(b)]=self.confy
            if a == 'label':
                self.kordxl[int(b)-1]=self.confx
                self.kordyl[int(b)-1]=self.confy

#Начинаем поток, чтобы при создании елементов не висло окно тКинтера //M203
    def addfuntrd (self,event):
            self.th1 = threading.Thread(target = self.addfun)
            self.th1.start()

# Создание тренда, пока что только одного конкретного датчика //M400
    def trd (self):
        plt.title('Температура', fontsize=20, fontname='Times New Roman')                       # Задаем конфиги окну тренда
        plt.xlabel('Время', color='black')                                                      # Ставим нижний и боковой текст
        plt.ylabel('Температура ',color='black')
        plt.legend()
        x_list = [self.nowz]                                        
        y_list = [self.zap]
        plt.grid(True)                                                                          # Говорим, что будем использовать сетку
        plt.plot([0,1,2,3,4,5,6,7,8,9],[0,4,5,2,1,6,7,9,2],colors=['red'])#(self.nowz,self.zap)       colors=['red','blue']                                                   # Берем у массивов информацию для отрисовки по координатам
        plt.show()                                                                              # Показываем тренд
        print ('trend :',self.zap)
        print ('now :',self.now)
        print ('nowz : ',self.nowz)

# Воссоздание шкалы //M105
    def newScale1 (self):
        print ('Загружаю шкалы...')
        ir = 0
        while ir <= int(self.counts)-1 :                                                         
            self.newScale = tkinter.Scale(self.canvas1,orient='horizontal',resolution=0.1,bg='#DEF7FE',from_=self.nachs[ir],to=self.konchs[ir])
            self.newScale.place(x =int(self.kordxs[ir]), y =int(self.kordys[ir]))
            print(self.counts,'bcb',ir)
            ir+=1
        self.reimage1()

# Воссоздание окна ввода //M105
    def newEntry1 (self):
        print ('Загружаю окна ввода...')
        ie = 0
        while ie <= int(self.counte)-1 :                                                           
            self.newEntry = tkinter.Entry(self.canvas1, width=30)
            self.newEntry.place(x =int(self.kordxe[ie]), y =int(self.kordye[ie]))
            print(self.counte,'bcb',ie)
            ie+=1
        self.newScale1()

# Воссоздание надписи //M105
    def newLabel1 (self):
        print ('Загружаю надписи...')
        ia = 0
        while ia <= int(self.countl)-1 :                                                           
            self.newLabel = tkinter.Label(self.frame1, text=self.textl[ia],bg ='#DEF7FE')
            self.newLabel.place(x =int(self.kordxl[ia]), y =int(self.kordyl[ia]))
            print(self.countl,'bcb',ia)
            ia+=1
        self.newEntry1()

# Воссоздание ранее созданных кнопок //M105
    def newButton1 (self):
        print ('Загружаю кнопки...')
        i = 0
        while i <= int(self.count1)-1 :                                                           # Весь смысл состоит в том, чтобы по предыдущему счетчику воссоздавать кол-во кнопок и все параметры массива(требует небольшой доработки)
            self.newButton = tkinter.Button(self.canvas1, text=self.pidr[self.count2], command= lambda which=self.count2 : self.vizov(which))
            self.newButton.place(x =int(self.kordx[self.count2]), y =int(self.kordy[self.count2]))
            self.count2 +=1
            print(self.count1,'bcb',self.count2)
            i+=1
        self.newLabel1()

# Сохранение всего проекта, нужно нажатие с кнопки для запуска фун-и //M010
    def saveprog (self):
        self.tx_error.configure(state=tk.NORMAL)
        self.tx_error.insert(1.0,str(datetime.now())+': Сохранение данных...\n')
        self.tx_error.configure(state=tk.DISABLED)
        #self.error = self.error+'\n'+str(datetime.now())+': Сохранение данных.'
        #self.label.config(text = self.error)

        i1=1
        while i1<=self.cntb:
            print(self.kordx,self.kordy,self.mist,self.pidr)
            self.kordx.remove('-')
            self.kordy.remove('-')
            self.mist.remove('-')
            self.pidr.remove('-')
            i1+=1
            print(self.kordx,self.kordy,self.mist,self.pidr)
        i2=1
        while i2<=self.cnte:
            print(self.kordxe,self.kordye,self.tage)
            self.kordxe.remove('-')
            self.kordye.remove('-')
            self.tage.remove('-')
            i2+=1
            print(self.kordxe,self.kordye,self.tage)
        i3=1
        while i3<=self.cnts:
            print(self.kordxs,self.kordys,self.konchs,self.nachs)
            self.kordxs.remove('-')
            self.kordys.remove('-')
            self.konchs.remove('-')
            self.nachs.remove('-')
            i3+=1
            print(self.kordxs,self.kordys,self.konchs,self.nachs)
        i4=1
        while i4<=self.cntl:
            print(self.kordxl,self.kordyl,self.textl)
            self.kordxl.remove('-')
            self.kordyl.remove('-')
            self.textl.remove('-')
            i4+=1
            print(self.kordxl,self.kordyl,self.textl)

        i5=1
        while i5<=self.cnt_UNI_1:
            print(self.UNI_1_kordx,self.UNI_1_kordy)
            self.UNI_1_kordx.remove('-')
            self.UNI_1_kordy.remove('-')
            i5+=1
            print(self.UNI_1_kordx,self.UNI_1_kordy)

        i6=1
        while i6<=self.cnt_UNI:
            print(self.UNI_kordx,self.UNI_kordy)
            self.UNI_kordx.remove('-')
            self.UNI_kordy.remove('-')
            i6+=1
            print(self.UNI_kordx,self.UNI_kordy)
        i7=1
        while i7<=self.cnt_nano:
            print(self.nano_kordx,self.nano_kordy)
            self.nano_kordx.remove('-')
            self.nano_kordy.remove('-')
            i7+=1
            print(self.nano_kordx,self.nano_kordy)
        i8=1
        while i8<=self.cnt_mega:
            print(self.mega_kordx,self.mega_kordy)
            self.mega_kordx.remove('-')
            self.mega_kordy.remove('-')
            i8+=1
            print(self.mega_kordx,self.mega_kordy)
        i9=1
        while i9<=self.cnt_ethernet:
            print(self.ethernet_kordx,self.ethernet_kordy)
            self.ethernet_kordx.remove('-')
            self.ethernet_kordy.remove('-')
            i9+=1
            print(self.ethernet_kordx,self.ethernet_kordy)

        i10=1
        while i10<=self.cnt_server:
            print(self.server_kordx,self.server_kordy)
            self.server_kordx.remove('-')
            self.server_kordy.remove('-')
            i10+=1

        i11=1
        while i11<=self.del_dop_line_ethernet:
            print('chet',self.dop_line_ethernet_count)
            print(self.wid_line_ethernet_mass,self.line_tag,self.dop_ethernet_x,self.dop_ethernet_y)
            self.wid_line_ethernet_mass.remove('-')
            self.line_tag.remove('-')
            self.dop_ethernet_x.remove('-')
            self.dop_ethernet_y.remove('-')
            print(self.wid_line_ethernet_mass,self.line_tag,self.dop_ethernet_x,self.dop_ethernet_y)
            i11+=1
        i12=1
        while i12<=self.del_dop_line_wifi:
            print(self.wid_line_wifi_mass,self.line_tage_wifi,self.dop_wifi_x,self.dop_wifi_y)
            self.wid_line_wifi_mass.remove('-')
            self.line_tage_wifi.remove('-')
            self.dop_wifi_x.remove('-')
            self.dop_wifi_y.remove('-')
            print(self.wid_line_wifi_mass,self.line_tage_wifi,self.dop_wifi_x,self.dop_wifi_y)
            i12+=1
            
            #print(self.server_kordx,self.server_kordy)
        with open("data\\count_page.dat","wb") as pickle_file:  #
            pickle.dump(self.count_page,pickle_file,pickle.HIGHEST_PROTOCOL) #    
        with open("data\\name_page.dat","wb") as pickle_file:  #
            pickle.dump(self.name_page,pickle_file,pickle.HIGHEST_PROTOCOL) #            
        with open("data\\kordx.dat","wb") as pickle_file:
            pickle.dump(self.kordx,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open("data\\kordy.dat","wb") as pickle_file:
            pickle.dump(self.kordy,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open("data\\mist.dat","wb") as pickle_file:
            pickle.dump(self.mist,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open("data\\pidr.dat","wb") as pickle_file:
            pickle.dump(self.pidr,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open("data\\count1.dat","wb") as pickle_file:
            pickle.dump(self.count,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open("data\\trendx1.dat","wb") as pickle_file:
            pickle.dump(self.nowz,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open("data\\trendy1.dat","wb") as pickle_file:
            pickle.dump(self.zap,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\kordxl.dat','wb') as pickle_file:
            pickle.dump(self.kordxl,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\kordyl.dat','wb') as pickle_file:
            pickle.dump(self.kordyl,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\textl.dat','wb') as pickle_file:
            pickle.dump(self.textl,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\kordxs.dat','wb') as pickle_file:
            pickle.dump(self.kordxs,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\kordys.dat','wb') as pickle_file:
            pickle.dump(self.kordys,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\nachs.dat','wb') as pickle_file:
            pickle.dump(self.nachs,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\konchs.dat','wb') as pickle_file:
            pickle.dump(self.konchs,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\kordxe.dat','wb') as pickle_file:
            pickle.dump(self.kordxe,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\kordye.dat','wb') as pickle_file:
            pickle.dump(self.kordye,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\tage.dat','wb') as pickle_file:
            pickle.dump(self.tage,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\countl.dat','wb') as pickle_file:
            pickle.dump(self.countl,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\counte.dat','wb') as pickle_file:
            pickle.dump(self.counte,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('data\\counts.dat','wb') as pickle_file:
            pickle.dump(self.counts,pickle_file,pickle.HIGHEST_PROTOCOL)
        with open('netdata\\unicount.dat','wb') as pickle_file:
            pickle.dump(self.UNI_count,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Счётчик уно вайфай',self.UNI_count)
        with open('netdata\\uni1count.dat','wb') as pickle_file:
            pickle.dump(self.UNI_1_count,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('счётчик уно',self.UNI_1_count)
        with open('netdata\\nanocount.dat','wb') as pickle_file:
            pickle.dump(self.nano_count,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('счётчик нано',self.nano_count)
        with open('netdata\\megacount.dat','wb') as pickle_file:
            pickle.dump(self.mega_count,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('счётчик мега',self.mega_count)
        with open('netdata\\ethernetcount.dat','wb') as pickle_file:
            pickle.dump(self.ethernet_count,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('счётчик коммутатора',self.ethernet_count)
        with open('netdata\\servercount.dat','wb') as pickle_file:
            pickle.dump(self.server_count,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('счётчик сервера',self.server_count)
        with open('netdata\\uni1kordx.dat','wb') as pickle_file:
            pickle.dump(self.UNI_1_kordx,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты х уно',self.UNI_1_kordx)
        with open('netdata\\uni1kordy.dat','wb') as pickle_file:
            pickle.dump(self.UNI_1_kordy,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты у уно',self.UNI_1_kordy)
        with open('netdata\\unikordx.dat','wb') as pickle_file:
            pickle.dump(self.UNI_kordx,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты х уно вай фай',self.UNI_kordx)
        with open('netdata\\unikordy.dat','wb') as pickle_file:
            pickle.dump(self.UNI_kordy,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты у уно вай фай',self.UNI_kordy)
        with open('netdata\\nanokordx.dat','wb') as pickle_file:
            pickle.dump(self.nano_kordx,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты х нано',self.nano_kordx)
        with open('netdata\\nanokordy.dat','wb') as pickle_file:
            pickle.dump(self.nano_kordy,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты у нано',self.nano_kordy)
        with open('netdata\\megakordx.dat','wb') as pickle_file:
            pickle.dump(self.mega_kordx,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты х мега',self.mega_kordx)
        with open('netdata\\megakordy.dat','wb') as pickle_file:
            pickle.dump(self.mega_kordy,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('уоординаты у мега',self.mega_kordy)
        with open('netdata\\ethernetkordx.dat','wb') as pickle_file:
            pickle.dump(self.ethernet_kordx,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты х коммутатора',self.ethernet_kordx)
        with open('netdata\\ethernetkordy.dat','wb') as pickle_file:
            pickle.dump(self.ethernet_kordy,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты у коммутатора',self.ethernet_kordy)
        with open('netdata\\serverkordx.dat','wb') as pickle_file:
            pickle.dump(self.server_kordx,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты х сервера',self.server_kordx)
        with open('netdata\\serverkordy.dat','wb') as pickle_file:
            pickle.dump(self.server_kordy,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('координаты у сервера',self.server_kordy)
        with open('netdata\\ethernet_prov.dat','wb') as pickle_file:
            pickle.dump(self.ethernet_prov,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Массив дополнительных линий ETHERNET',self.ethernet_prov)
        with open('netdata\\wifi_prov.dat','wb') as pickle_file:
            pickle.dump(self.wifi_prov,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Массив допольнительных линий WIFI',self.wifi_prov)
        with open('netdata\\line_ethernet_kordy_mass.dat','wb') as pickle_file:
            pickle.dump(self.line_ethernet_kordy_mass,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Массив координат главной линии ETHERNET',self.line_ethernet_kordy_mass)
        with open('netdata\\line_wifi_kordy_mass.dat','wb') as pickle_file:
            pickle.dump(self.line_wifi_kordy_mass,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Массив координат главной линии WIFI',self.line_wifi_kordy_mass)
        with open('netdata\\main_line_ethernet_count.dat','wb') as pickle_file:
            pickle.dump(self.main_line_ethernet_count,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Счётчик главных линий ETHERNET',self.main_line_ethernet_count)
        with open('netdata\\main_line_wifi_count.dat','wb') as pickle_file:
            pickle.dump(self.main_line_wifi_count,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Счётчик главных линий WIFI',self.main_line_wifi_count)
        with open('netdata\\dop_line_ethernet_count.dat','wb') as pickle_file:# С этого места
            pickle.dump(self.dop_line_ethernet_count,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Счётчик дополнительных линий езернет',self.dop_line_ethernet_count)
        with open('netdata\\line_tag.dat','wb') as pickle_file:
            pickle.dump(self.line_tag,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Список тегов на дополнительные линии', self.line_tag)
        with open('netdata\\wid_line_ethernet_mass.dat','wb') as pickle_file:
            pickle.dump(self.wid_line_ethernet_mass,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Список номеров линий',self.wid_line_ethernet_mass)
        with open('netdata\\dop_line_wifi_count.dat','wb') as pickle_file:
            pickle.dump(self.dop_line_wifi_count,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Счётчик дополнительных линий вай-фай',self.dop_line_wifi_count)
        with open('netdata\\line_tag_wifi.dat','wb') as pickle_file:
            pickle.dump(self.line_tag_wifi,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Список тегов вай фай доп. линий', self.line_tag_wifi)
        with open('netdata\\wid_line_wifi_mass.dat','wb') as pickle_file:
            pickle.dump(self.wid_line_wifi_mass,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Номер дополнительных линий вай фай',self.wid_line_wifi_mass)
        with open('netdata\\dop_ethernet_x.dat','wb') as pickle_file:
            pickle.dump(self.dop_ethernet_x,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Координаты х доп.линий езернет',self.dop_ethernet_x)
        with open('netdata\\dop_ethernet_y.dat','wb') as pickle_file:
            pickle.dump(self.dop_ethernet_y,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Координаты у доп.линий езернет',self.dop_ethernet_y)
        with open('netdata\\dop_wifi_x.dat','wb') as pickle_file:
            pickle.dump(self.dop_wifi_x,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Координаты х доп.линий вай фай',self.dop_wifi_x)
        with open('netdata\\dop_wifi_y.dat','wb') as pickle_file:
            pickle.dump(self.dop_wifi_y,pickle_file,pickle.HIGHEST_PROTOCOL)
            print('Координаты у допюлиний вай фай', self.dop_wifi_y)
        self.tx_error.configure(state=tk.NORMAL)
        self.tx_error.insert(1.0,str(datetime.now())+': Сохранение завершено.\n')
        self.tx_error.configure(state=tk.DISABLED)
# Загрузка всего проекта//M011
    def loadprog (self):
        self.tx_error.configure(state=tk.NORMAL)
        self.tx_error.insert(1.0,str(datetime.now())+': Загрузка данных...\n')
        self.tx_error.configure(state=tk.DISABLED)
        with open('netdata\\dop_ethernet_x.dat','rb') as pickle_file:
            self.dop_ethernet_x = pickle.load(pickle_file)
            print('Загрузка координат доп.линий езернет х', self.dop_ethernet_x)
        with open('netdata\\dop_ethernet_y.dat','rb') as pickle_file:
            self.dop_ethernet_y = pickle.load(pickle_file)
            print('Загрузка координат у доп.линий езернет', self.dop_ethernet_y)
        with open('netdata\\dop_wifi_x.dat','rb') as pickle_file:
            self.dop_wifi_x = pickle.load(pickle_file)
            print('Загрузка координат х доп.линий вай фай',self.dop_wifi_x)
        with open('netdata\\dop_wifi_y.dat','rb') as pickle_file:
            self.dop_wifi_y = pickle.load(pickle_file)
            print('Загрузка координат у доп.линий вай фая', self.dop_wifi_y)
        with open("data\\kordx.dat","rb") as pickle_file:
            self.kordx = pickle.load(pickle_file)
            print(self.kordx)
        with open("data\\kordy.dat","rb") as pickle_file:
            self.kordy = pickle.load(pickle_file)
            print(self.kordy)
        with open("data\\mist.dat","rb") as pickle_file:
            self.mist = pickle.load(pickle_file)
            print(self.mist)
        with open("data\\pidr.dat","rb") as pickle_file:
            self.pidr = pickle.load(pickle_file)
            print(self.pidr)
        with open("data\\count1.dat","rb") as pickle_file:
            self.count1 = pickle.load(pickle_file)
            print('Счётчик',self.count1)
        with open("data\\trendx1.dat","rb") as pickle_file:
            self.nowz = pickle.load(pickle_file)
        with open("data\\trendy1.dat","rb") as pickle_file:
            self.zap = pickle.load(pickle_file)
        with open("data\\kordxl.dat","rb") as pickle_file:
            self.kordxl = pickle.load(pickle_file)
            print(self.kordxl)
        with open("data\\kordyl.dat","rb") as pickle_file:
            self.kordyl = pickle.load(pickle_file)
            print(self.kordyl)
        with open("data\\textl.dat","rb") as pickle_file:
            self.textl = pickle.load(pickle_file)
            print(self.textl)
        with open('data\\kordxs.dat','rb') as pickle_file:
            self.kordxs = pickle.load(pickle_file)
            print(self.kordxs)
        with open('data\\kordys.dat','rb') as pickle_file:
            self.kordys = pickle.load(pickle_file)
            print(self.kordys)
        with open('data\\nachs.dat','rb') as pickle_file:
            self.nachs = pickle.load(pickle_file)
            print(self.nachs)
        with open('data\\konchs.dat','rb') as pickle_file:
            self.konchs = pickle.load(pickle_file)
            print(self.konchs)
        with open('data\\kordxe.dat','rb') as pickle_file:
            self.kordxe = pickle.load(pickle_file)
            print(self.kordxe)
        with open('data\\kordye.dat','rb') as pickle_file:
            self.kordye = pickle.load(pickle_file)
            print(self.kordye)
        with open('data\\tage.dat','rb') as pickle_file:
            self.tage = pickle.load(pickle_file)
            print(self.tage)
        with open('data\\countl.dat','rb') as pickle_file:
            self.countl = pickle.load(pickle_file)
            print(self.countl)
        with open('data\\counte.dat','rb') as pickle_file:
            self.counte = pickle.load(pickle_file)
            print(self.counte)
        with open('data\\counts.dat','rb') as pickle_file:
            self.counts = pickle.load(pickle_file)
            print(self.counts)
        with open('netdata\\unicount.dat','rb') as pickle_file:
            self.UNI_count = pickle.load(pickle_file)
            print('Счётчик уно вайфай',self.UNI_count)
        with open('netdata\\unikordx.dat','rb') as pickle_file:
            self.UNI_kordx = pickle.load(pickle_file)
            print('координаты х уно вай фай',self.UNI_kordx)
        with open('netdata\\unikordy.dat','rb') as pickle_file:
            self.UNI_kordy = pickle.load(pickle_file)
            print('координаты у уно вай фай',self.UNI_kordy)
        with open('netdata\\uni1count.dat','rb') as pickle_file:
            self.UNI_1_count = pickle.load(pickle_file)
            print('счётчик уно',self.UNI_1_count)
        with open('netdata\\uni1kordx.dat','rb') as pickle_file:
            self.UNI_1_kordx = pickle.load(pickle_file)
            print('координаты х уно',self.UNI_1_kordx)
        with open('netdata\\uni1kordy.dat','rb') as pickle_file:
            self.UNI_1_kordy = pickle.load(pickle_file)
            print('координаты у уно',self.UNI_1_kordy)
        with open('netdata\\nanocount.dat','rb') as pickle_file:
            self.nano_count = pickle.load(pickle_file)
            print('счётчик нано',self.nano_count)
        with open('netdata\\nanokordx.dat','rb') as pickle_file:
            self.nano_kordx = pickle.load(pickle_file)
            print('координаты х нано',self.nano_kordx)
        with open('netdata\\nanokordy.dat','rb') as pickle_file:
            self.nano_kordy = pickle.load(pickle_file)
            print('координаты у нано',self.nano_kordy)
        with open('netdata\\megacount.dat','rb') as pickle_file:
            self.mega_count = pickle.load(pickle_file)
            print('счётчик мега',self.mega_count)
        with open('netdata\\megakordx.dat','rb') as pickle_file:
            self.mega_kordx = pickle.load(pickle_file)
            print('координаты х мега',self.mega_kordx)
        with open('netdata\\megakordy.dat','rb') as pickle_file:
            self.mega_kordy = pickle.load(pickle_file)
            print('уоординаты у мега',self.mega_kordy)
        with open('netdata\\ethernetcount.dat','rb') as pickle_file:
            self.ethernet_count = pickle.load(pickle_file)
            print('счётчик коммутатора',self.ethernet_count)
        with open('netdata\\ethernetkordx.dat','rb') as pickle_file:
            self.ethernet_kordx = pickle.load(pickle_file)
            print('координаты х коммутатора',self.ethernet_kordx)
        with open('netdata\\ethernetkordy.dat','rb') as pickle_file:
            self.ethernet_kordy = pickle.load(pickle_file)
            print('координаты у коммутатора',self.ethernet_kordy)
        with open('netdata\\servercount.dat','rb') as pickle_file:
            self.server_count = pickle.load(pickle_file)
            print('счётчик сервера',self.server_count)
        with open('netdata\\serverkordx.dat','rb') as pickle_file:
            self.server_kordx = pickle.load(pickle_file)
            print('координаты х сервера',self.server_kordx)
        with open('netdata\\serverkordy.dat','rb') as pickle_file:
            self.server_kordy = pickle.load(pickle_file)
            print('координаты у сервера',self.server_kordy)
        with open('netdata\\ethernet_prov.dat','rb') as pickle_file:
            self.ethernet_prov = pickle.load(pickle_file)
            print ('Загрузка массива дополнительных ETHERNET линий', self.ethernet_prov)
        with open('netdata\\wifi_prov.dat','rb') as pickle_file:
            self.wifi_prov = pickle.load(pickle_file)
            print ('Загрузка массива дополнительных WIFI линий',self.wifi_prov)
        with open('netdata\\line_ethernet_kordy_mass.dat','rb') as pickle_file:
            self.line_ethernet_kordy_mass = pickle.load(pickle_file)
            print('Загрузка массива координат гланых линий ETHERNET',self.line_ethernet_kordy_mass)
        with open('netdata\\line_wifi_kordy_mass.dat','rb') as pickle_file:
            self.line_wifi_kordy_mass = pickle.load(pickle_file)
            print('Загрузка массива координат главных линий WIFI',self.line_wifi_kordy_mass)
        with open('netdata\\main_line_ethernet_count.dat','rb') as pickle_file:
            self.main_line_ethernet_count = pickle.load(pickle_file)
            print('Загрузка счётчика главных линий ETHERNET', self.main_line_ethernet_count)
        with open('netdata\\main_line_wifi_count.dat','rb') as pickle_file:
            self.main_line_wifi_count = pickle.load(pickle_file)
            print('Загрузка счётчика главных линий WIFI', self.main_line_wifi_count)
        with open('data\\name_page.dat','rb') as pickle_file:#
            self.name_page = pickle.load(pickle_file)#
        with open('data\\count_page.dat','rb') as pickle_file:#
            self.count_page = pickle.load(pickle_file)#
            print('Загрузка счётчика страниц', self.count_page)#
        with open('netdata\\dop_line_ethernet_count.dat','rb') as pickle_file:
            self.dop_line_ethernet_count = pickle.load(pickle_file)
            print('Загрузка счётчика дополнительных линий езернет',self.dop_line_ethernet_count)
        with open('netdata\\line_tag.dat','rb') as pickle_file:
            self.line_tag = pickle.load(pickle_file)
            print('Загрузка тегов доп.линий езернет', self.line_tag)
        with open('netdata\\wid_line_ethernet_mass.dat','rb') as pickle_file:
            self.wid_line_ethernet_mass = pickle.load(pickle_file)
            print('Загрузка списка номеров доп.линий езернет', self.wid_line_ethernet_mass)
        with open('netdata\\dop_line_wifi_count.dat','rb') as pickle_file:
            self.dop_line_wifi_count = pickle.load(pickle_file)
            print('Загрузка счётчика доп.линий вай фай',self.dop_line_wifi_count)
        with open('netdata\\line_tag_wifi.dat','rb') as pickle_file:
            self.line_tag_wifi = pickle.load(pickle_file)
            print('Загрузка тегов доп.линий вай фая',self.line_tag_wifi)
        with open('netdata\\wid_line_wifi_mass.dat','rb') as pickle_file:
            self.wid_line_wifi_mass = pickle.load(pickle_file)
            print('Загрузка списка номеров доп.линий вай фая', self.wid_line_wifi_mass)
        print(self.kordx,self.kordy,self.mist,self.pidr,self.count1,self.nowz,self.zap,self.kordxl,self.kordyl,self.textl,self.kordxs,self.kordys,self.nachs,self.konchs,self.kordxe,self.kordye,self.tage,self.countl,self.counte,self.counts)
            
        print ("Загружаю с текстовика")
        self.count=self.count1
        self.tx_error.configure(state=tk.NORMAL)
        self.tx_error.insert(1.0,str(datetime.now())+': Загрузка завершена.\n')
        self.tx_error.configure(state=tk.DISABLED)
        self.newButton1()

# Обновление лейбла на основной странице //M101
    def button_press(self):
        if self.go:
            self.go = False
            self.button.config(text = 'Click me')
        else:
            self.go = True
            self.th = threading.Thread(target = self.th_foo)
            self.th.start()
            self.button.config(text = 'Stop me')

    def th_foo(self):
        while self.go:
            self.label2.config(text = self.result)
            self.label2.update()
            time.sleep(0.1)


# Сердце проекта, сервер//M202
    def threaded(self,c,addrs):
        self.tx_error.configure(state=tk.NORMAL)
        self.tx_error.insert(1.0,str(datetime.now())+': Подключен клиент.\n')
        self.tx_error.configure(state=tk.DISABLED)
        print('nw',addrs)
        main_count = self.server_data_count
        self.server_data_count +=1
        count_table = 0
        while True:
            data = c.recv(1024)
            self.matrix_table.clear()
            #print('Получил', data)
            if not data:
                print('Bye')
                self.btn.config(bg='grey95') 
                break
            self.c = list(data)                                                         # Переводим всю полученную информацию в список,сейчас используем для расшифровки аналоговых датчиков(работает)
            brt = str(self.c[12]-48)+str(self.c[13]-48)+str(self.c[14]-48)              # Кустарным способом преобразуем ASCII в str целых чисел,а не табличных                
            self.now = str(datetime.now())                                              # Момент для нормальной работы тренда, мы получаем каждый цикл данные и успеваем записать именно строчку в массив, для дальнейшего использования
            self.nowz.append(self.now)                                                  # Добавляем в конец массива новое время
            self.zap.append(int(brt))                                                   # Добавляем в конец массива новые данные с датчика (требует шкалирования)
            #print('массив',self.c)
            global result
            self.result = data                                                          # Записываем всю полученную инфу с клиента на self.result для дальнейшего использования программой
            self.result_tab[main_count] = data
            self.r = str
            self.r = str(self.c[2])                                                     # Тест отправки сигнала от сервера к клиенту, сейчас отключен
            global plt8                                                                 # self.cose - полностью собранный массив, который мы отправляем на клиент, пока что тут записанны только дискреты, но аналог будет записан по аналогии
            self.cose = str
            self.cose = list(str(self.pin2)+str(self.pin3)+str(self.pin4)+str(self.pin5)+str(self.pin6)+str(self.pin7)+str(self.pin8)+str(self.pin9)+str(self.pin10)+str(self.pin11)+str(self.pin12)+str(self.pin13))
            c.send(str(self.cose).encode('ascii'))                                      # Кодируем и отправляем на клиент
            #print('Отправил ',self.cose)
            #if count_table == 0:
            #    self.addfuntrd_training_1() 
            #    count_table +=1
            self.testing_conv = a = regex.findall(r'\X', str(self.result)) # конвертируем пакет в int
            mas = [a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],(a[14],a[15],a[16]),(a[17],a[18],a[19]),(a[20],a[21],a[22]),(a[23],a[24],a[25]),(a[26],a[27],a[28]),(a[29],a[30],a[31])] # Формируем массив таблицы из результата сервера
            count = len(mas)
            count_1 = 0
            mas_1 = ['']
            for count_1 in range(count):
                mas_1 = mas[count_1]
                self.matrix_table.append([self.name_uno[0],'1.'+str(count_1),mas_1,self.tag_symv_tab[count_1],self.comments_symv[count_1]])#(a[50],a[51],a[52])
                count_1 +=1
            b = str(self.testing_conv[14])+str(self.testing_conv[15])+str(self.testing_conv[16])
            inter = ((1/1023)*(int(b)+1))*100 # шкалирование от 0 до 100
            print('sever')
        c.close()
    # Ожидание нового подключения с дальнейшим выделением в новый поток //M202
    def raos (self):
        self.tx_error.configure(state=tk.NORMAL)
        self.tx_error.insert(1.0,str(datetime.now())+': Запуск сервера...\n')
        self.tx_error.configure(state=tk.DISABLED)
        host = ""
        port = 10000
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(10)
        self.btn.config(bg='green')
        self.main_link_test = 1
        while True:
            sock, addr = s.accept()
            print('Connected to :', addr[0], ':', addr[1])
            addrs = addr[0]
            start_new_thread(self.threaded, (sock,addrs))
            
# Тут пошли жестко забитые пины ардуина/тест для тегов //M202
    def pin2on(self):
        global pin2
        if self.pin2 == 0:
            self.pin2 = 1
        else:
            self.pin2 = 0

    def pin3on(self):
        global pin3
        if self.pin3 == 0:
            self.pin3 = 1
        else:
            self.pin3 = 0

    def pin4on(self):
        global pin4
        if self.pin4 == 0:
            self.pin4 = 1
        else:
            self.pin4 = 0

    def pin5on(self):
        global pin5
        if self.pin5 == 0:
            self.pin5 = 1
        else:
            self.pin5 = 0

    def pin6on(self):
        global pin6
        if self.pin6 == 0:
            self.pin6 = 1
        else:
            self.pin6 = 0

    def pin7on(self):
        global pin7
        if self.pin7 == 0:
            self.pin7 = 1
        else:
            self.pin7 = 0

    def pin8on(self):
        global pin8
        if self.pin8 == 0:
            self.pin8 = 1
        else:
            self.pin8 = 0

    def pin9on(self):
        global pin9
        if self.pin9 == 0:
            self.pin9 = 1
        else:
            self.pin9 = 0

    def pin10on(self):
        global pin10
        if self.pin10 == 0:
            self.pin10 = 1
        else:
            self.pin10 = 0

    def pin11on(self):
        global pin11
        if self.pin11 == 0:
            self.pin11 = 1
        else:
            self.pin11 = 0

    def pin12on(self):
        global pin12
        if self.pin12 == 0:
            self.pin12 = 1
        else:
            self.pin12 = 0


    def pin13on(self):
        global pin13
        if self.pin13 == 0:
            self.pin13 = 1
        else:
            self.pin13 = 0
            

# Реализация присваивания новой кнопке, через заведомо созданные "теги", функция работает, но требует пересмотра, когда будет добавлен новый контроллер //M104
    def vizov(self,which,event=None):
        print ('присвоили ',self.knop)
        print ('взяли номер для массива ',which)
        print ('массив ',self.mist)
        print ('счётчик ',self.count)
        self.knop = (self.mist [int(which)])
        index_but = self.tag_symv_tab.index(self.knop)
        print(index_but)
        if index_but == 13:
            self.pin13on()
        elif index_but == 12:
            self.pin12on()
        elif index_but == 11:
            self.pin11on()
        elif index_but == 10:
            self.pin10on()
        elif index_but == 9:
            self.pin9on()
        elif index_but == 8:
            self.pin8on()
        elif index_but == 7:
            self.pin7on()
        elif index_but == 6:
            self.pin6on()
        elif index_but == 5:
            self.pin5on()
        elif index_but == 4:
            self.pin4on()
        elif index_but == 3:
            self.pin3on()
        elif index_but == 2:
            self.pin2on()
        else:
            index_but = 0


# Создание новой кнопки через тКинтер //M103
    def button2(self):        
        global xex
        global yey
        global knop
        global pidr
        global mist
        self.xex = self.w
        self.xex = self.window.winfo_pointerx ()                                                             # Снова берем координаты
        self.kordx.append (self.xex)
        self.yey = self.window.winfo_pointery ()
        self.kordy.append (self.yey)
        self.nm = self.show.get()                                                           # Вытаскиваем с окна ввода данные и записываем в переменную(имя кнопки)
        self.pidr.append(self.nm)
        self.cmd = self.show1.get()                                                         # Вытаскиваем с окна ввода данные и записываем в переменную(команда)
        self.mist.append(self.cmd)
        self.newButton = tkinter.Button(self.canvas1, text=self.nm, command= lambda which=self.count : self.vizov(which))            # Сам процесс создания кнопки, каждая кнопка записывается в ячейку массива, а потом через счетчик и записанные массивы воспроизводится
        self.newButton.place(x =self.xex, y =self.yey)
        self.count +=1
        self.newWindow.destroy()

# Создание статичного текста //M103
    def label21(self):        
        global xex
        global yey
        global knop
        global pidr
        global mist
        print ('Создаю лейбл')
        self.xex = self.window.winfo_pointerx ()                                            
        self.kordxl.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.kordyl.append(self.yey)
        self.nm1 = self.show2.get()                                                           
        self.textl.append(self.nm1)
        self.newLabel = tk.Label(self.frame1, text=self.nm1,bg ='#DEF7FE')            
        self.newLabel.place(x =self.xex, y =self.yey)
        self.countl +=1
        self.newWindow1.destroy()

# Создание окна ввода //M103
    def yntry211(self):        
        global xex
        global yey
        global knop
        global pidr
        global mist
        print ('окно ввода')
        self.xex = self.window.winfo_pointerx ()                                            
        self.kordxe.append(self.xex)
        self.yey = self.window.winfo_pointery ()
        self.kordye.append(self.yey)
        self.nm2 = self.show3.get()                                                           
        self.tage.append(self.nm2)
        self.newEntry = tk.Entry(self.frame1, width=30)            
        self.newEntry.place(x =self.xex, y =self.yey)
        self.counte +=1
        self.newWindow.destroy()

# Окно создания новой кнопки, нужно переделать все на ивенты //M102
    def createNewWindow(self):
        self.newWindow = tk.Toplevel(self.window)
        self.newWindow.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.newWindow,text='Имя')
        f_bot = LabelFrame(self.newWindow,text='Тег')  
        labelExample = tk.Label(self.newWindow, text = "Новая кнопка")
        namm = tk.Label(f_top,text="Введите имя кнопки:")
        self.show = tk.Entry(f_top,width=30)
        namn1 = tk.Label(f_bot,text="Введите тег:")
        self.show1 = ttk.Combobox(f_bot,values = self.tag_symv_tab) 
        buttonExample = tk.Button(self.newWindow, text = "Создать",command = self.button2)
        f_top.pack(padx=10,pady=10)
        namm.pack(side = LEFT,padx = 5, pady = 5)                                                                             # Пакуем, чтобы не заебыватся как оно расположенно, идет сверху вниз
        self.show.pack(side = LEFT,padx = 5, pady = 5)
        f_bot.pack(padx=10,pady=10)
        namn1.pack(side = LEFT,padx = 5, pady = 5)
        self.show1.pack(side = LEFT,padx = 5, pady = 5)
        labelExample.pack()
        buttonExample.pack()

# Окно создания скейла //M102
    def createNewWindow3(self):
        self.newWindow3 = tk.Toplevel(self.window)
        self.newWindow3.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.newWindow3,text='Минимум')
        f_bot = LabelFrame(self.newWindow3,text='Максимум')
        f_fot = LabelFrame(self.newWindow3,text='Тег')
        labelExample = tk.Label(self.newWindow3, text = "Новую шкалу")
        namm = tk.Label(f_top,text="Введите от :")
        self.show4 = tk.Entry(f_top,width=30)
        namm2 = tk.Label(f_bot,text="Введите до :")
        self.show5 = tk.Entry(f_bot,width=30)
        namn3 = tk.Label(f_fot,text='Введите тег :')
        show5 = ttk.Combobox(f_bot,values = self.tag_symv_tab) 
        buttonExample3 = tk.Button(self.newWindow3, text = "Создать шкалу",command = self.newScale)
        f_top.pack(padx=10,pady=10)
        namm.pack(side = LEFT,padx = 5, pady = 5)                                                                          
        self.show4.pack(side = LEFT,padx = 5, pady = 5)
        f_bot.pack(padx=10,pady=10)
        namm2.pack(side = LEFT,padx = 5, pady = 5)
        self.show5.pack(side = LEFT,padx = 5, pady = 5)
        f_fot.pack(padx=10,pady=10)
        namn3.pack(side = LEFT,padx = 5, pady = 5)
        show5.pack(side = LEFT,padx = 5, pady = 5)
        labelExample.pack(padx = 5, pady = 5)
        buttonExample3.pack()


# Окно создания надписи //M102
    def createNewWindow1(self):
        self.newWindow1 = tk.Toplevel(self.window)
        self.newWindow1.iconbitmap('image//rao_inc.ico')
        f_top = LabelFrame(self.newWindow1,text='Имя')
        f_bot = LabelFrame(self.newWindow1,text='Текст')  
        labelExample = tk.Label(self.newWindow1, text = "Новый текст")
        namm = tk.Label(f_bot,text="Текст:")
        self.show2 = tk.Entry(f_bot,width=30)
        buttonExample1 = tk.Button(self.newWindow1, text = "Создать лейбл",command = self.label21)
        f_bot.pack(padx=10,pady=10)
        namm.pack(side = LEFT,padx = 5, pady = 5)                                                                          
        self.show2.pack(side = LEFT,padx = 5, pady = 5)
        labelExample.pack(padx = 5, pady = 5)
        buttonExample1.pack()


# Окно создания окна ввода //M102
    def createNewWindow2(self):
        self.newWindow = tk.Toplevel(self.window)
        self.newWindow.iconbitmap('image//rao_inc.ico')
        #f_top = LabelFrame(self.newWindow,text='Имя')
        f_bot = LabelFrame(self.newWindow,text='Тег')  
        labelExample = tk.Label(self.newWindow, text = "Новое окно ввода")
        namn1 = tk.Label(f_bot,text="Введите тег:")
        self.show3 = ttk.Combobox(f_bot,values = self.tag_symv_tab) 
        buttonExample2 = tk.Button(self.newWindow, text = "Создать",command = self.yntry211)
        f_bot.pack(padx=10,pady=10)
        namn1.pack(side = LEFT,padx = 5, pady = 5)
        self.show3.pack(side = LEFT,padx = 5, pady = 5)
        labelExample.pack(padx = 5, pady = 5)
        buttonExample2.pack()

    
if __name__ == '__main__':
        
    raoconnect() 
    
