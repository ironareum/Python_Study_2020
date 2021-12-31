#슈퍼클래스 (=부모클래스)
class Car:
    color=""
    speed=0
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed
    def speed_up(self,speed):
        self.speed+=speed
    def speed_down(self,speed):
        self.speed-=speed
#하위클래스(=서브클래스)

class Sedan(Car):
    seatNum =5
    def getSeatNum(self):
        return self.seatNum

car=Car("red", 0)
sedan = Sedan("black", 0)
print('자동차의 색상은 %s, 속도는 %d km입니다.' %(car.color, car.speed))
print('세단의 색상은 %s, 속도는 %d km이고, 좌석수는 %d 입니다.' %(sedan.color, sedan.speed, sedan.seatNum))
