def atoi(s) :
    i=0
    for x in s :
        i=i*10 + ord(x)-ord('0')
        return i

print(itoa('123'))

print(ord('1'))
print(ord('0'))

def itoa(num):
    neg=False
    if neg:
    if num<0:

    result=''
    while num:
        num, remain = num//10, num % 10
        result = chr(ord('0')+remain)+result
    return result




