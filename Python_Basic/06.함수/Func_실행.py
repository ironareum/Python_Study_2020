
#사용자 정의한 모듈 호출하기

#방법1)
# import Func
#
# Func.func1()
# Func.func2()
# Func.func3()

#방법2)
from Func import func1, func2, func3
func1()
func2()
func3()

#파이썬에서 제공하는 표준 모듈의 목록
import sys
# print(sys.builtin_module_names)

import random
print(dir(random))
