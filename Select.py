import random

dim = 20
arr = [random.randint(0, 100) for i in range(dim)]

print("Исходный массив")
print(arr)

# ccount = 0       счетчик перестановок
# mcount = 1       счетчик сравнений

k = 0
mcount = 0
ccount = 0
for k in range(dim - 1):
    m = k 
    i = k + 1 
    for i in range(i, dim):
        ccount += 1
        if arr[i] < arr[m]:
            m = i
    if k != m:
        t = arr[k]
        arr[k] = arr[m]
        arr[m] = t
        mcount += 1
 
print("\nУпорядоченный массив: метод простого выбора")
print(arr)
print("\nЭлементов в массиве: ", dim)
print("Сравнений: ", ccount)
print("Перестановок: ", mcount)
