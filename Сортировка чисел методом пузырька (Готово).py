# Метод пузырька. Начало.
size = int(input("Введите, пожалуйста, положительный целочисленный размер массива: "))
if size <= 0:
    print("Некорректный размер массива!")
else:
    i = 0
    arr = []
    while i < size: # Создание массива
        print("Введите, пожалуйста, " + str(i+1) + "-й числовой элемент массива: ")
        n = int(input())
        arr.append(n)
        i = i+1
    i = 0
    j = 0
    while i < size:
        while j < (size-1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            j = j+1
        i = i+1
        j = 0
    arr.reverse()
    print("Отсортированный массив методом Пузырька: ", arr)
# Метод пузырька. Конец.
# Метод выборки. Начало.
size = int(input("Введите, пожалуйста, положительный целочисленный размер массива: "))
if size <= 0:
    print("Некорректный размер массива!")
else:
    i = 0
    arr = []
    while i < size: # Создание массива
        print("Введите, пожалуйста, " + str(i+1) + "-й числовой элемент массива: ")
        n = int(input())
        arr.append(n)
        i = i+1
    n = 0
    j = 0
    arra = []
    minus = 1
    minimal = 0
    while n < size:
        print(n)
        mini = n
        while j < (size-minus):
            if arr[j] < arr[mini]:
                mini = j
                minimal = arr[mini]
            j = j+1
        j = 0
        n = n+1
        minus = minus+1
        arra.append(minimal)
        del arr[mini]
    print(arr)
    print(arra)
# Метод выборки. Конец.
