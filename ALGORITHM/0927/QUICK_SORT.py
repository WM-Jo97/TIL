def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    left  = [] # 기준보다 작은값 저장
    right = [] # 기준보다 큰 값 저장
    pivot = numbers[len(numbers)//2]  #기준값

    for i in range(len(numbers)):
        if i == (len(numbers)//2): #기준값이 비교되지 않도록 하기 위함.
            continue

        if pivot > numbers[i]:
            left.append(numbers[i])
        else:
            right.append(numbers[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = [3,2,4,6,9,1,8,7,5]
print(f'정렬 전 : ', numbers)
print('---'*10)
numbers = quick_sort(numbers)
print(f'정렬 후 : ', numbers)