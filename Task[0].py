# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def GetNumber(message):
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            isCorrect = True
        except ValueError:
            print("Введено не число. Повторите! ")
    return number

def InitArray(number):
    array = []
    for i in range(number):
        array.append(randint(0,10))
    return array

def SumOdd(array):
    sum = 0
    for i in range(1,len(array),2):
        sum+=array[i]
    return sum

numb = GetNumber("Введите количество элементов: ")
newArray = InitArray(numb)
sum = SumOdd(newArray)
print(f'- {newArray} на нечётных позициях элементы {newArray[1]} и {newArray[3]}, ответ: {sum}')