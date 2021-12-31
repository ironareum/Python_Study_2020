#슈퍼클래스 (=부모클래스)
class Car:
    color=""
    speed=0
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed
    def speed_up(self,speed):
        self.speed+=speed
        print('현재속도(슈퍼클래스)): ', self.speed)
    def speed_down(self,speed):
        self.speed-=speed
#하위클래스(=서브클래스)

class Sedan(Car):
    seatNum =5
    def getSeatNum(self):
        return self.seatNum
    #속도제한 주기
    def speed_up(self,speed):
        if self.speed ==100:
            print('현재 최고속도로 달리고 있습니다. 속도를 줄여주세요.')
            speed=0

        self.speed+=speed

        if self.speed>=100:
            self.speed=100
            print('현재 속력은 %d km 입니다.제한속도는 100km입니다.' %(self.speed) )

car=Car("red", 0)
print('자동차의 색상은 %s, 속도는 %d km입니다.' %(car.color, car.speed))
car.speed_up(80)
car.speed_up(20)
car.speed_up(20)


sedan = Sedan("black", 80)
print('세단의 색상은 %s, 속도는 %d km이고, 좌석수는 %d 입니다.' %(sedan.color, sedan.speed, sedan.seatNum))
sedan.speed_up(20)
sedan.speed_up(20)
