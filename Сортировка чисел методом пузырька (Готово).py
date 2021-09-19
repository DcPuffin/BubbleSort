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
