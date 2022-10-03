stack = []
# Торубара Даниил, 922403
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    ele = int(input())
  
    stack.append(ele)

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
    
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

quick_sort(stack, 0, len(stack) - 1)
print(stack)