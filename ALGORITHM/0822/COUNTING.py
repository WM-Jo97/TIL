A=[0,4,1,3,1,2,4,1]

count= [0 for _ in range(max(A)+1)]


for i in A:
    count[i] = count[i]+1


Sorted_list=[0 for _ in range(len(A))]

for i in range(1,len(count)):
    count[i]=count[i]+count[i-1]

for i in range(len(A)-1,-1,-1):
    Sorted_list[count[A[i]]-1] = A[i]
    count[A[i]] -=1

print(Sorted_list)
