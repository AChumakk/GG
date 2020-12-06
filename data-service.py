"""Модуль призначено для роботи з вхідними даними
"""


def get_clients():
    """повертає список клієнтів з файла "dovidnik.txt"
    
    Returns:
       dovidnik_list : довідник
    """
    
    from_file = [
       "1;Масло",
       "2;Сир_твердий",
       "3;Молоко",
       "4;Сир",
       "5;Маргарин",
       "6;М'ясо",
       "7;Ковбаса",
       "8;Фарш_м'ясний",
       "9;М'ясо_кістки"
    ]
 
     # накопичувач
    dovidnik_list = []
    
    for line in from_file:
        line_list = line.split(';')
        dovidnik_list.append((line_list))
    
    return dovidnik_list

def show_dovidnik(dovidnik):
    """виводить на екран список довідника по заданій умові
 
    Args:
        dovidnik (list): список довідника
    """

dovidnik_code_frome = input("З якого код товару")
dovidnik_code_to    = input("По який код товару")

for tovar in dovidnik:
        print("код: {:2} назва: {:Сир_твердий}".format(dovidnik[0], dovidnik[1]))
    
dovidnik = get_clients()
    
for c in dovidnik:
    print(c)
    '''Ця функція виконує ряд завдань: заповнення текстового документу,
вивід з текстового документу строк, які нам потрібні двома шляхами 
завдяки циклам'''


h = open("C:\ICS-121\my_file\my_file.txt", 'w+')
'''Ця функція під'єднує текстовий файл до програми 
та додає функцію писати у ньому'''
i = 1
for i in range(10):

    h.write(str(i) + " строка\n")

    i + 1
    '''Це цикл, який заповнює 10 строк у текстовому документі'''

h.close()
'''Завершення роботи з текстовим документом'''

b = open("C:\ICS-121\my_file\myfile.txt", 'r')
'''Ця функція під'єднує текстовий файл до програми 
та додає функцію читати елементи, що знаходяться у документі'''
slist = []
k = 0
for k in range (5):
    stroka = b.readlines(k)
    slist.append(stroka)
    print(slist[k])
    k+1
    '''Цикл, що читає строки з текстового документу та додає їх у список,
    щоб вивести їх у подальшому на екран'''
b.close()

print('__')

with open("C:\ICS-121\my_file\my_file.txt") as sf:
    file = sf.readlines()
print(file)
'''Функція, що робить те ж сами, що й минула, але 
із застосуванням менеджера контенту'''