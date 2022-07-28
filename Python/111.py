class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, species):
        self.name = name, species
        Doggy.num_of_dogs+=1
        Doggy.birth_of_dogs+=1

    def bark():
        print('멍멍!')

    def __del__(self):
        print(f'{self.name}이/가 하늘나라로 갔습니다.')
        Doggy.num_of_dogs-=1

    def get_status():
        print(f'현재 강아지 수 : {Doggy.num_of_dogs} 마리')
        print(f'태어난 강아지 수 : {Doggy.birth_of_dogs} 마리')

dog1=Doggy('붕붕','BULLDOG')
dog2=Doggy('똥글이','MINI BICHON')
dog3=Doggy('로켓', 'CHIWAWA')
dog4=Doggy('말복', 'JINDOGAE')

Doggy.get_status()
print(dog1.name)
print(dog2.name)
print(dog3.name)
print(dog4.name)
Doggy.bark()