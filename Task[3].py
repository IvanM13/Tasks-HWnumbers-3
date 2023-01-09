# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
#- 2 -> 10

def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            isCorrect = True
        except ValueError:
            print("Введено не целое число. Повторите! ")
    return number

def Binary(number):
    my_list = ""
    while True:
        if int(number//2) == 0:
            my_list+='1'
            break
        else:
            my_list+=str(int(number%2))
            number/=2
    return my_list


numb = GetNumber('введите десятичное число: ')
m_list = Binary(numb)
print(f'{numb} -> {m_list[::-1]}')
