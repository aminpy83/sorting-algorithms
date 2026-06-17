arr = [5, 4, 3, 2, 1]

for i in range(len(arr) - 1):
    smallest = i
    for j in range(i + 1, len(arr)):
        if arr[smallest] > arr[j]:
            smallest = j

    arr[smallest], arr[i] = arr[i], arr[smallest]
    print(arr)

# not selection sort
# for i in range(len(arr)):
#   least = min(arr[i:])
#   arr[arr.index(least)], arr[i] = arr[i], arr[arr.index(least)]
