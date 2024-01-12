# 동물
# 이름, 나이, 성별, 음식 개수, 체력 개수
# 먹기, 산책하기

class Aniaml:

    # init에다가 생성
    def __init__(self, name, age, gender, feed_count=1, life=1):
        # 해당하는 주소에 name을 받아와서 네임 만들기
        self.name = name
        self.age = age
        self.gender = gender
        self.feed_count = feed_count
        self.life = life

    # sefl 사용 시 주소값 자동으로 들어감
    # 음식 1개 소모, 체력 1개 획득
    def eat(self):
        # self 주소에 있는 feed_count는 차감하고
        self.feed_count -= 1
        # self 주소에 있는 life는 증가 한다
        self.life +=1

    # 체력 1개 소모, 음식 1개 획득
    def walk(self):
        # self 주소에 있는 life는 차감하고
        self.life -= 1
        # self 주소에 있는 feed_coun는 증가한다
        self.feed_count += 1

tiger = Aniaml(name='호랑이', age=10, gender='수컷')
lion = Aniaml(name='사자', age=20, gender='암컷')

tiger.eat()
lion.walk()

print(tiger.name, tiger.age, tiger.gender, tiger.feed_count, tiger.life)
print(lion.name, lion.age, lion.gender, lion.feed_count, lion.life)