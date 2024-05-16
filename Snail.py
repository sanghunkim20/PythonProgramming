arr =[]
num = 1

for i in range(5):
    arr.append([])
    for j in range(3):
        arr[i].append(num)
        num += 1

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print("\n", end="")