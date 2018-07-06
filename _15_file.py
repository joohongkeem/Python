# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180704","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 파일의 생성과 파일 모드
#
# 파일객체 = open({파일명}, {파일모드} [, enconding='인코딩'])
#
#   파일모드
#    (default) r : 읽기 모드 - 파일을 읽기만 할 때 사용
#              w : 쓰기 모드 - 파일에 내용을 기록할 때 사용
#              a : 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
#
#   파일모드
#    (default) t : 텍스트 모드
#              b : 바이너리 모드
#


# 파일 제어 기본 함수
#
#       open  : 파일을 생성한다.
#       write : 파일에 내용을 기록한다.
#       read  : 파일에서 내용을 읽어온다.
#       close : 파일 사용을 끝낸다.
#               파일을 열었으면(open) 반드시 사용 후 닫아주도록 한다.
#

# File Write

f = open('91.txt','w',encoding='utf-8')
write_size = f.write("Life is too short, You need Python")  # 91.txt파일 생김
print(write_size)                                           # 34 출력
f.close()

# File Write

f = open('92.txt', 'w', encoding='utf-8')
for i in range(1,10):
    f.write("%d: Life is too short, You need Python\n"%i)
f.close()

# File Read

f = open('92.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close
            # 1: Life is too short, You need Python
            # 2: Life is too short, You need Python
            # 3: Life is too short, You need Python
            # 4: Life is too short, You need Python
            # 5: Life is too short, You need Python
            # 6: Life is too short, You need Python
            # 7: Life is too short, You need Python
            # 8: Life is too short, You need Python
            # 9: Life is too short, You need Python


print("-------------------------------------------------")


# readline
#
# - readline 함수를 이용하면 텍스트 파일을 줄 단위로 읽어올 수 있다.
#   readline(O) readlines(X)

f = open('92.txt','r')

while True:
    line = f.readline()
    if not line:
        break               # 읽어올 줄이 없으면 무한루프 탈출
    print(line,end='')

f.close()
            # 1: Life is too short, You need Python
            # 2: Life is too short, You need Python
            # 3: Life is too short, You need Python
            # 4: Life is too short, You need Python
            # 5: Life is too short, You need Python
            # 6: Life is too short, You need Python
            # 7: Life is too short, You need Python
            # 8: Life is too short, You need Python
            # 9: Life is too short, You need Python


# - readlines 함수를 이용하면 모든 라인을 불러 리스트로 제공한다.
#   readline(X) readlines(O)

f = open('92.txt','r')

lines = f.readlines()
print(lines)

for line in lines:
    print(line,end='')

f.close()
            # 1: Life is too short, You need Python
            # 2: Life is too short, You need Python
            # 3: Life is too short, You need Python
            # 4: Life is too short, You need Python
            # 5: Life is too short, You need Python
            # 6: Life is too short, You need Python
            # 7: Life is too short, You need Python
            # 8: Life is too short, You need Python
            # 9: Life is too short, You need Python

print("-------------------------------------------------")

# 바이너리(Binary) 파일 다루기
#
# - 바이너리 파일을 다루려면 모드를 바이너리로 지정해야 한다.
#

# f = open('03.jpg')                # 바이너리 모드가 아니므로 에러!

# Copy binary Sample

f_src = open('93.jpg','rb')         # 바이너리 읽기 모드
data = f_src.read()
f_src.close()
# print(data)                       # 엄청 오래걸림

f_dest = open('93_copy.jpg','wb')   # 바이너리 쓰기 모드
f_dest.write(data)                  # 이 값을 프린트해보면, 파일 크기 출력
f_dest.close()


print("-------------------------------------------------")

# 파일 관련 함수
#
# - seek : 사용자가 원하는 위치로 파일 포인터 이동
# - tell : 현재 파일에서 어디까지 읽고 썼는지 위치를 반환

f = open('94.txt','w', encoding = 'utf-8')
data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n"
f.write(data)
f.close()

f = open('94.txt', 'r', encoding = 'utf-8')

pos = f.tell()
print(pos)              # 0 : 처음 파일 포인터의 위치

text = f.readline()     
print(text)             # ABCDEFGHIJKLMNOPQRSTUVWXYZ\n
                        #
pos = f.tell()          
print(pos)              # 28 : 알파벳 26글자, NULL문자는 2개로 계산 ?!


f.seek(16)
pos = f.tell()
print(pos)              # 16 : 파일포인터를 16으로 이동
text = f.readline()     # 16부터 널문자까지 읽음
print(text)             # QRSTUVWXYZ
pos = f.tell()
print(pos)              # 28
f.close()



# 질문, 한글을 wirte하려면 ?!?!?!
# - 한글 중간에 걸리게 seek해보기

print("-------------------------------------------------")

# with ~ as  : 자동 자원 정리
#
# - with ~ as를 이용하여 파일 입출력을 수행하면, 수동으로 파일을 close하지 않아도 된다.
#

with open('92.txt','r') as f_as:
    for line in f_as.readlines():
        print(line, end = "")

print(f_as.closed)                  # True 출력

print("-------------------------------------------------")