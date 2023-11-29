def quicksort3(arr):
    if len(arr) <= 1:
        return arr
    if len(arr)%2 == 0:
        pivot_idx = len(arr) // 2 -1
    else:
        pivot_idx = len(arr) // 2
    pivot = arr[pivot_idx]
    print("PIIIVOOOOOOOOOT!!", pivot)
    left, right = [], []

    for i in range(len(arr)):
        if i == pivot_idx:
            continue
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quicksort3(left) + [pivot] + quicksort3(right)


quicksort3([14,1,2,6,11,8,5,9,4,3,10,7,12,13])