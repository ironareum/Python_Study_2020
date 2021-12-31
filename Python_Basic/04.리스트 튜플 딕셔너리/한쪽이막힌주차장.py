sel=0
car="A"
parkingLot =[]
top =0
while (sel !=3):
    sel = int(input('<1>자동차 넣기, <2> 자동차 빼기, <3>끝 : '))

    # if(len(parkingLot)==0):
    #     parkingLot.append(chr(car))

    if sel ==1 :
        if(top>=5):
            print('주차장이 꽉 차서 못들어감')
        else:
            parkingLot.append(car)
            print('%s 자동차 들어감. 주차장 상태 ==> %s' %(car, parkingLot))
            car = chr(ord(car)+1)
            top+=1
    elif sel ==2:
        if top > 0:
            # val=parkingLot[int_-1]
            # del(parkingLot[int_-1]) #리스트 내 선택항목 삭제
            outCar=parkingLot.pop() #리스트 젤 마지막 항목 빼내고, 빼낸항목 삭제
            print('%s 자동차 나감. 주차장 상태 ==> %s' %(outCar, parkingLot))
            car = chr(ord(car)-1)
            top-=1
        else:
            print('빠져나갈 자동차가 없음')
            continue
    else :
        print('현재 주차장에 %d 대가 있음' %(len(parkingLot)))
        print('프로그램을 종료합니다.')
