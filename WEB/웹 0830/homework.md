
## 1. menus 리스트를 반복문으로 출력

{% for __(a)__ in menus%}
<p>{{menu}}<p>
{% endfor %}

a = menu

## 2. posts 리스트를 반복문을 활용하여 0번 글부터 출력

{% for post in posts%}
<p>{{__(b)__}}번 글 : {{post}}<p>
{% endfor %}

b = index(post)

## 3. user 리스트가 비어있다면 현재 가입한 유저가 없습니다. 텍스트를 출력하시오

{% for user in users%}
    <p>{{user}}<p>
{% __c__ %}
    <p>현재 가입한 유저가 없습니다.<p>
{% endfor %}

c = if not user

## 4. 첫 번쨰 반복문일떄와 아닐떄를 조건문으로 분기 처리하시오.

{% __a__ forloop,first %}
    <p>첫 번째 반복문입니다.</p>
{% __b__ %}
    <p>첫 번째 반복문이 아닙니다.</p>
{% __c__ %}
