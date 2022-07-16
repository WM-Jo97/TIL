def roc(x,y):
    if y%3+1==x:
        print("A")
    else:
        print("B")
 
a,b = map(int, input().split())        
roc(a,b)