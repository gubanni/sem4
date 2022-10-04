def InputNumber(text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{text}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def calculate_nok(x, y): 
    if x > y: 
        greater = x 
    else: 
        greater = y 
    while(True): 
        if((greater % x == 0) and (greater % y == 0)): 
            nok = greater 
            break 
        greater += 1 
    return nok 
        
num1 = InputNumber("Введите первое число: ") 
num2 = InputNumber("Введите второе число: ") 
print(f"НОК чисел {num1} и {num2}: {calculate_nok(num1, num2)}")
