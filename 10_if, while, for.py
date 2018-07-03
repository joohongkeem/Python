# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180703","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# if - elif - else 조건문
#
# if 조건식1 :
#       구문1
#       구문2
# elif 조건식2  :
#       구문3
#       구문4
# else :
#       구문5
#

n=-2
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")           # Negative

print("-------------------------------------------------")

# 조건 표현식(Conditional Expression)
#
# (value = ) {true-expr} if {condition} else {false-expr}
#
# - C 또는 Java의 3항 연산자와 같은 역할을 한다

money = 8500
print("by Taxi" if money>10000 else "by Bus")   # by Bus


print("-------------------------------------------------")

# 조건문 - in, not in
#
# - 파이썬은 리스트, 튜플, 문자열, 사전, 집합등 에 in, not in 등
#   편리한 조건식을 제공
#

print(1 in [1,2,3])                         # True
print(1 not in [1,2,3])                     # False
print(1 in (1,2,3))                         # True
print(1 not in (1,2,3))                     # False
print("y"in "Python")                       # True
print("y" not in "Python")                  # False
print("배구" in {"배구":3,"농구":4})        # True
print("족구" in {"배구":3,"농구":4})        # False
print("배구" in {"배구","축구","농구"})     # True
print("배구" not in {"배구","축구","농구"}) # False

print("-------------------------------------------------")

# for 반복문
#
# for {TARGET} in {OBJECT} :
#       구문1
#       구문2
# else :
#       구문3
#
#
# - {OBJECT}는 list, str, tuple, bytes, bytearray, range 등 시퀀스 자료형
# - 반복횟수는 {OBJECT}의 크기
# - {OBJECT} 안의 객체를 하나씩 순차적으로 꺼내어 구문1, 구문2 가 실행됨
# - 반복이 정상적으로 끝나면 else 블록이 실행
# - for문 내에서 break로 빠져나오면 else 블록은 실행되지 않음
#

# list 객체를 이용한 for문

animals = ['사자','호랑이','낙타','독수리']
for animal in animals:
    print(animal, end = " ")
else:
    print("@")                      # 사자 호랑이 낙타 독수리 @

# range 객체를 이용한 for문

for x in range(0,21,2):
    print(x, end= " ")          
else:
    print("@")                      # 0 2 4 6 8 10 12 14 16 18 20 @

# for ~ else 문의 활용

for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
    if x>10:
        print("(break!)")
        break
    else:
        print(x,end= " ")
else:
    print("10보다 큰 수 없음")      # 1 2 3 4 5 6 7 8 9 10 (break!)
    
    
print("-------------------------------------------------")

# enumerate
#
# - 요소의 값은 물론, 인덱스가 필요할 경우 enumerate() 함수를 이용한다
#

colors = ['red','orange','yellow','green','pink','blue']

for i,color in enumerate(colors):
    print("idx =",i, ",color =",color)

        # idx = 0 ,color = red
        # idx = 1 ,color = orange
        # idx = 2 ,color = yellow
        # idx = 3 ,color = green
        # idx = 4 ,color = pink
        # idx = 5 ,color = blue

print("-------------------------------------------------")

# break
#
# - 어떤 조건에서 반복을 중지하고 빠져나가야 하는 경우 break 문
#

L = [1,3,5,7,9,11,12,13,15,17]

for x in L:
    if x%2 == 0:
        break
    print(x,end=' ')
print()                         # 1 3 5 7 9 11


print("-------------------------------------------------")

# continue
#
# - continue문을 만나면, 이후 구문은 실행하지 않고 처음으로 이동한다
#

L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for x in L:
    if x%2 != 0 :
        continue
    print(x, end=" ")           # 0 2 4 6 8 10 12 14 16 18 20 
print()

print("-------------------------------------------------")

# while 반복문
#
# while 조건식 :
#       구문1
#       구문2
# else:
#       구문3
#
# - 조건식이 참인 동안 구문 1,2가 반복 실행
# - else블록은 while문을 빠져나올 때 실행
# - 단, break로 while문을 빠져나올 경우 else 블록은 실행되지 않는다.
# - 무한루프에 빠지지 않도록 주의!!
#   (경우에 따라서는 의도적으로 무한루프를 돌리기도 한다)
#

counter = 1
while counter <11:
    print(counter, end = " ")
    counter += 1
else:
    print("끝")              # 1 2 3 4 5 6 7 8 9 10 끝

print("-------------------------------------------------")

# while문 내에서 break, continue, else 사용하기
    
i = 0
while i<30:
    i+= 1
    if i<5 :
        continue
    print(i, end=" ")
    if i>=10:
        break
else:
    print("break가 있기 때문에 이 문장은 출력되지 않을 것이다")
print()                          # 5 6 7 8 9 10


print("-------------------------------------------------")

# List 내포                                       (헷갈린다★)
#
# [{표현식} for {항목} in {객체} if {조건}]
#
# - 리스트 내포(List Comprehension)를 이용하면 좀더 직관적인 프로그램을 만들 수 있다
#

a = [1,6,4,13,8,3]
# a 리스트의 항목 중, 짝수인 것만 2배하여 result에 저장
result = [ i*2 for i in a if i%2==0 ]
print(result)                            # [12, 8, 16]

print("-------------------------------------------------")

# 무한루프
#
# - 조건을 True로 주면 무한루프를 구성할 수 있다.
# - break 문으로 루프를 탈출할 수 있는 조건이 있어야 한다.
#

while(True):
    print("Ctrl+C를 눌러 루프를 종료하십시오.")

print("-------------------------------------------------")
