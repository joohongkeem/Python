# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180705","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")


def fib(n):                     # n 까지의 피보나치 수열을 출력하는 함수
    a,b = 0,1
    while b<n:
        print(b, end=' ')        # 줄바꿈 대심 공백으로 한줄에 출력
        a,b = b, a+b
    print("(끝)")                     # 줄 넘기기

def fib2(n):                    # n 까지의 피보나치 수열을 반환하는 함수
    result = []
    a,b = 0,1
    while b<n:
        result.append(b)        # 리스트 값 채우기
        a,b = b, a+b
    return result               # 피보나치 수 리스트 반환

print("fibo.py의 모듈 이름 " + __name__)     # fibo.py의 모듈 이름 __main__

if __name__ == "__main__":      # 외부에서 호출시
    import sys
    fib(int(sys.argv[1]))         # 첫 번째 외부 인자 값을 사용하여 fib 호출


# 도스창 띄워서 python fibo.py 50     -> 커맨드 라인 인자, 50이 argv[1]에 저장됨
#
# -------------------------------------------------
# # 20180705                   Made by joohongkeem#
# -------------------------------------------------
# fibo.py의 모듈 이름 __main__
# 1 1 2 3 5 8 13 21 34 (끝)

