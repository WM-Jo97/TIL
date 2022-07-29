import random
import json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        self.n=n
        for i in range(self.n):
            self.number_lines.append(sorted(random.sample(range(1,46),6)))
        

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        self.draw_number=draw_number
        with open(f'.\data\lotto_{draw_number}.json','r', encoding='utf-8') as lotto_json:
            self.lotto_1 = json.load(lotto_json)
            self.alph=['A','B','C','D','E']
            year,month,day = Lotto.get_draw_date(self.draw_number)
            print('==========================================')
            print(f'           제 {self.draw_number}회 로또          ')
            print('==========================================')
            print(f'추첨일 : {year}/{month}/{day} (토)         ')
            for i in range(self.n):
                print(f'{self.alph[i]} : {self.number_lines[i]}')
            

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        main_numbers, bonus_number = Lotto.get_lotto_numbers(draw_number)


        print('==========================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print('==========================================')
        self.get_lotto_numbers(draw_number)
        for i in range(self.n):
            alph=['A','B','C','D','E']
            line=self.number_lines[i]
            same_main_counts,is_bonus = Lotto.get_same_info(main_numbers, bonus_number, line)
            if Lotto.get_ranking(same_main_counts,is_bonus) == -1:
                ranking = '낙첨'
            else:
                ranking = f'{Lotto.get_ranking(same_main_counts,is_bonus)}등 당첨!'
            if is_bonus==True:
                bonus= '+ 보너스 일치'
            else:
                bonus= ''
            print(f'{alph[i]} : {same_main_counts}개 일치 {bonus} ({ranking})')

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
            with open(f'.\data\lotto_{draw_number}.json','r', encoding='utf-8') as lotto_json:
                lotto_2 = json.load(lotto_json)
                lotto_2.get('drwNoDate')
                Time=list(lotto_2.get('drwNoDate').split('-'))
                year = Time[0]
                month = Time[1]
                day = Time[2] 
                return year,month,day
        # return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        main_numbers=[]
        with open(f'.\data\lotto_{draw_number}.json','r', encoding='utf-8') as lotto_json:
                lotto_4 = json.load(lotto_json)
        bonus_number=lotto_4.get('bnusNo')
        for i in range(1,7):    
            main_numbers.append(lotto_4.get(f'drwtNo{i}'))
            main_numbers.sort()
        return (main_numbers, bonus_number)
        # return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts=0
        is_bonus=False
        for i in line:
            if i in main_numbers:
                same_main_counts+=1
            elif i == bonus_number:
                is_bonus=True
            else:
                pass
        return same_main_counts,is_bonus
        # return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        ranking=0
        if same_main_counts == 6:
            ranking=1
        elif same_main_counts == 5 and is_bonus==True:
            ranking=2
        elif same_main_counts == 5:
            ranking=3
        elif same_main_counts == 4:
            ranking=4
        elif same_main_counts == 3:
            ranking=5
        else:
            ranking=-1
        
        return ranking
