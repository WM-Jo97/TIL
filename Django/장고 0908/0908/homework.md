1. 로그인 된 사용자인지 만을 확인하기 위한 속성 : is_authenticated

2. a = AuthenticationForm
   b = login
   c = form.get_user()

3. anoymous

4. PBKDF2, bcrypt, scrypt 알고리즘 , sha256,sha1,md5 해쉬

5. logout 이라는 함수 이름이 두번 중복해서 쓰임
   import 에서 logout 을 as auth_logout 으로 바꾸고

   def logout(request):
        auth_logout(request)
        return~ ~ 으로 수정