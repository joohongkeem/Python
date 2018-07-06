# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180704","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# Using Pickle
#
# - 객체의 내용을 파일에 저장하거나 복원해야 할 경우에 Pickle 모듈을 사용하면 편리
# - Pickle 모듈은 객체를 파일에 썼다가 나주에 복원할 수 있도록, 객체를 바이트 스트림으로 '직렬화'
#       > 모든 파이썬의 객체를 저장하고 읽을 수 있음
#       > 원하는 객체를 형태 변환 없이 쉽게 쓰고 읽을 수 있다.
# - Pickle 모듈을 사용하려면 import pickle을 이용하여 모듈을 로드해야 한다.
# - Pickle 모듈 주요 메서드
#       > dump(data, file [,protocol]) : data 객체를 [protocol을 이용해] file에 저장
#       > load (file) : file로부터 저장된 객체를 불러옴
#

# 객체의 저장(Pickling) - dump
#
# - file에 객체를 저장하고자 할 떄에는 dump 메서드를 이용한다.
# - dump 메서드에 프로토콜 버전을 정의해 줄 수 있다.
#       > 최신 프로토콜 버전을 확인하려면 pickle.HIGHEST_PROTOCOL로 확인
#


import pickle
f = open("95.bin","wb",)
print(pickle.HIGHEST_PROTOCOL)                          # 4
data = {"baseball":9}
pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)             # players.bin 파일 생성 후, data 정보를 넣는다.
f.close()

# 객체의 복원(Unpickling) - load
#
# - file로부터 객체를 불러올 때에는 load 메서드를 이용한다.
# - dump시에 PROTOCOL을 지정했더라도, load시에는 지정해주지 않아도 된다.
#       > pickle 파일에 PROTOCOL 버전이 저장되어 있음
#

import pickle
f = open("95.bin","rb")
data = pickle.load(f)
f.close()
print(data)                                             # {'baseball': 9}


print("-------------------------------------------------")

# 복수 객체의 저장
# - 기본적으로 Pickle은 단일 객체를 저장하는 포맷이지만,
#   dump메서드를 중복하여 사용하면 복수의 객체를 저장할 수 있다.
#
import pickle
with open("96.bin", "wb") as f:
    pickle.dump({"baseball":9}, f)
    pickle.dump({"soccer":11}, f)
    pickle.dump({"basketball":5}, f)

# 복수 객체의 복원
# - 저장된 객체를 복원하려면 load 메서드를 이용
#       > load가 수행될 때마다 한줄씩 불러들이며, 더 이상 불러올 객체가 없을 때 EOFError 발생
#

# 다음 코드의 문제점 찾아보기
#import pickle
#with open("96.bin","rb") as f:
#    print(pickle.load(f))
#    print(pickle.load(f))
#    print(pickle.load(f))
#    print(pickle.load(f))

            # [출력]
            # {'baseball': 9}
            # Traceback(most recent call last):
            # {'soccer': 11}
            # {'basketball': 5}
            #  File "C:/Users/bit-user/Desktop/주홍/Python/16_pickle.py", line 70, in < module >
            #   print(pickle.load(f))
            # EOFError: Ran out of input
            #
            # -> 에러내용이 위치 뒤죽박죽

# 올바른 코드
import pickle
with open("96.bin","rb") as f:
    data_list = []
    while True:
        try:
            data = pickle.load(f)
        except EOFError:
            break
        data_list.append(data)

print(data_list)                # [{'baseball': 9}, {'soccer': 11}, {'basketball': 5}]


print("-------------------------------------------------")

# Pickle 사용시 유의사항
#   - Pickle 은 단순 텍스트 저장이 아닌 바이트 스트림 직렬화를 이용한 것이므로
#     파일 모드는 반드시 "b"모드로 지정해야 한다.
#   - Pickle 에 사용되는 데이터 포맷은 파이썬에 특화되어 있기 때문에
#     다른 언어로 작성된 응용프로그램과의 데이터 교환에는 사용하지 않는 것이 좋다.
#   - 저장된 데이터에 대한 보안을 제공하지 않는 점에 유의하며 사용
#

print("-------------------------------------------------")