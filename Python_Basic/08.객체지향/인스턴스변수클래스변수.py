#클래스 변수: 클래스.클래스변수명
#인스턴스 변수: 인스턴스.클래스변수명
class Car:
    color="" #인스턴스 변수
    speed=0 #인스턴스 변수
    count=0 #클래스 변수
    def __init__(self):
        self.speed=0
        Car.count+=1

#변수선언
myCar1, myCar2 =None, None

#메인코드부분
myCar1=Car()
myCar2=Car()
myCar1.speed=30
print('자동차1의 현재속도는 %d km, 생산된 자동차 숫자는 총 %d대 입니다.' %(myCar1.speed, myCar1.count))
