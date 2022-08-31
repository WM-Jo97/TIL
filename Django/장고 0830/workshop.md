## 1.intro/urls.py

path('pages/', views.pages)

## 2. pages/views.py

'''
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
'''

## 3.template/lotto.html

<body>
    <h1>제 000회 로또 번호 추천</h1>
    <p>조홍준님께서 선택하신 로또 번호는 {{A}} 입니다. </p>
</body>
