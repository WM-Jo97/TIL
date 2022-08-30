import random
from django.shortcuts import render


def pages(request):
    A=[]
    while True:
        B=random.randrange(1,46)
        if not B in A:
            A.append(B)
        if len(A) == 6:
            break
    context ={
        'A' : A,
    }

    return render(request,'lotto.html',context)
# Create your views here.
