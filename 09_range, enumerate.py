# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180703","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 순차 자료형(Sequence) 내장 함수 : range
#
# range({start=0,} end {, step = 1})
#   >> start 이상 ★end 미만★까지의 순차적 '리스트'를 step 간격으로 생성
#

seq = range(10)                     # 0 이상 10미만의 순차적 정수 목록
print(seq, "type =", type(seq))     # range(0, 10) type = <class 'range'>
print(seq[0:])                      # range(0, 10)
print(len(seq))                     # 10     >> 11이 아니다★★

for i in seq:
    print(i,end=' ')                # 0 1 2 3 4 5 6 7 8 9
print()                             # 10까지 나오지 않는다 ★★★★


seq2 = range(5,15)                  # 5이상 15미만의 순차적 정수 목록
print(len(seq2))                    # 10     >> 11이 아니다★★
for idx in seq2:
    print(idx,end=' ')              # 5 6 7 8 9 10 11 12 13 14
print()

seq3 = range(0,-20,-1)              # 0이하 -10초과의 순차적 정수 목록
print(len(seq3))
for j in seq3:
    print(j, end=' ')
    j-=2                            # 이렇게 쓰더라도
print()                             # 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11 -12 -13 -14 -15 -16 -17 -18 -19


print("-------------------------------------------------")

# 순차 자료형(Sequence) 내장 함수 : enumerate
#
#   - 순차 자료형에서 현재 아이템의 색인과 함께 처리하고자 할 때 흔히 사용
#   - 0부터 인덱싱!

i = 0
for value in ['red','yellow','blue','white','grey']:
    print('{0} -> {1}'.format(i,value))
    i+=1


# enumerate 함수를 사용할때와 비교

for i,value in enumerate(['red','yellow','blue','white','grey']):
    print('{0} -> {1}'.format(i,value))

# 둘다 출력은 동일
# 0 -> red
# 1 -> yellow
# 2 -> blue
# 3 -> white
# 4 -> grey

# (차이점)
# 1. 위에는 i=0이라는 초기화가 있지만 아래엔 없다
# 2. 위에는 for value in [List]를 사용했지만,
#    아래는 for i,value in enumerate([List]) 사용
# 3. 위에는 i+=1을 해주지만, 아래에선 해주지 않는다. -> 인덱스 자동으로 증가

print("-------------------------------------------------")
