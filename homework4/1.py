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
 
