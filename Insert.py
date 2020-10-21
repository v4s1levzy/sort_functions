import random

dim = 20
arr = [random.randint(0, 100) for i in range(dim)]

print("Исходный массив")
print(arr)

n = 1
alg_count = [0, 0]

# alg_count = 0       счетчик перестановок
# alg_count = 1       счетчик сравнений    

for i in range(1, dim):  
        temp = arr[i]  
        j = i - 1
        while j >= 0:  
            alg_count[0] += 1  
            if arr[j] > temp:
                alg_count[1] += 1  
                arr[j + 1] = arr[j]  
                arr[j] = temp
            j -= 1

print("\nУпорядоченный массив: метод простого выбора")
print(arr)
print("\nЭлементов в массиве: ", dim)
print("Сравнений: ", alg_count)
print("Перестановок: ", alg_count)

            
