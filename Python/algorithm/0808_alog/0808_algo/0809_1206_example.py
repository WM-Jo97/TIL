import sys

sys.stdin = open("input_1206.text")


for t in range(1,11):

    cnt = int(input())
    building_list= list(map(int,input().split()))
    result = 0 #최종 결과


    for i in range(cnt):
        cur_building = building_list[i]

        if not cur_building: #빌딩이 없는 경우 좌우 확인  x
            continue

        else:

            # 좌, 우 4개의 빌딩 중 가장 높은 빌딜을 찾는 부분
            max_height=0
            idx = [-2,-1,1,2] # 좌우 2칸 idx
            for side in range(4):
                if building_list[i+idx[side]] > max_height:
                    max_height = building_list[i + idx[side]]

            if cur_building > max_height:
                result+=cur_building-max_height

    print(f'#{t} {result}')