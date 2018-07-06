# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180704","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 예외 처리
#
# - 오류는 프로그램이 잘못 작동괴는 것을 막기 위한 파이썬의 처리
# - 이 오류를 회피하기 위한 동작을 예외 처리라 한다.
#


list = []
# print(list[0])            # IndexError: list index out of range
                            # 내부에 인덱스 0에 매칭괴는 값이 없으므로 Error

test = "Try convert me to int"
# number = int(test)        # ValueError: invalid literal for int() with base 10: 'Try convert me to int'
                            # 정수 형식의 문자열이 아니어서 변환이 불가!

# result = 4/0              # ZeroDivisionError: division by zero
                            # 0으로는 나눗셈을 할 수 없다.

print("-------------------------------------------------")

# 오류의 회피 - try, except
#
# try:
#       문장1
# except:
#       문장2
#
# -> 문장1을 시도해보고, 오류가 발생하면 문장2를 실행한다.
#

try:
    print(1/3)
except:
    print("Error")
                            # 0.3333333333333333
try:
    print(1/0)
except:
    print("Error")
                            # Error

print("-------------------------------------------------")

# 특정 오류의 회피
#
# try:
#       문장1
# except {발생오류}:
#       문장2
#
# -> 문장1을 시도해보고, {발생오류}가 발생하면 문장2를 실행한다.
#

try:
    print(1/0)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")  # 0으로 나눌 수 없습니다



print("-------------------------------------------------")

# 특정 오류의 회피
#
# try:
#       문장1
# except {발생오류} as {오류변수}:
#       문장2
#
# -> 문장1을 시도해보고, {발생오류}가 발생하면 문장2를 실행하고,
#                           오류정보를 {오류변수}에 넣는다.
#

try:
    print(1/0)
except ZeroDivisionError as e:
    print(e)                        # division by zero


list=[]
try:
    print(list[0])
    print(1/0)
except ZeroDivisionError as e:
    print(e)                        
except IndexError as e:
    print(e)
                                    # list index out of range 만 출력된다!!                
                    
print("-------------------------------------------------")

# 예외 처리 - try, except, else
#
# try:
#       문장1
# except {발생오류} as {오류변수}:
#       문장2
# else:
#       문장3
#
# -> 1. 문장1을 시도해본다.
#    2. {발생오류} 발생시 {오류변수}에 오류의 내용을 넣는다.
#    3. 예외가 발생하지 않았을 경우, 문장3을 실행한다.
#


try:
    f = open("notexists.txt", "r")
except FileNotFoundError as e:
    print(e)
else:
    data = f.read()
    f.close()
    print("파일 close")
                    # [Errno 2] No such file or directory: 'notexists.txt'

print("-------------------------------------------------")

# 예외 처리 - try ~ finally
#
# try:
#       문장1
# except {발생오류} as {오류변수}:
#       문장2
# finally:
#       문장3
#
# -> 1. 문장1을 시도해본다.
#    2. {발생오류} 발생시 {오류변수}에 오류의 내용을 넣는다.
#    3. 예외 발생 여부와 상관 없이 마지막에 항상 수행
#

try:
    f = open("notexists.txt", "r")
except FileNotFoundError as e:
    print(e)
finally:
    print("파일 close")
                    # [Errno 2] No such file or directory: 'notexists.txt'
                    # 파일 close

print("-------------------------------------------------")                    
