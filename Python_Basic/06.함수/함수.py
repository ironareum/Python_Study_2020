#함수 정의부분
def plus(v1, v2) :
    result=0
    result=v1+v2
    return result

#변수 선언부분
hap=0

#메인 코드부분
hap=plus(100,200)
print("100과 200의 plus() 함수 결과는 %d" %hap)


#매개변수 디폴트 값 설정 ======================
def para_func(v1,v2,v3=0) :
    result=0
    result=v1+v2+v3
    return result

hap=para_func(10,20)
print(hap)

hap=para_func(10,20,30)
print(hap)


#가변매개변수 ===================
# 매개변수자리: *붙이기 (튜플형식으로 변환)
def para_func(*para):
    result=0
    print(para) #튜플 형식으로 변환??
    for num in para:
        result+=num
    return result

#변수 선언부분
hap=0

#메인 코드부분
hap=para_func(10,20)
print('매개변수 2개 함수 호출결과 ==> %d' %hap)

hap=para_func(10,20,30)
print('매개변수 3개 함수 호출결과 ==> %d' %hap)


#매개변수자리: ** (딕셔너리 형식).
#호출시에도 (매개변수.키=값) 으로 입력
def dic_func(**para):
    for k in para.keys():
        print('%s ---> %d 명 입니다.' %(k, para[k]))

dic_func(아이오아이=11, 소녀시대=8, 걸스데이=4)
