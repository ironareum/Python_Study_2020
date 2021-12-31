#함수 사용??????=============
# def speed(car_name, speed):
#     print('%s 의 현재속도는 %d 입니다.' %(car_name, speed))
#
# speed("아우디", 0)
# speed("벤츠", 30)

#객체지향?? =============
audi = {
    "name": "아우디",
    "speed": 0
}
def info(car):
    print('%s 의 현재속도는 %d 입니다.' %(car["name"], car["speed"]))
# def info(car):
#     print('%s 의 현재속도는 %d 입니다.' %(car["name"], car["speed"]))

info(audi)
