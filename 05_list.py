# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180703","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# List
# - 순서를 갖는 개체들의 집합, 파이썬 자료형들 중 가장 많이 사용
# - 리스트 생성과 연산
#       - 시퀀스 자료형 : 시퀀스 연산(인덱싱, 슬라이싱, 연결, 반복, len, in, not in)
#       - 변경 가능(mutable) 자료형이므로 항목의 추가, 변경, 삭제 모두 가능

        # (복습) Mutable, Immutable
        # str1+str2 를 하면 둘의 원본으 전혀 바뀌지 않고
        # str1+str2 에 해당하는 새로운 객체가 생성된다 -> Immutable


L = [1,2,'python']                  # List는 [ ] 기호를 이용하여 생성
print(type(L))                      # <class 'list'>
print(L[-2],L[-1],L[0],L[1],L[2])   # 2 python 1 2 python   ★작은따옴표 X
print(L[1:3])                       # [2, 'python']
print(L*2)                          # [1, 2, 'python', 1, 2, 'python'] 
print(L+[3,4,5])                    # [1, 2, 'python', 3, 4, 5]
print(len(L))                       # 3
print(2 in L)                       # True

print(L)                            # [1, 2, 'python']
del L[0]
print(L)                            # [2, 'python']

print("-------------------------------------------------")

# 항목의 변경

a=['apple','banana',10,20]
a[2] = a[2] + 90            # mutable 자료형 -> 항목 변경 가능
print(a)
# 슬라이스를 이용한 치환

a = [1,12,123,1234]
print(a)                    # [1,12,123,1234]
a[0:2] = [10,20]            # a[0]과 a[1]을 '10'과 '20'으로 각각 변경
print(a)                    # [10,20,123,1234]
a[0:2] = [99]               # a[0]과 a[1]을 합쳐서 '99'로 만듬
print(a)                    # [99,123,1234]
a[1:2] = [20]               # a[1]을 20으로 변경
print(a)                    # [99,20,1234]
a[1]='banana'               # a[1]을 'banana'로 변경
print(a)                    # [99,'banana',1234]

a[1:2] = 'Banana'           # a[1]을 합쳐서 'B','a','n','a','n','a'로 변경
print(a)                    # [99,'Banana',1234]
a[7:] = '마시쩡'            # a[7:]을 '마','시','쩡' 으로 변경 
print(a)                    # [99, 'B', 'a', 'n', 'a', 'n', 'a', '마', '시', '쩡']
a[0:] = [100]
print(a)                    # [100]

        # 잘 봐두자!!! ★헷갈림★
a=[10,20,30]
a[2] = 'banana'
print(a)                    # [10,20,'banana']
a[2:] = 'banana'           
print(a)                    # [10,20,'b','a','n','a','n','a']
a=[10,20,30]
a[2] = ['banana']           
print(a)                    # [10, 20, ['banana']]
a[2:] = ['banana']
print(a)                    # [10, 20, 'banana']


print("-------------------------------------------------")

# 슬라이스를 이용한 삭제

a = [1,12,123,1234]
print(a)                    # [1, 12, 123, 1234]
a[1] = []
print(a)                    # [1, [], 123, 1234]    -> 삭제 X
a[1:2] = []             
print(a)                    # [1, 123, 1234]        -> 삭제 O
a[0:] = []
print(a)                    # []                    -> 모두 삭제

# 슬라이스를 이용한 삽입

a = [1,12,123,1234]
print(a)                    # [1, 12, 123, 1234]
a[1] = 'a'
print(a)                    # [1, 'a', 123, 1234]                -> 삽입 X, 치환
a[1:1] = 'b'
print(a)                    # [1, 'b', 'a', 123, 1234]           -> 삽입 O
a[5:] = [12345]
#a[5:] = 12345              # 에러
print(a)                    # [1, 'b', 'a', 123, 1234, 12345]    -> 맨끝 삽입
a[:0] = [-12,-1,0]
print(a)                    # [-12,-1,0,1,'b,'a',123,1234,12345] -> 맨앞 삽입

print("-------------------------------------------------")

# 리스트의 메서드

a = [1,2,3]
print(a)

a.append(5)         # List.append(x) : List의 마지막에 x를 추가
print(a)            # [1, 2, 3, 5]
a.insert(3,4)       # List.insert(i,x) : List 인덱스 i위치에 x를 추가
print(a)            # [1, 2, 3, 4, 5]
print(a.count(2))   # List.count(x) : List 내의 x의 개수를 반환
a.reverse()         # List.reverse() : List를 역순으로 뒤집음
print(a)            # [5, 4, 3, 2, 1]
a.sort()            # List.sort() : List 요소를 순서대로 정렬
print(a)            # [1, 2, 3, 4, 5]
a.remove(3)         # List.remove(x) : List 에 있는 x값을 제거
print(a)            # [1, 2, 4, 5]            
a.extend([6,7,8])   # List.extend(list2) : List 마지막에 list2를 추가
print(a)            # [1, 2, 4, 5, 6, 7, 8]

print("-------------------------------------------------")

# 리스트를 Stack으로 사용하기 >> Last in, First Out
# - 리스트의 append와 pop 메소드를 이용하여 스택을 구현할 수 있다.

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)        # [10, 20, 30]
print(stack.pop())  # 30
print(stack.pop())  # 20
print(stack)        # [10]

print("-------------------------------------------------")

# 리스트를 Queue로 사용하기 >> First in, First Out
# - 리스트의 append와 pop 메서드를 이용하여 스택을 구현할 수 있다.

queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
print(queue)        # [10, 20, 30, 40]
print(queue.pop(0)) # [10]  
print(queue.pop(0)) # [20]      >> 가장 앞쪽 인덱스 요소를 pop
print(queue.pop(0)) # [30]
print(queue)        # [40]

print("-------------------------------------------------")

# sort 메서드의 활용 
# - sort 메서드의 reverse 를 True로 설정하면 역순으로 정렬할 수 있다.

a = [1,5,3,9,8,4,2]
a.sort()
print(a)                # [1, 2, 3, 4, 5, 8, 9]
a = [1,5,3,9,8,4,2]
a.sort(reverse=True)
print(a)                # [9, 8, 5, 4, 3, 2, 1]

print("-------------------------------------------------")

# sort 메서드의 활용
# - 키값 기반의 사용자 정의 정렬

a = [10, 2, 22, 9, 8, 33, 4, 11]
a.sort(key=str)                     # 문자열 가나다순 정렬
print(a)                            # [10, 11, 2, 22, 33, 4, 8, 9]

a = [10, 2, 22, 9, 8, 33, 4, 11]    
a.sort(key=str, reverse=True)       # 문자열 가나다 역순 정렬
print(a)                            # [9, 8, 4, 33, 22, 2, 11, 10]

a = [10, 2, 22, 9, 8, 33, 4, 11]
a.sort(key=int)                     # 숫자크기 순 정렬
print(a)                            # [2, 4, 8, 9, 10, 11, 22, 33]

a = [10, 2, 22, 9, 8, 33, 4, 11]
a.sort(key=int, reverse=True)       # 숫자크기 역순 정렬
print(a)                            # [33, 22, 11, 10, 9, 8, 4, 2]

print("-------------------------------------------------")
