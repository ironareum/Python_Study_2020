menu ={'짜장면':'단무지',
        '삼겹살':'김치',
        '피자':'콜라',
        '라면':'김치',
        '치킨':'치킨무'
        }

sel = input('%s중 좋아하는 것은?' %(menu.keys()))
if sel in menu :
    print('<%s> 궁합 음식은 <%s> 입니다.' %(sel, menu[sel])) #menu.get(sel) 과 동일
elif sel =="끝":
    break
else :
    print('그런 음식이 없네요. 확인해 보세요.')
