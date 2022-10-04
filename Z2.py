def InputNumber():
    is_OK = False
    while not is_OK:
        try:
            number = int(input("Введите длину списка: "))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def createlist(n):
    xs = []
    for i in range(n):
        xs.append(int(input(f"Введите {i} элемент списка:")))
    return xs
def new_list(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list    
n = InputNumber()    
list = createlist(n)
new_list = new_list(list)
print(f"Исходный список: {list}")
print(f"Список из неповторяющихся элементов: {new_list}")