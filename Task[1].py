# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] -> [12, 15, 16];
# - [2, 3, 5, 6] -> [12, 15]

import math
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

def InitArr(number):
    mass = []
    for i in range(number):
        mass.append(randint(0,10))
    return mass

def NewArr(mass):
    newMass = []
    for i in range(math.ceil(len(mass)/2)):
        newMass.append(mass[i]*mass[len(mass)-i-1])
    return newMass

numb = GetNumber('Введите количество элементов: ')
firstMass = InitArr(numb)
secondMass = NewArr(firstMass)
print(f'{firstMass} -> {secondMass}')