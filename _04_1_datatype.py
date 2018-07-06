# Run module(Hot key : F5)
print("#20180702","Made by joohongkeem",sep=' ',end='#\n')
print("--------------------------------------")

# 자료형의 분류

# [접근방법]
#   - 직접(Direct)     : int, float, complex, bool
#   - 시퀀스(Sequence) : bytes, str, list, tuple
#   - 매핑(Mapping)    : dict

# [변경가능성]
#   - 변경 가능(Mutable)     : list, set, dict
#   - 변경 불가능(Immutable) : int, float, complex, bool, bytes, str, tuple

# [저장 모델]
#   - 리터럴(Literal) : int, float, complex, bool, bytes, str
#   - 저장(Container) : list, tuple, dict, set

# List : 순서 O, 중복 데이터 허용
# Set  : 순서 X, 중복 데이터 불허용
# Map  : Key와 Value가 함께 다닌다. Ex) 지역번호. 02-서울, 031-경기, ...

print("--------------------------------------")

a=1
print(a>10)
print(a<10)
b=a==1
print(b)
print(type(b))
print(b+10)
print(True+True)

print("--------------------------------------")

a= 30
print(type(a))
print(isinstance(a,int))
print(isinstance(a,float))

# 10진수 -> 2,8,6진수 변환

print("[10진수]",a)
print("[2 진수]",bin(a))
print("[8 진수]",oct(a))
print("[16진수]",hex(a))

print("type(a)=",type(a))               # int 클래스의 객체
print("type(bin(a))=",type(bin(a)))     # str 클래스의 객체

print(isinstance(a,int))
print(isinstance(bin(a),str))

b=0b1101        # 2진수
c=0o23142       # 8진수
d=0x23AB4       # 16진수
print(b,c,d)    # 10진수로 변환된 값이 출력된다


print("--------------------------------------")

a = 3
b = 3.0
c = 3.33

#print(a.is_integer())  # is_integer()함수는 float객체에서 선언된 것, int에선 못씀
print(b.is_integer())   # True
print(c.is_integer())   # False

print("--------------------------------------")

# 논리형엔 or, and, not 세가지가 있다.
print(True and True)
print(True and False)
print(False and True)
print(False and False,"\n")

print(True or True)
print(True or False)
print(False or True)
print(False or False,"\n")

print(not True)
print(not False)

print("--------------------------------------")

# 수치형

# int
a = 23
print(type(a))
print(isinstance(a,int))

# float
a = 1.2
print(type(a))
print(isinstance(a,float))
print(a.is_integer())
b=3e3
c=-0.2E-4
print(a,b,c)
print(b.is_integer())


# complex
a = 4+5j
print(type(a))
print(isinstance(a,complex))
print(a.real,a.imag)
b = complex(7,-2)
print(b)

print("--------------------------------------")

# 내장 수치 함수

print(abs(-3))
print(int(3.141592))
print(float(3))
print(complex(1,2))
print(divmod(10,3))
print(pow(2,10))

print("--------------------------------------")

# 비트 연산자

print(bin(0b0001 << 2))             # 왼쪽으로 2bit 이동   (*4  와 같다)
print(bin(0b1000 >> 2))             # 오른쪽으로 2bit 이동 (//4 와 같다)
print(bin(0b00001000&0b11111111))   # 비트 AND를 이용한 필터링
print(bin (8 | 2))                  # 비트OR연산

print("--------------------------------------")
