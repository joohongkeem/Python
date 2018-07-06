# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180703","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 사전(dict)      -> Map과 비슷
#
# - 순서를 가지지 않는 객체의 집합
# - Key 기반으로 값을 저장하고 참조하는 매핑형 자료형
# - 시퀀스 자료형이 아니므로 len(), in, not in() 정도만 가능
# - 인덱스가 없으므로 key를 이용하여 접근!!
#

dic={'basketball':5, 'soccer':11, 'baseball':9}
                            # 'basketball','soccer','baseball' : KEY
                            #                       5, 11, 9   : VALUE
                            #
print(dic)                  # {'basketball': 5, 'soccer': 11, 'baseball': 9}
print(type(dic))            # <class 'dict'>

print(dic['basketball'])    # 5
#print(dic[5])              # 에러

dic['volleyball']=6;        # dic에 새로운 객체 추가 >> dicname[KEY] = VALUE
print(dic)                  # {'basketball': 5, 'soccer': 11, 'baseball': 9, 'volleyball': 6}

print(len(dic))                 # 4
print('soccer' in dic)          # True
print('volleyball' not in dic)  # False


print("-------------------------------------------------")

# 다양한 사전 생성 방법

d = dict()                          # empty dict
print(d)                            # {}

d = dict(one=1, two=2)              # keyword arguments
print(d)                            # {'one': 1, 'two': 2}
d = dict(three=3,four=4)
print(d)                            # {'three': 3, 'four': 4}

d = dict([('one',1), ('two',2)])    # tuple list
print(d)                            # {'one': 1, 'two': 2}

keys=('one','two','three')
values=(1,2,3)
d = dict(zip(keys, values))         # 키와 값을 별도로 선언후 합침
print(d)                            # {'one': 1, 'two': 2, 'three': 3}

print("-------------------------------------------------")

# 사전의 키(Key)
#   - 사전의 키는 해싱해야 하기떄문에, 수정 불가능한 객체여야 한다
#     Ex) bool, 수치형(int, float, complex), str, tuple

d ={}
print(d)
                    # 사전에 객체 추가 >> dicname[KEY] = VALUE
d[True] = 'true'
print(d)            # {True: 'true'}
d[10] = '10'
print(d)            # {True: 'true', 10: '10'}
d["twenty"] = '20'  
print(d)            # {True: 'true', 10: '10', 'twenty': '20'}
d[(1,2,3)] = '6'
print(d)            # {True: 'true', 10: '10', 'twenty': '20', (1, 2, 3): '6'}

#d[[1,2,3]] = '6'    # 에러발생
                     # Why? 사전의 키는 '수정 불가능한 객체' 여야 한다.


print("-------------------------------------------------")

# 사전의 메서드

d = {'농구':5, '축구':11, '야구':9}
d['배구']=6         # 새로운 값 할당
print(d)            # {'농구': 5, '축구': 11, '야구': 9, '배구': 6}


print(d.keys())     # dicname.keys() : 사전내 키 목록을 dict_keys 객체로 반환
                    # dict_keys(['농구', '축구', '야구', '배구'])

print(d.values())   # dicname.values() : 사전내 값 목록을 dict_values 객체로 반환
                    # dict_values([5, 11, 9, 6])

print(d.items())    # dicname.items() : 사전내 키-값 쌍을 (KEY,VALUE)튜플로 묶어 dict_items 객체로 반환
                    # dict_items([('농구', 5), ('축구', 11), ('야구', 9), ('배구', 6)])

                        # dict_keys, dict_values, dict_items를 리스트로 사용하려면 list()함수를 활용
print(list(d.keys()))   # ['농구', '축구', '야구', '배구']
print(list(d.values())) # [5, 11, 9, 6]
print(list(d.items()))  # [('농구', 5), ('축구', 11), ('야구', 9), ('배구', 6)]


x = d.get('배구')       # dicname.get(KEY {,default})
                        # - 사전내 key에 대응하는 값을 반환
                        # - default를 지정하면 key에 대응하는 값이 없을 때 default 반환
print(x)                            # 6
print(d.get('족구'))                # None        >> 값이 없으면 기본적으로 None 반환★
print(d.get('족구',"없어임마"))     # 없어임마

del d['축구']         # del dicname[KEY]  : 사전 내에 KEY에 대응하는 객체를 삭제
print(d)              # {'농구': 5, '야구': 9, '배구': 6}

d.clear()             # dicname.clear() : 사전을 비움
print(d)              # {}
                      # [★주의사항★]
                      # 집합 s에 print(clear(s)) 하면 set() 으로 출력됐다

print("-------------------------------------------------")

# 사전 순회

d = {'농구':5, '축구':11, '야구': 9}


for key in d:   # 이렇게 사용하면, key값을 모두 순회하며 반복문 실행. (그렇다고 key가 키워드는 XX)
    print(str(key) + ":" + str(d[key]), end = ',')
else:
    print("끝")
                # 농구:5,축구:11,야구:9,끝
                # key가 존재하는동안, 반복문 실행


key = 5                     # 여기에  key = 5 써도 아래 순회엔  전혀 지장 XXX
print(key)                  # 5

for key in d.keys():
    print("{0}의 키값은 {1}이다.".format(key,d[key]), end='\n')

else:
    print("끝")
                # 농구의 값은 5이다.
                # 축구의 값은 11이다.
                # 야구의 값은 9이다.
                # 끝
                # "{0}, {1}".format(key,d[key])하면 {0}에 key, {1}에 d[key]가 들어간다.

print("key =",key)          # key = 야구


for key, value in d.items():
    print("{0} = {1}, {2} = {3}".format("KEY",key,"VALUE",d[key]))
else :
    print("끝")
                # KEY = 농구, VALUE = 5
                # KEY = 축구, VALUE = 11
                # KEY = 야구, VALUE = 9
                # 끝

print("-------------------------------------------------")
