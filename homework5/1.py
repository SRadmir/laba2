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
