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
