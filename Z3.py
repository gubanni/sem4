import random
def InputNumber():
    is_OK = False
    while not is_OK:
        try:
            number = int(input("Введите натуральную степень k: "))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def write_file(st):
    with open('fZ3.md', 'w') as data:
        data.write(st)

def createkoef(k):
    list = []
    for i in range(k+1):
        list.append(random.randint(0,101))
    return list
    

def createmn(koef):
    lst= koef[::-1]
    st = ''
    if len(lst) < 1:
        st = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                st += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    st += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                st += f'{lst[i]}x'
                if lst[i+1] != 0:
                    st += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                st += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                st += ' = 0'
    return st

k = InputNumber()
koef = createkoef(k)
write_file(createmn(koef))