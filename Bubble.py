import random

dim = 20
arr = [random.randint(0, 100) for i in range(dim)]

print("Исходный массив")
print(arr)

n = 1
alg_count = [0, 0]

# alg_count[0] = 0       счетчик перестановок
# alg_count[1] = 0       счетчик сравнений

while n < dim:
    for i in range(dim - n):
        alg_count[0] += 1
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            alg_count[1] += 1
    n += 1
    
print("\nУпорядоченный массив: метод простого выбора")
print(arr)
print("\nЭлементов в массиве: ", dim)
print("Сравнений: ", alg_count[1])
print("Перестановок: ", alg_count[0])
