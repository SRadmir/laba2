# Это лабораторная работа №2 
## задание 1 ##
### код
```
import datetime
def qwerty(dr0, dr1, dr2):
         if 0<=int(dr0)<=31 and 1<=int(dr1)<=12 and 0<=int(dr2)<= datetime.date.today().year:
                                        if (int(dr0)<=30 and (int(dr1)==4 or int(dr1)==6 or int(dr1)==9 or int(dr1)==11)) or (int(dr0)<=31 and (int(dr1)==1 or int(dr1)==3 or int(dr1)==5 or int(dr1)==7 or int(dr1)==8 or int(dr1)==10 or int(dr1)==12))\
                                                or ((int(dr2)%10==4 or int(dr2)%10==0) and int(dr1)==2 and(1<=int(dr0)<=29) or (int(dr1)==2 and (int(dr2)%10!=4 or int(dr2)%10!=0) and 1<=int(dr0)<=28)):
                                                return True
def d():
        while True:
                try:
                        dr=input("Введите дату рождения в формате дд.мм.гггг")
                        if dr.lower != 'stop':
                                dr = dr.split('.')
                                td= datetime.date.today()
                                if qwerty(dr[0],dr[1],dr[2]):
                                        if td.month>int(dr[1]):
                                                print(f' Вам - {td.year-int(dr[2])}')
                                        elif td.month<int(dr[1]):
                                                print(f'Вам - {td.year-int(dr[2])-1}')
                                        else:
                                                if td.day>int(dr[0]):
                                                        print(f'Вам - {td.year-int(dr[2])}')
                                                elif td.day==int(dr[0]):
                                                        print(f"C Днем Рожденя, вам - {td.year-int(dr[2])} лет")
                                                else:
                                                        print(f' Вам - {td.year-int(dr[2])-1}')
                                if not qwerty(dr[0],dr[1],dr[2]):
                                                print("Неверный формат даты рождения")
                                else:
                                        break
                except ValueError:
                                print("Неверный формат даты рождения")
                except IndexError:
                                print("Неверный формат даты рождения")
d()

```
## задание 2 ##
### код
```
from random import randint
while True:
        a = input("Введите цифру - ")
        if a == 'stop':
                print("1stop1")
                break
        else:
                l=['1', '2', '3', '4', '5', '6', '7', '8' , '9']
                if a in l:
                        lst=[randint(0, 200) for i in range(10)]
                        newlst = list(filter(lambda x: (x%int(a)==0), lst))
                        print(f'Список кратных чисел {newlst}')
                        print(f'Рандомный список{lst}')
                        continue
                else:
                        print("Ошибка ввода")
                        continue
```
## задание 3 ##
### код
```
def getnumber():
        lst= []
        for i in range(30):
                if i % 2 != 0:
                        lst.append(i)
        yield lst
a= getnumber()
lst1=[]
for q in a:
        lst1.append(q)
print(f"первое значение - {lst1[0][0]}, пятое значение - {lst1[0][4]}, последнее значение - {lst1[0][-1]}") 
```
## задание 4 ##
### код
```
def gq():
        if  gamer== 'бумага':
                return 0
        elif gamer== 'камень':
                return 1
        else:
                return 2
def game(gr, pc):
        if gr == 0:
                if pc==0:
                        stata.append("ничья")
                        return print("ничья")
                if pc == 1:
                        stata.append("победа")
                        return print("победа")
                if pc ==2:
                        stata.append("поражение")
                        return print("поражение")
        if gr == 1:
                if pc==0:
                        stata.append("поражение")
                        return print("поражение")
                if pc == 1:
                        stata.append("ничья")
                        return print("ничья")
                if pc ==2:
                        stata.append("победа")
                        return print("победа")
        if gr ==2:
                if pc==0:
                        stata.append("поражение")
                        return print("поражение")
                if pc == 1:
                        stata.append("победа")
                        return print("победа")
                if pc ==2:
                        stata.append("ничья")
                        return print("ничья")
import random
lst = ["бумага", "камень", "ножницы"]
stata= []
while True:
        gamer = input("Выбор бумага/камень/ножницы").lower()
        if gamer =="stop":
                print(f'Кол-во сыгранных матчей - {len(stata)}')
                print(f'Кол-во побед - {stata.count("победа")}')
                print(f'Кол-во ничьих - {stata.count("ничья")}')
                print(f'Кол-во проигрышей - {stata.count("поражение")}')
                break
        else:
                if gamer in lst:
                        gr= gq()
                        pc = random.randint(0, 2)
                        result= game(gr, pc)
                        if result == "победа":
                                print("Победа!")
                        elif result=="поражение":
                                print("Поражение")
                        elif result == "ничья":
                                print("ничья")
                if not gamer in lst:
                        print("Неверно")
```