import random
import json
from re import A

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        global number_lines
        number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for i in range(n):
            number_lines.append(sorted(random.sample(range(1,46),6)))
        

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        with open(f'.\data\lotto_{draw_number}.json','r', encoding='utf-8') as lotto_json:
            global lotto_1
            lotto_1 = json.load(lotto_json)
            alph=['A','B','C','D','E']
            print('==========================================')
            print(f'           제 {draw_number}회 로또          ')
            print('==========================================')
            print(f'추첨일 : {get_draw_date(draw_number)} (토)         ')
            for i in range(n):
                print(f'{alph[i]} : {number_lines[i]}')
            

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        main_numbers=[]
        bonus_number=lotto_1.get('bnusNo')
        for i in range(1,7):    
            main_numbers.append(lotto_1.get(f'drwNo{i}'))
        print('==========================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print('==========================================')
        alph=['A','B','C','D','E']
        for i in range(n):
            print(f'{alph[i]} : {same_main_counts}개 일치 ({ranking}')

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
            with open(f'.\data\lotto_{draw_number}.json','r', encoding='utf-8') as lotto_json:
                lotto_1 = json.load(lotto_json)
                lotto_1.get('drwNoDate')
                Time=list(lotto_1.get('drwNoDate').split('-'))
                year = Time[0]
                month = Time[1]
                day = Time[2] 
                return f'{year}/{month}/{day}'
        # return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        return (main_numbers, bonus_number)
        # return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts=0
        is_bonus=''
        for i in main_numbers:
            if main_numbers[i]in number_lines:
                same_main_counts+1
            elif bonus_number in number_lines:
                is_bonus=' + 보너스'
            else:
                pass
        return same_main_counts, is_bonus
        # return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        ranking=''
        if same_main_counts == 6:
            ranking='1등 당첨!'
        elif same_main_counts == 5 and is_bonus==' + 보너스':
            ranking='2등 당첨!'
        elif same_main_counts == 5:
            ranking='3등 당첨!'
        elif same_main_counts == 4 or (same_main_counts==3 and is_bonus==' + 보너스'):
            ranking='4등 당첨!'
        elif same_main_counts == 3 or (same_main_counts==2 and is_bonus==' + 보너스'):
            ranking='5등 당첨!'
        else:
            ranking='낙첨'
        
        return ranking
