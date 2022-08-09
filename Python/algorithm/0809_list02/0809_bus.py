import sys

sys.stdin = open('bus.text')

T = int(input())
for t in range(1,T+1):
    (K, N, M) = list(map(int,input().split()))  #K N M
    charger = list(map(int,input().split()))    # CHARGER 충전소 위치
    charger.append(N)                           # 마지막 충전소~ 목적지까지의 거리를 확인하기 위해
    charger.insert(0,0)                         # 출발점 ~ 첫번째 충전소 거리를 확인하기 위해


    turm_list=[]                                # 거리들의 리스트
    for i in range(0,len(charger)-1):
        turm = charger[i+1]-charger[i]
        turm_list.append(turm)

    turm_max = 0                                # 하나만 거리가 이동 가능거리를 초과해도 값은 0이므로 max 초기화
    for i in turm_list:
        if i>turm_max:
            turm_max=0
            turm_max+=i

    if turm_max> K:                             # 가장 긴 길이가 이동 가능 거리보다 크면 0 출력
        print(f'#{t} 0')


    else:
        move=charger[len(charger)-1]-K          # move = 가장 마지막 목적지에서 최대 가능거리만큼 떨어진 값
        count=0                                 # 충전 횟수
        while move>0:                           # 점점 뒤로 갈 것이기 때문에 0보다 작은 값
            if move in charger:                 # 만약 목적지에서 주행 가능 거리만큼 움직인 곳에 충전소가 있으면
                count+=1                        # count +1, 버스의 위치인 move 는 -K 만큼 이동
                move = move-K
            else:
                for i in range(1,K+1):            # 1~이동 가능거리, (이동 가능거리 이상의 값은 위에서 걸러짐)
                    if move+i in charger:         # 버스의 위치를 뒤로 돌리면서 이동하기 때문에 i는 + 방향으로 움직여야 목적지와 가까운 쪽
                        count+=1
                        move=move+i-K
                        break                     # break가 없었을때는 6개만 맞았어요.. break 잊지 마세요..

        print(f'#{t} {count}')

