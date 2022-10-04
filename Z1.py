def InputNumber():
    is_OK = False
    while not is_OK:
        try:
            number = int(input("Введите число: "))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def listofmnoz(number):
    lst = []
    i = 2
    num = number
    while i <= num:
        if num % i == 0:
            lst.append(i)
            num //= i
            i = 2
        else:
            i += 1
    return lst


number = InputNumber()
list = listofmnoz(number)

print(f"Простые множители числа {number} приведены в списке: {list}")