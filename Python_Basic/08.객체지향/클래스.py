'''
class 클래스 이름:
    #이 부분에 관련 코드 구현

예)
class 자동차:
    #자동차의 속성(=필드)
    자동차 색상=""
    자동차 속도=0

    #자동차의 기능
    속도 올리기(증가할_속도량):
        #현재 속도에서 증가할 속도량만큼 속도를 올리는 코드
    속도 내리기()
'''
# 1.클래스 생성 (=자동차 설계도)
class Car:
    color=""
    speed=0
    def speed_up(self, speed):
        self.speed+=speed
    def speed_down(self, speed):
        self.speed-=speed

# 2.인스턴스 생성(=찍어내는 자동차)
myCar1 = Car()
myCar2 = Car()
myCar3 = Car()

# 3.필드에 값 대입하기 : 각가의 자동차는 각기 다른 속성값을 가짐
myCar1.color="빨강"
myCar2.color="파랑"
myCar3.color="노랑"

myCar1.speed=0
myCar2.speed=0
myCar3.speed=0

myCar1.speed_up(30)
myCar2.speed_up(60)

print('자동차1의 색상은 %s이며, 현재속도는 %d km 입니다.' %(myCar1.color, myCar1.speed))

print('자동차2의 색상은 %s이며, 현재속도는 %d km 입니다.' %(myCar2.color, myCar2.speed))
