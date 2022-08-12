s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2]+ 'c'


print(s1==s2)
print(s1==s3)
print(s1==s4)
print(s1==s5)

print(s2==s3)
print(s2==s4)
print(s2==s5)
print(---*10)
print(s1 is s2)
print(s1 is s3)
print(s1 is s4)