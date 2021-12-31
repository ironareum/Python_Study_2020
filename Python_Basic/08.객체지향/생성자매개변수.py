#클래스 생성
class Car:
    name=""
    color=""
    speed=0
    def __init__(self, name, color, speed):
        self.name=name
        self.color=color
        self.speed=speed

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getSpeed(self):
        return self.speed

    def speed_up(self, speed):
        self.speed+=speed

    def speed_down(self, speed):
        self.speed-=speed

#인스턴스 생성
myCar1=Car("아우디","빨강", 20)

#클래스의 속성값을 직접 호출하지 않고 메소드를 통해 호출함.
print('%s 의 색상은 %s색 이며, 속도는 %d km 입니다.' %(myCar1.getName(), myCar1.getColor(), myCar1.getSpeed()))
