arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = float(input("Enter element: "))   # accepts float and negative values
    arr.append(num)

# Selection Sort
for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array:")
print(arr)
