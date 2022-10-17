import sys
sys.stdin=open('example_10800.text')

import sys
N = int(input(''))
ball_list = []
for i in range(N):
    C, S = map(int, sys.stdin.readline().rstrip().split(' '))
    ball_list.append([i, S, C])

# size, color로 오름차순 정렬
ball_list.sort(key=lambda x:(x[1], x[2]))

color_list = [0] * 200001
player_list = [0] * N

sum = 0
i, j = 0, 0

#print(ball_list)
# 누적 합
while i < N:

    a_ball = ball_list[i]
    b_ball = ball_list[j]

    # B >= A 일 때 종료
    while b_ball[1] < a_ball[1]:

        # 총 사이즈 누적
        sum += b_ball[1]
        # 컬러 별 사이즈 누적
        color_list[b_ball[2]] += b_ball[1]

        j += 1
        b_ball = ball_list[j]

    player_list[a_ball[0]] = sum - color_list[a_ball[2]]
    i += 1

#print(player_list)
for i in range(N):
    print(player_list[i])