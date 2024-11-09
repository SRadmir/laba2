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
