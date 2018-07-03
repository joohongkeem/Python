# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180703","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")


# 튜플  
#
# - 리스트와 거의 비슷하지만 다름 :
#   시퀀스(Sequence) 자료형, But!! 그 값을 바꿀 수 없는 Immutable 자료형(원본유지)
# - 튜플은 () 기호로 생성한며 , 
#   하나의 요소만을 가질 떄는 요소 뒤에 컴마(,)를 반드시 붙임★★★
# - 괄호를 생략해도 튜플로 인식
#
#   >> 각각의 세로열이 속성(Field)
#   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#   학번 | 이름 | 학교 | 주소 | ....    
#   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#   0111   John    A     군포   ...        >> 행 각각이 튜플, 총 갯수 Cardinality
#   0210    Sam    B     안양   ...           (파일 구조의 'Record)
#    ..      ..    ..     ..    ...
#    ..      ..    ..     ..    ...
#   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


tup = (1,2,3)
print(tup, "type =", type(tup))     # (1, 2, 3) type = <class 'tuple'>

tup = 1, 2, 'Python'                # 괄호를 생략해도 튜플을 생성할 수 있다.
print(tup, "type =", type(tup))     # (1, 2, 'Python') type = <class 'tuple'>

                                            # 인덱싱
print(tup[-2],tup[-1],tup[0],tup[1],tup[2]) # 2 Python 1 2 Python   ('Python' X)

                        # 슬라이싱
print(tup[1:3])         # (2, 'Python')
print(tup[:])           # (1, 2, 'Python')

                        # 반복
print(tup*2)            # (1, 2, 'Python', 1, 2, 'Python')
print(2*tup)            # (1, 2, 'Python', 1, 2, 'Python')

                        # 연결(+)
print(tup+(3,4,5))      # (1, 2, 'Python', 3, 4, 5)
print(len(tup))         # 5
print(5 in tup)         # True >> 요소 내부에 5가 있는지 확인

print("-------------------------------------------------")

# Packing과 Unpacking
#
# Packing : 나열된 객체를 Tuple로 저장하는 것
# Unpacking : 튜플, 리스트 안의 객체를 변수로 할당하는 것

t = 10, 20, 30, 'Python'
print(t)            # (10, 20, 30, 'Python')
print(type(t))      # <class 'tuple'>

                    
a, b, c, d = t                      # unpacking tuple
print(a,b,c,d)                      # 10 20 30 Python
# a, b = t                          # Unpacking시 왼쪽 변수가 부족하면, Error !!

a, b, c, d = [10, 20, 30, 'Ptyhon'] # unpacking list
print(a,b,c,d)                      # 10 20 30 Ptyhon


t = (1,2,3,4,5,6)                   # 확장 Unpacking
a, *b = t                           # 왼쪽 변수가 부족해도 사용 가능 
print(a,type(a))                    # 1 <class 'int'>
print(b,type(b))                    # [2, 3, 4, 5, 6] <class 'list'>
                                    #     >> *b 는 list로 할당 ★★★

a,b,*c = t
print(a,type(a))                    # 1 <class 'int'>
print(b,type(b))                    # 2 <class 'int'>
print(c,type(c))                    # [3, 4, 5, 6] <class 'list'>

a,*b,c = t
print(a,type(a))                    # 1 <class 'int'>
print(b,type(b))                    # [2, 3, 4, 5] <class 'list'>
print(c,type(c))                    # 6 <class 'int'>


L = [a,b,c,d]                       # packing List
print(L,type(L))                    # [1, [2, 3, 4, 5], 6, 'Ptyhon'] <class 'list'>
T = (a,b,c,d)                       # packign Tuple
print(T,type(T))                    # (1, [2, 3, 4, 5], 6, 'Ptyhon') <class 'tuple'>
T = a,b,c,d                         # 괄호 생략해도 Tuple로 인식 !
print(T,type(T))                    # (1, [2, 3, 4, 5], 6, 'Ptyhon') <class 'tuple'>

print("-------------------------------------------------")



