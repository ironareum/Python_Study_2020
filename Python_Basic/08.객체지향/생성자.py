#생성자는 인스턴스를 생성하면 무조건 호출되는 메소드

#생성자: __init__()
'''
class 클래스 이름:
    def __init__():
        #이부분에 초기화할 코드를 입력
'''

class Car:
    color=""
    speed=0
    def __init__(self):
        self.color="빨강"
        self.speed=0

    def speed_up(self, speed):
        self.speed+=speed
    def speed_down(self, speed):
        self.speed-=speed  
myCar1 = Car()
print('자동차1의 색상은 %s색 이며, 속도는 %d km 입니다.' %(myCar1.color, myCar1.speed))
