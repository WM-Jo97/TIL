from lotto import Lotto
import random
import json

number_lines = []
n=5
for i in range(5):
    number_lines.append(sorted(random.sample(range(1,46),6)))

print(number_lines)

draw_number=1023

with open(f'.\data\lotto_{draw_number}.json','r', encoding='utf-8') as lotto_json:
    lotto_json = json.load(lotto_json)
    Time=list(lotto_json.get('drwNoDate').split('-'))
    print(Time)