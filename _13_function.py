# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180703","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 함수
#
# - 입력값을 가지고 어떤 일을 수행한 다음 그 결과물을 내 놓는 것
# - 함수를 사용하는 이유?
#       > 반복되는 부분이 있을 경우 재활용을 위해
#       > 프로그램의 흐름을 일목요연하게 볼 수 있다
#

# 함수 정의하기
#
# - Def 키워드를 이용하여 정의
# - 함수 이름과 인수들이 기술
# - 함수 선언부는 :로 끝난다
# - 들여쓰기 규칙이 적용
# - 함수으 끝은 들여쓰기가 적용 안되는 라인에서 끝난다.
#

def dummy():
    pass        # 실행할 내용이 없을때는 pass
                # 함수 이름만 만들어주고, 내용이 없으면 syntax error
                # 반드시 pass를 써줘야 함
                
def my_function():
    print("Hello Python!!")

def add(a,b):
    return a+b  # 결과값을 돌려줘야 할 때는 return문으로 반환

def do_nothing():
    return      # return문만 썼을 경우, None이 반환

dummy()
my_function()           # Hello Python!!
print(add(10,20))       # 30
print(do_nothing())     # None


# 함수도 객체이므로 다음과 같은 호출도 가능하다 ★★
#

a = add
print(a(100,200))           # 300
print(a, add, sep = "\n")   # <function add at 0x000002310DDE6048>
                            # <function add at 0x000002310DDE6048>

print("-------------------------------------------------")

# return
#
# - 함수를 종료시키고, 해당 함수를 호출한 곳으로 되돌아 가게 한다.
# - 파이썬에서는 어떤 종류의 객체도 반환할 수 있다.
# - 여러 객체를 return 하면 '튜플'로 반환한다 ★★
# - return문을 만나면 함수는 종료한다.
# - return문만 사용하면 None을 반환한다.
# - 함수가 끝날 때까지 종료할 필요가 없고 반환할 값이 없을 때는,
#   return문이 없어도 된다.
#

def do_nothing():
    return              # 인수 없이 return -> None을 반환

def say_hello():
    print("Hello~~")    # return문이 필요 없는 경우도 있다.

def max_value(a,b):
    if a>b:
        return a        
    else:
        return b        # 1개의 값을 return

def swap(a,b):
    return b,a          # 여러개의 값을 return할 수 있다.
                        
print(swap(10,20))      # (20, 10)  -> '튜플'로 return한다.
a,b = swap(10,20)
print(a,b)              # 20 10



print("-------------------------------------------------")

# 인수의 전달 방법
#
# - 기본적으로 참조에 의한 호출(Call-by-Reference)
# - But, 인수의 타입(Mutable or Immutable)에 따라 처리 방식이 달라진다
#

# Mutable 객체를 인수로 전달할 경우
#

def g(t):
    t[0] = 0
a = [1,2,3]
print(a)                    # [1, 2, 3]
g(a)
print(a)                    # [0, 2, 3]         (바뀐다!!)

# Immutable 객체를 인수로 전달할 경우
#

def h(t) :
    t = (10,20,30)
a = (1,2,3)
print(a)                    # (1, 2, 3)
h(a)
print(a)                    # (1, 2, 3)         (안바뀐다!!)


print("-------------------------------------------------")

# 스코핑 룰(Scope)
#
# - 이름공간(Namespace) : 프로그램에서 사용되는 이름들이 저장되는 공간
# - 이름은 값을 치환할 때, 해당 값의 객체와 함께 생겨나고 이름공간에 저장
# - 이름공간에 저장된 이름을 통해 객체를 참조
# - 이름공간의 종류
#       > Local Scope : 함수 내부
#       > Enclosed : Function in Function
#       > Global : 모듈 내부
#       > Built-in : 내장 영역
# - 동일한 이름이 여러 영역에 있다면 LEGB 순으로 찾는다
#

x = 1
def func(a):
    return a+x      # Local Scope에 x가 없으므로 Global x를 사용한다.
def func2(a):
    x = 2
    return a+x      # Local Scope에 x가 있으므로 Local x를 사용한다.

print(func(10))     # 11
print(func2(10))    # 12
print(x)            # 1


# - 함수 내부에서 전역 객체를 사용해야 하는 경우 global 선언문을 이용한다
# - 가능하면 함수 내부에서 글로벌 객체를 직접 사용하는 것은 피하도록 하자!!

g = 1
def func3(a):
    global g        # Global g 를 사용하겠다!
    g = 3           # g객체는 global 객체이다.
    return a+g
print(func3(10))    # 13
print(g)            # 3

print("-------------------------------------------------")

# 함수의 인수
#
# - 인수는 필요한 개수만큼 선언할 수 있다.
# - 기본값이 필요하면 함수 선언시 지정할 수 있다.
#

def sum(a,b):
    return a+b
def incr(a, step = 1):      # step의 기본값은 1
    return a+step

print(sum(2,3))             # 5
print(incr(10))             # 11        step의 기본값 1 사용
print(incr(10,2))           # 12        step의 값 직접 지정함

print("-------------------------------------------------")

# 함수의 인수_ 키워드 인수
#
# - 인수값을 인수 이름으로 전달할 수 있다.( 함수의 정의에 따른다 )
#

def area(width, height):
    return width * height

print(area(10,12))
print(area(height=4,width=3))       # == area(3,4)

print("-------------------------------------------------")

# 함수의 인수_ 가변 인수
#
# - 정해지지 않은 개수의 인수값을 받을 때 사용한다.
# - 선언시 인수명 앞에 *를 붙여 선언한다.
#

def get_total(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(get_total(1,2,3,4,5,6,7,8,9,10))


# 아래 두개의 코드는 같은 내용이다!

a = list(range(3,6))
print(a, type(a), len(a))           # [3, 4, 5] <class 'list'> 3

args = [3, 6]
a = list(range(*args))
print(a, type(a), len(a))           # [3, 4, 5] <class 'list'> 3


print("-------------------------------------------------")

# 함수의 인수_ 사전 키워드 전달
#
# - 정해지지 않은 키워드 인수는 모두 dict로 받을 수 있다.
# - 선언시 인수명 앞에 **를 붙인다
# - 사전 키워드 인수는 선언의 맨 마지막에 있어야 한다.
#

def func(a,b,*args,**kwd):
    print(a,b)
    print(args)
    print(kwd)
    
func(10,20,30,40,depth=10,dimension=3)  # 10 20
                                        # (30, 40)  -> *는 가변인수 '튜플★'
                                        #           (정해지지 않은 개수의 인수들)
                                        # {'depth': 10, 'dimension': 3}
                                        # -> 정해지지 않은 키워드 인수는 **
                                        #    'dict'형으로 받아진다 ★

print("-------------------------------------------------")

# 함수 객체를 인수로 전달
#
# - 파이썬에서는 함수도 객체이다.
# - 따라서 인수로 함수를 전달하는 것도 가능하다
#

states = ['gunPO','anYang ','gwAcheon ',' gwAngmYeong ','euiwang     ',
          'suwon  ','      chEOnan','    ansan  ']

def clean_strings(strings, *funcs):     # 함수 목록을 가변 인수로 전달
    results = []
    for string in strings:
        for func in funcs:              # 전달된 함수들을 순차적으로 적용
            string = func(string)
        results.append(string)
    return results

states = clean_strings(states, str.strip, str.title)
print(states)                   # ['Gunpo', 'Anyang', 'Gwacheon', 'Gwangmyeong'
                                # , 'Euiwang', 'Suwon', 'Cheonan', 'Ansan']
                                #
                                # strname.strip() : 문자열 좌우의 공백문자 제거
                                # strname.title() : 각 단어의 첫글자 대문자로!

print("-------------------------------------------------")

# 익명 함수(Lambda) ★★
#
# - 이름이 정의되지 않은 '익명 함수'를 선언
# - 데이터 분석/변형 함수에서 파라미터로 처리 함수를 인자로 받는 경우가 많다.
#

def square(x):
    return x**2

for i in range(10):
    print("{0}^2 = {1}".format(i+1,square(i+1)))

# 위의 함수를 Lambda를 이용하여 만든다면?
#

for i in range(1,11):
    print("{0}^2 = {1}".format(i,(lambda x : x**2)(i)))


print("-------------------------------------------------")

# Lambda를 이용한 정렬
#
# - 정렬할 때, key 함수로 정의하기에도 편리한 경우가 많다.

strings = ['foo','card','bar','aaaa','abab','abab','foo']


strings.sort(key= lambda x : len(x))
print(strings)              # ['foo', 'bar', 'foo', 'card', 'aaaa', 'abab', 'abab']

# lambda x : len(x) 는
# def a:
#   return len(x) 과 같다.

strings.sort(key= lambda x : strings.count(x))
print(strings)              # ['foo', 'bar', 'foo', 'card', 'aaaa', 'abab', 'abab']
                            # list.count(x) : 리스트 내의 x의 개수를 반환
                            # 왜 위랑 똑같이 나오지?!?!

print("-------------------------------------------------")

# 강사님 예제 코딩

def intro_mycar(manu, seats=4, type="sedan"):
    print('내차는',manu,'의',seats,'인승',type,'이다.')


intro_mycar(manu='기아')              # 내차는 기아 의 4 인승 sedan 이다.
intro_mycar(manu='기아', type='SUV')  # 내차는 기아 의 4 인승 SUV 이다.
intro_mycar(type='SUV', manu='현대')  # 내차는 현대 의 4 인승 SUV 이다.
intro_mycar('Audi',2,'스포츠카')      # 내차는 Audi 의 2 인승 스포츠카 이다.
intro_mycar('Audi', seats=2)          # 내차는 Audi 의 2 인승 sedan 이다.

# intro_mycar()                       # 필수 인자값 manu 누락 -> TypeError

# intro_mycar(manu='현대',2)          # 키워드 인자값 뒤에 키워드 없는 인자값 X
                                      # 실행 아예 안됨

# intro_mycar('기아', manu='현대')    # 같은 매개변수에 중복 인자값 대입 불가
                                      # TypeError

# intro_mycar(color='회색')            # color라는 키워드가 없으므로 TypeError
                                      

input = {'manu':'현대','seats':9,'type':'승합차'}
intro_mycar(**input)                  # 내차는 현대 의 9 인승 승합차 이다.


print("-------------------------------------------------")


def my_func():
    """ 여기에 함수에 대한 상세 설명*function document)을 넣습니다.
    여러줄이 들어갈 수 있으며, 함수의 내장 변수(__doc__)를 사용하여
    출력할 수 있습니다.
    """
    pass

print(my_func.__doc__)
                    #  여기에 함수에 대한 상세 설명*function document)을 넣습니다.
                    #     여러줄이 들어갈 수 있으며, 함수의 내장 변수(__doc__)를 사용하여
                    #     출력할 수 있습니다.

# print(open.__doc__)       # 마찬가지로 __doc__를 이용하여 open함수에 대한 정보를 얻을 수 있다.

print("-------------------------------------------------")