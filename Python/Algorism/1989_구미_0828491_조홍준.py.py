T = int(input())
 
data=[input() for i in range(T)]
 
for t in range(T):    
    a=data[t].strip()
    test=t+1
    if a==a[::-1]:
        print('#%d'%test,"1")
        continue
    else:
        print('#%d'%test,"0")