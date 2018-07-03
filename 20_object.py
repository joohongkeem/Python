# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180703","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 객체
#
# 1. 이름과 객체
#
# - 파이썬에서 모든 자료(데이터)들은 객체의 형태로 저장된다.
# - 파이썬의 변수는 컴파일러 언어처럼 변수에 할당된 값을 저장하는
#   저장공간(메모리)의 주소 심볼릭이 아니다.
# - 변수는 단지 객체의 이름(심볼)일 뿐이다.
# - 파이썬의 객체 이름(변수)과 객체의 ID(주소)는 심볼 테이블에 함께 저장되어
#   관계를 갖게 된다.
#
#       a=1 -> 객체 1을 만들고 그 이름이 a
#
 
print("-------------------------------------------------")

# 2. 심볼테이블
#
# - 변수의 이름과 저장된 데이터의 주소를 저장하는 테이블
# - 심볼테이블의 내용을 살펴보기 위해, globals(), locals() 내장 함수를 이용
# - 두 함수는 해당 스코프 내 심볼테이블의 내용을 dict 타입의 객체로 반환
#


glob_a = 1
glob_b = "Symbol"   # 글로벌 변수 선언

def f():            # 로컬 변수 확인을 위한 함수 선언
    local_a = 2
    local_b = "Table"
    print(locals()) # 로컬 심볼테이블 확인

f()                 # {'local_a': 2, 'local_b': 'Table'}

print(globals())    # 글로벌 심볼테이블 확인
                    # {'__name__': '__main__', '__doc__': None,
                    # '__package__': None, '__loader__': <class '
                    # _frozen_importlib.BuiltinImporter'>, '__spe
                    # c__': None, '__annotations__': {}, '__built
                    # ins__': <module 'builtins' (built-in)>, '__
                    # file__': 'C:\\Users\\bit-user\\Desktop\\주홍
                    # \\짬프뚜빠이썬\\10_object.py', 'glob_a': 1,
                    # 'glob_b': 'Symbol', 'f': <function f at 0x000
                    # 00146DD66C1E0>}
                    
print("-------------------------------------------------")
                    

# 3. 레퍼런스 카운트와 쓰레기 수집
#
# - 레퍼런스 카운트(Reference Count) : 객체를 참조하는 참조 수
# - 레퍼런스 카운트가 0이 되면 사용하지 않는 객체로 판단, 자동으로 사라짐
# - 이러한 자업을 '쓰레기 수집(Garbage Collection)'이라 함
#

# sys.getrefcount(x) : 입력한 자료형에 대한 참조 개수

import sys
print(sys.getrefcount(3))   # 144
                            # 파이썬 내부적으로 3이라는 자료형 사용하기때문
a = 3
print(sys.getrefcount(3))   # 145
b = 3
print(sys.getrefcount(3))   # 146   >> 변수를 늘리면 참조개수가 증가
                            # 즉, 3이라는 객체 하나를 146개가 참조하는 것!
                            # a,b는 모두 같은 3을 가리킨다.
                            
print(sys.getrefcount(object()))    # 1
x = object()
print(sys.getrefcount(x))           # 2

