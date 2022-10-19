import sys
sys.stdin = open('example_2.text')
input = sys.stdin.readline

LECTURE = int(input())

Lecture_arr = []
for i in range(LECTURE):
    Temp = list(map(int,input().split()))
    Lecture_arr.append(Temp)


Student = int(input())

Student_arr =[]
for i in range(Student):
    Temp = list(map(int,input().split()))
    Student_arr.append(Temp)


total = 0
for i in range(len(Student_arr)):
    for j in range(len(Lecture_arr)):
        count = 0
        for x in range(1,len(Lecture_arr[j])):
            if Lecture_arr[j][x] in Student_arr[i][1:]:
                count += 1

        if count == len(Lecture_arr[j])-1:
            total += 1

    print(total)
    total = 0
