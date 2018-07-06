# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180705","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 파이썬 모듈
#
# - 함수나 변수 등을 정의해 놓은 파이썬 프로그램 파일
# - 모듈 내에서는 어떤 코드도 작성 가능하다 (변수, 함수, 클래스 등)
# - 다른 모듈에 의해 호출되고 사용된다
# - 모듈의 종류
#       > 표준 모듈
#       > 사용자 생성 모듈
#       > 서드 파티 모듈
# - 모듈을 불러올 땐, import {모듈명}
#

import _19_1_mymodule
print(_19_1_mymodule.addPi(100))      # 103.14159
print(_19_1_mymodule.subPi(100))      # 96.85841
print(_19_1_mymodule.mulPi(100))      # 314.159
print(_19_1_mymodule.divPi(100))      # 31.831015504887652

print("-------------------------------------------------")

# 네임 스페이스
#
# - 네임스페이스는 모듈 내부의 이름(변수, 함수, 클래스)를 구분하는 역할 수행
# - 네임스페이스가 주어지지 않은 변수나 함수는 legb 규칙에 따라 찾게 된다.
#

import math
import _19_1_mymodule

print(_19_1_mymodule.pi)          # _19_1_mymodule 내의 pi 이용        3.14
print(math.pi)              # math 모듈 내부의 pi 이용     3.141592653589793


# from ~ import
#
# from {모듈명} import {모듈객체}      # 모듈명 없이 객체명만으로 접근
#

from math import pi, sin, cos, tan
print(sin(pi/6), cos(pi/3), tan(pi/4))      # 0.49999999999999994 0.5000000000000001 0.9999999999999999

# - 현재 모듈에 특정 이름이 중복되는 경우 맨 마지막에 import된 객체가 적용
#

from math import pi, sin, cos, tan
from _19_1_mymodule import pi                   # pi의 이름이 중복되므로 맨 마지막에 import한 _19_1_mymodule pi사용
print(sin(pi/6), cos(pi/3), tan(pi/4))      # 0.4997701026431024 0.5004596890082058 0.9992039901050427

# - (*) 을 사용하면 모듈 내에 정의된 모든 이름을 현재 모듈로 가져온다
#

from math import *                        # math 모듈 내 모든 이름 가져오기
print(sin(pi/6), cos(pi/3), tan(pi/4))      # 0.49999999999999994 0.5000000000000001 0.9999999999999999

# - 모듈의 이름을 다른 이름으로 바꾸는 것도 가능
#

import _19_1_mymodule as M        # _19_1_mymodule 의 이름을 M 으로 변경
print(M.pi)                  # 3.14

# - 모듈 내에 정의된 객체의 이름을 변경하는 것도 가능
#

from math import sin as S, cos as C, tan as T
import _19_1_mymodule as M
print(S(M.pi/6), C(M.pi/3), T(M.pi/4))      # 0.4997701026431024 0.5004596890082058 0.9992039901050427
                                            # S=sin, C=cos, T=tan  // M = mymoudle

print("-------------------------------------------------")

# 모듈 지원 함수 목록 보기
#
# - dir함수 : 인자에 객체를 넣어주면, 해당 객체가 어떤 변수와 메서드를 갖고있는지 반환해 준다.
#

import _19_1_mymodule
print(dir(_19_1_mymodule))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'addPi', 'divPi', 'mulPi', 'pi', 'subPi']
a = [1,"Python",3.14159]
print(dir(a))
#['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print("-------------------------------------------------")

# 연습해보기
#

import _19_4_fibo as fibo

print(fibo.fib(20))             # 1 1 2 3 5 8 13 (끝)
                                # None                  (★질문★) 왜 None이 나올까?
fib = fibo.fib
print(fib(20))                  # 1 1 2 3 5 8 13 (끝)
                                # None


print(type(fib))                # <class 'function'>

from _19_4_fibo import fib, fib2
print(fib(100))                 # 1 1 2 3 5 8 13 21 34 55 89 (끝)
                                # None

from _19_4_fibo import fib as F, fib2 as F2
print(F2(200))                  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

print("-------------------------------------------------")


# ★(헷갈림)★
# __name__ 과 "__main__"
#
# - 모든 모듈은 모듈의 이름을 저장하고 있는 내장 변수 __name__ 을 갖고 있다.
# - 최상위 모듈(인터프리터에서 실행되는 모듈)의 __name__은 "__main__"이다
# - 그 외 import되는 모듈의 이름은 파일명이다

        # _19_2_module_1 파일에 print("_19_2_module_1 모듈 이름" + __name__)
        # _19_2_module_2 파일에 import _19_2_module_1
        #                 print("_19_2_module_2 모듈 이름" + __name__)
        #
        # shell command 에서 python _19_2_module_1.py 입력
        # (출력 결과)
        # _19_2_module_1 의 모듈이름 : __main__
        #
        # shell command 에서 python _19_2_module_2.py 입력!!
        # (출력 결과)
        # _19_2_module_1 의 모듈이름 : _19_2_module_1
        # _19_2_module_2 의 모듈이름 : __main__

# - 내장 변수 __name__과 최상위 실행 모듈의 이름이 "__main__" 인 점을 응용하면
#   import 되는 모듈로 사용하면서
#   자신이 최상위 모듈로 실행될 떄만 특정 기능을 수행하는 코드를 만들 수 있다.
#   ★(헷갈림)★

        # mymod.py 파일을 만들어서
        # def main():
        #       print("mymod.py를 최상위 모듈로 실행했습니다")
        #
        # if __name__ == "__main__":
        #       main()
        # else:
        #       print("mymod.py의 모듈이름 : " + __name__")
        #
        # 이런식으로 내용을 입력한다면,
        # mymod.py가 최상위 모듈로 실행한다면 main()함수가 호출되고
        # 그렇지 않다면 모듈이름을 출력할 수 있다.


print("-------------------------------------------------")

# import한 모듈 이름 열거
#
# - 한번이라도 import한 모듈은 dict 타입인 sys.modules 변수에 저장된다
#
import sys
for i in sys.modules.keys():
    print(i)

                                # sys
                                # builtins
                                # _frozen_importlib
                                # _imp
                                # _thread
                                # _warnings
                                #   ....
                                #   ....
                                # _multibytecodec
                                # encodings.cp437
                                # _19_1_mymodule
                                # math
                                # _19_4_fibo


# 모듈의 공유 : 모듈은 한 번 가져오기만 하면 메모리에 적재되고 공유된다!!
#


print("-------------------------------------------------")

# 이름(변수, 함수, 클래스) 이 속한 모듈 알아내기
#
# - 파이썬 변수, 함수, 클래스는 각각 자신이 정의된 모듈의 이름이 저장된
#   __module__속성을 가지고 있다.
#

from math import sin
from cmd import Cmd

print(sin.__module__)               # math
print(Cmd.__module__)               # cmd

print("-------------------------------------------------")

# 여러가지 내장 모듈
#

    # 1. sys 모듈 & argv
    #   - sys : 파이썬 인터프리터와 관련된 정보와 기능 제공
    #   - argv : 명령행에서 넘어온 인수(arguments)를 처리할 수 있다.
    #

# _19_3_args.py 파일에서
# import sys
# args = sys.argv[1:]       # argv[0] 은 스크립트명 자체!
#
# for x in args:
#       print(x, end = " ")
# else:
#       print()
#
# 입력 후에 command shell에서
# python _19_3_args.py 1 2 3 4 5 6 7 8 9 10 입력
#
# (출력)
# 1 2 3 4 5 6 7 8 9 10
#
print("-------------------------------------------------")
    # 2. math 모듈
    #
print(math.pi)              # 파이값           3.141592653589793
print(math.e)               # 자연상수         2.718281828459045

print(abs(10))              # 절대값           10
print(abs(-10))             # 절대값           10

print(round(1.2345,2))      # 소수점 둘째 자리까지 출력 (셋째자리에서 반올림)   1.23
print(round(-1.5555555,3))  # 소수점 셋째 자리까지 출력 (넷째자리에서 반올림)   -1.556
print(round(-1.1))          # 소수점 반올림       -1

print(math.trunc(1.7))      # 소수점 이하 버림      1
print(math.trunc(-1.7))     # 소수점 이하 버림     -1

print(math.factorial(10))   # 팩토리얼 계산       3628800

print(math.pow(2,10))       # 1024.0

print(math.sqrt(225))      # 제곱근 계산         15


    # 로그함수
    # - 첫 번째 매개변수의 로그를 반환, 두 번재 매개변수는 밑수
    #       > 두 번째 매개변수가 생략되면 밑수는 자연지수 e로 간주
    #       > 밑수가 10인 로그를 위한 log10 함수도 별도로 제공
print(math.log(2))          # log(e)2       0.6931471805599453
print(math.log(2,4))        # log(4)2       0.5
print(math.log10(1000))     # log(10)1000   3.0

print("-------------------------------------------------")

    # 3. re 모듈 - 정규식(Regular Expression)
    #
    # - string보다 더 전문적으로 문자열을 다룰 수 있는 모듈
    # - 문자열 내에서 패턴에 매칭되는 문자열을 추출
    #

import re

list = """
Primary Email : joohongkeem@naver.com
Secondary Email : jorange5@naver.com
"""
result_list = re.findall(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)",list)
print(result_list)          # [('joohongkeem', 'naver', 'com'), ('jorange5', 'naver', 'com')]
for result in result_list:
    print(result)       # ('joohongkeem', 'naver', 'com')
                        # ('jorange5', 'naver', 'com')


print("-------------------------------------------------")

    # 4. random 모듈 - 난수
    #
    # - 임의로 특정 값을 선택해 제공하는 기능 - 주사위의 예
    # - random 모듈은 단순히 난수를 발생하는 것 이외에 다양한 기능을 제공
    #       > random() : 0 이상 1 미만의 '★실수★' 난수를 발생
    #       > randint(start,end) : start ~ end 사이의 정수 난수를 발생
    #       > randrange([start,] stop [,step]) : start, stop 사이의 step 간격 수 중 난수를 발생
    #       > shuffle(seqvar) : 시퀀스 자료형을 섞음
    #       > choice(seqvar) : 시퀀스 자료형에서 아무거나 하나를 뽑아줌
    #       > sample(seqvar, size) : 시퀀스 자료형에서 size만큼의 값을 임의로 뽑아옴

import random

print(random.random())      # 0 이상 1 미만의 '실수' 난수를 발생
print(random.randint(1,6))  # 1 ~ 6 사이의 '정수' 난수를 발생
print(random.randrange(1,100,3))    # 1 ~ 100 사이 3간격의 수 중에서 난수를 발생

seq = ["짬뽕", "짜장면", "짬짜면", "볶음밥", "제육덮밥"]
print(seq)                      # ['짬뽕', '짜장면', '짬짜면', '볶음밥', '제육덮밥']

random.shuffle(seq)             # 시퀀스 자료형 섞기
print(seq)                      # ['짜장면', '짬뽕', '짬짜면', '볶음밥', '제육덮밥']

print(random.choice(seq))       # 시퀀스 자료형 중 임의로 한 개의 값 반환
                                # 짬짜면

print(random.sample(seq, 3))    # 시퀀스 자료형 중, 3개를 임의로 뽑아옴
                                # ['짬뽕', '짜장면', '짬짜면']

print("-------------------------------------------------")

