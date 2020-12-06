from tkinter import *
from beautifultable import BeautifulTable
h0=['Квартал', 'Номер магазина', 'Плановий товарообіг,грн.', 'Фактичний товарообіг,грн.', 'Планова численість,чол.', 'Фактична численість,чол.']
h1 = ['1 кв.', '1', '43102,6', '44568,1', '209', '189']
h2 = ['1 кв.', '6', '11707,2', '10922,8', '45', '40']
h3 = ['1 кв. ', '7', '5498,0', '5650,9', '20', '18']
h4 = ['2 кв.', '1', '52684,5', '51825,4', '200', '190']
h5 = ['2 кв.', '6', '15905,3', '16000,2', '46', '45']
h6 = ['2 кв.', '7', '6895,0', '7000,4', '25', '23']
h7 = ['3 кв.', '1', '68453,4', '68400,3', '198', '195']
h8 = ['3 кв.', '6', '14236,6', '14000,7', '45', '43']
h9 = ['3 кв.', '7', '7245,2', '7300,1', '23', '23']
h10 = ['4 кв.', '1', '7529,9  ', '7524,0', '22', '21']
h11 = ['4 кв.', '6', '1566,0 ', '1540,1', '5', '5']
h12 = ['4 кв.', '7', '797,0', '803,0 ', '3', '3']

ha0=['Квартал', 'Номер магазина', 'Фактична численість,чол.']
ha1 = ['1 кв.', '1', '189']
ha2 = ['1 кв.', '6', '40']
ha3 = ['1 кв.', '7', '18']
ha4 = ['2 кв.', '1', '190']
ha5 = ['2 кв.', '6', '45']
ha6 = ['2 кв.', '7', '23']
ha7 = ['3 кв.', '1', '195']
ha8 = ['3 кв.', '6', '43']
ha9 = ['3 кв.', '7', '23']
ha10 = ['4 кв.', '1', '21']
ha11 = ['4 кв.', '6', '5']
ha12 = ['4 кв.', '7', '3']


table = BeautifulTable()
table.column_headers = h0
table.append_row(h1)
table.append_row(h2)
table.append_row(h3)
table.append_row(h4)
table.append_row(h5)
table.append_row(h6)
table.append_row(h7)
table.append_row(h8)
table.append_row(h9)
table.append_row(h10)
table.append_row(h11)
table.append_row(h12)


atable = BeautifulTable()
atable.column_headers = ha0
atable.append_row(ha1)
atable.append_row(ha2)
atable.append_row(ha3)
atable.append_row(ha4)
atable.append_row(ha5)
atable.append_row(ha6)
atable.append_row(ha7)
atable.append_row(ha8)
atable.append_row(ha9)
atable.append_row(ha10)
atable.append_row(ha11)
atable.append_row(ha12)


hb0 = ['Номер магазина', 'Назва']
hb1 = ['1', 'Універсам №1']
hb2 = ['6', 'Галактон']
hb3 = ['7', 'Поляниця']


btable = BeautifulTable()
btable.column_headers = hb0
btable.append_row(hb1)
btable.append_row(hb2)
btable.append_row(hb3)

hbc0 = ['Назва магазина', 'Квартал', 'Товарообіг плановий', 'Товарообіг фактичний', 'Відсотки виконання', 'Продуктивність планова', 'Продуктивність фактична']
hbc1 = ['Галактон', '1 кв.', '11707,20', '10922,80', '93,30', '260,16', '273,07']
hbc2 = ['Галактон', '2 кв.', '15905,30', '16000,20', '100,60', '345,77 ', '355,56']
hbc3 = ['Галактон', '3 кв.', '14236,60', '14000,70', '98,34', '316,37', '325,60']
hbc4 = ['Галактон', '4 кв.', '1566,03', '1540,08 ', '98,34', '316,37', '325,60']
hbc5 = ['...', '...', '...', '...', '...', '...', '...']
hbc6 = ['Універсам №1', '1 кв.', '43102,60', '44568,10', '103,40', '206,23 ', '235,81']
hbc7 = ['Універсам №1', '2 кв.', '52684,50', '51825,40', '98,37', '263,42', '272,77']
hbc8 = ['Універсам №1', '3 кв.', '68453,40', '68400,30', '99,92 ', '345,72', '350,77']
hbc9 = ['Універсам №1', '4 кв.', '7529,87', '7524,03', '99,92', '345,72', '350,77']

bctable = BeautifulTable()
bctable.column_headers = hbc0
bctable.append_row(hbc1)
bctable.append_row(hbc2)
bctable.append_row(hbc3)
bctable.append_row(hbc4)
bctable.append_row(hbc5)
bctable.append_row(hbc6)
bctable.append_row(hbc7)
bctable.append_row(hbc8)
bctable.append_row(hbc9)



root = Tk()

def btn_click():
    print(table)
def abtn_click():
    print(atable)
def bbtn_click():
    print(btable)
def cbtn_click():
    print(bctable)

root ['bg'] = '#fafafa'
root.title('Таблиці')
root.wm_attributes('-alpha', 1)
root.geometry('600x400')


canvas = Canvas(root, height=600, width=400)
canvas.pack()

frame = Frame(root, bg='White')
frame.place(relwidth=0.7 , relheight=0.7)

title = Label(frame, text='таблиці', bg='green', font=40)
title.pack()
btn = Button(frame, text='таблиця 1', bg='white', command=btn_click)
btn.pack()
abtn = Button(frame, text='фільтрована таблиця 1', bg='white', command=abtn_click)
abtn.pack()
bbtn = Button(frame, text='таблиця 2', bg='white', command=bbtn_click)
bbtn.pack()
cbtn = Button(frame, text='таблиця 3', bg='white', command=cbtn_click)
cbtn.pack()

root.mainloop()
