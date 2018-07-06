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
                                    # sys.getrefcount함수를 호출하며 내부적으로 2번 사용
                                    
print(sys.getrefcount(x))           
y = x
print(sys.getrefcount(x))           # 3
del(x)
print(sys.getrefcount(y))           # 2 -> x가 del함수로 인해 없어졌으니 감소함
print(sys.getrefcount(object()))    # 1



# 조금 더 해보자
print(sys.getrefcount(101010))      # 2
                                    # sys.getrefcount함수 호출하며 내부적으로 2번 참조
x = 101010
print(sys.getrefcount(101010))      # 3
print(sys.getrefcount(x))           # 3
print(x is 101010)                  # True

y = 101010
print(sys.getrefcount(101010))      # 4
print(sys.getrefcount(y))           # 4
print(sys.getrefcount(x))           # 4
print(y is x)                       # Ture

z = x
print(sys.getrefcount(101010))      # 5
print(sys.getrefcount(x))           # 5
print(sys.getrefcount(y))           # 5
print(sys.getrefcount(z))           # 5

del(x)                              # del(variable) : 변수 variable을 삭제한다 
print(sys.getrefcount(101010))      # 4
print(sys.getrefcount(y))           # 4
print(sys.getrefcount(z))           # 4
print(y is 101010)                  # True
print(z is 101010)                  # True

print("-------------------------------------------------")

# 4. 객체ID
#
# - id() 함수를 이용하면 객체의 주소를 식별할 수 있다.
#       >> 만약 두 객체의 ID가 동일하면, 같은 객체를 참조하고 있는 것
#   ★★★★★
# - immutable 자료형 (int, float, complex, bool, bytes, str, tuple) 는 같은걸 가리킨다.
#   mutable 자료형 (list, set, dict) 는 그 때 그 때 객체를 생성하기에 다른걸 가리킨다.

var1 = 10
var2 = 10
print(hex(id(var1)),hex(id(var2)))      # 0x7fffdf09d540 0x7fffdf09d540     (같다!!)
print(var1 is var2)                     # True

List1=[1,2,3]
List2=[1,2,3]
print(hex(id(List1)),hex(id(List2)))    # 0x20cbf535e88 0x20cbf535c88       (다르다!!)
print(List1 is List2)                   # False
                                        # -> List는 각각 list 객체를 만든다.
List1[1] = 99
print(List1,List2)                      # [1, 99, 3] [1, 2, 3]
                                        # -> List1의 값만 바뀌었다.

str1 = "Hello"
str2 = "Hello"
print(hex(id(str1)),hex(id(str2)))      # 0x2933eda58f0 0x2933eda58f0       (같다!!)
print(str1 is str2)                     # True


print("-------------------------------------------------")

# 5. 객체의 복사
#
# - 위의 예제에서 list는 같은 객체를 참조하지 않고, 각각 객체를 만들었다.
#       -> 어떻게 하면 동일한 객체를 참조하도록 할 수 있을까?
#

    # 5-1. 레퍼런스 복사 (★★★객체 복사 O★★★)
    #
    #   - 객체를 참조하는 주소만 복사하는 것   
    #

List1 = [1,2,3]
List2 = List1                           # 객체 참조 주소만 복사된다
print(hex(id(List1)),hex(id(List2)))    # 0x28526b209c8 0x28526b209c8       (같다!!)
List1[1] = 99
print(List1,List2)                      # [1, 99, 3] [1, 99, 3]
                                        # -> 둘다 값이 바뀌었다.
                                        #    (Why?) 완전히 같은 객체 참조

    # 5-2. [:]를 이용한 복사  (객체 복사 X)
    #
    #   - 객체 전체를 가리키는 [:]를 이용하여 복사한다   
    #

List1 = [1,2,3]
List2 = List1[:]
print(hex(id(List1)),hex(id(List2)))    # 0x23a83c65908 0x23a83ee0908       (다르다!!)
List1[1] = 99
print(List1,List2)                      # [1, 99, 3] [1, 2, 3]
                                        # -> List1의 값만 바뀌었다.

    # 5-3. copy함수 이용  (얕은 복사)
    #
    #   - copy 모듈의 copy 함수를 사용하여 복사한다.
    #   - 리스트만 복사되고, 그 내부 리스트까지 별도의 객체로 복사가 되진 않는다.

import copy
List1 = [1,[1,2,3]]
List2 = copy.copy(List1)
print(List1, List2)                     # [1, [1, 2, 3]] [1, [1, 2, 3]]
List1[0] = 100
print(List1, List2)                     # [100, [1, 2, 3]] [1, [1, 2, 3]]
List1[1].append(4)
print(List1, List2)                     # [100, [1, 2, 3, 4]] [1, [1, 2, 3, 4]]
    

                                    

    # 5-4. deepcopy함수 이용  (깊은 복사)
    #
    #   - copy 모듈의 deepcopy 함수를 사용하여 복사한다.
    #   - 복합 객체를 재귀적으로 생성하고 복사한다.
    #

List1=[1,2,3]
List2=copy.deepcopy(List1)
print(hex(id(List1)),hex(id(List2)))    # 0x16270ca5ec8 0x16270ca7208       (다르다!!)
List1[1] = 99
print(List1,List2)                      # [1, 99, 3] [1, 2, 3]
                                        # -> List1의 값만 바뀌었다.

    #
    #   - deepcopy는 복합객체를 재귀적으로 생성하고 복사한다.
    #

import copy
List1 = [1,[1,2,3]]
List2 = copy.deepcopy(List1)
print(List1, List2)                     # [1, [1, 2, 3]] [1, [1, 2, 3]]
List1[0] = 100
print(List1, List2)                     # [100, [1, 2, 3]] [1, [1, 2, 3]]
List1[1].append(4)
print(List1, List2)                     # [100, [1, 2, 3, 4]] [1, [1, 2, 3]]
