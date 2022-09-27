def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    left = []
    right = []
    pivot = numbers[len(numbers)//2]

    for i in range(len(numbers)):
        if i == (len(numbers)//2):
            continue

        if pivot > numbers[i]:
            left.append(numbers[i])
        else:
            right.append(numbers[i])

    return quick_sort(left) + [pivot] + quick_sort(right)



numbers_1 = [11,45,23,81,28,34]
numbers_2 = [11,45,22,81,23,34,99,22,17,8]
numbers_3 = [1,1,1,1,1,0,0,0,0,0]
numbers_4 = [1,-2,-4,2,6]

numbers_1 = quick_sort(numbers_1)
numbers_2 = quick_sort(numbers_2)
numbers_3 = quick_sort(numbers_3)
numbers_4 = quick_sort(numbers_4)

print(numbers_1)
print(numbers_2)
print(numbers_3)
print(numbers_4)