# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180703","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 세트(Set)
#
# - 순서가 없고, 중복이 없는 객체들의 집합 (Non Sequence) >> { } 로 정의
#       >> len(), in, not in 정도만 활용 가능
# - 수정이 가능한(Mutable) 자료형
# - 수학의 집합을 표현할 때 사용한다.


a = {}
print(a, type(a))            # 그냥 {}하면 <class 'dict'> ★★★★
                             # 집합으로 만들려면 set()

a = {1,2,3}
print(a)            # {1, 2, 3}
print(type(a))      # <class 'set'>
print(len(a))       # 3
print(2 in a)       # True
print(2 not in a)   # False

print("-------------------------------------------------")

# 세트의 메서드

s = {1,2,3}

s.add(4)            # setname.add(x) : 세트에 x를 추가
s.add(1)            #          순서가 없으므로, 이미 값 있을 경우 알아서 무
print(s)            # {1, 2, 3, 4}

s.discard(2)        # setname.discard(x) : 세트에서 x를 제거, x가 없으면 무시
print(s)            # {1, 3, 4}

s.remove(3)         # setname.remove(x) :  세트에서 x를 제거, x가 없으면 오류
print(s)            # {1, 4}
#s.remove(10)       # 에러발생

s.update({2,3})     # setname.update({setname2}) : 세트에 여러개의 값을 추가
print(s)            # {1, 2, 3, 4}  >> Set은 순서가 없지만, 정렬되서 들어가는듯

s.clear()           # setname.clear() : 세트를 비움
print(s)            # set()         >>  이렇게 출력된다!!!
                    # Why?
                    # dicname.clear() 했을때 {}으로 출력되므로 구분하기 위함!

print("-------------------------------------------------")


# 교집합, 합집합, 차집합, 모집합, 부분집합

s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {10,20,30}

s3 = s1.union(s2)           # setname.union(setname2)   :   합집합
print(s3)
s3 = s1 | s2                # setname1 | setname2       :   합집합
print(s3)

s3 = s1.intersection(s2)    # setname.intersection(setname2) : 교집합
print(s3)
s3 = s1 & s2                # setname1 & setname2            : 교집합
print(s3)

s3 = s1.difference(s2)      # setname.difference(setname2) : 차집합
print(s3)
s3 = s1 - s2                # setname1 - setname2          : 차집합
print(s3)

s1 = {1,2,3,4,5}
s2 = {1,2,3}
s3 = {1,2,3,4,5,6,7,8}

                            # setname1.issuperset(setname2) : 모집합
print(s1.issuperset(s2))    # True
print(s1.issuperset(s3))    # False

                            # setname1.issubset(setname2)   : 부분집합
print(s1.issubset(s2))      # False
print(s1.issubset(s3))      # True


print("-------------------------------------------------")
