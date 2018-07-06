print("-------------------------------------------------")
print("# 20180706", "Made by joohongkeem#".rjust(38), sep=' ', end='\n')
print("-------------------------------------------------")

# 입출력

print('Hello!~')
print('Hello!~', 'pmk')

print('Hello, {}!'.format('pmk'))

name = input('이름 입력: ')
print('Hello, {}!'.format(name))

name = input('이릅 입력: ')
job = input('직업 입력: ')
print('{}의 직업은 {}'.format(name, job))

print('{0}의 직업은 {1}'.format(name, job))  # {} 내에 인덱스 표기 가능
print('훌륭한 {1}, {0}.'.format(name, job))  # 인덱스로 출력 순서 지정
print('Good {j}, {n}.'.format(n=name, j=job))  # 변수명 사용
print('{0}은 {lang} {1}.'.format(name, job, lang='Python'))  # 인덱스와 변수명 함께 사용

# 여러가지 포맷

print('{0} - {1} - {2}'.format(*'ABC'))  # 튜플, 리스트형 데이터를 자동 언팩킹하여 출력
print('{0} - {1} - {2}'.format(*['A', 'B', 'C']))
print('{0[0]} - {0[1]} - {0[2]}'.format(['A', 'B', 'C']))  # 리스트형
print('{0[name]} - {0[last_name]}'.format({'name': 'pmk', 'last_name': 'paek'}))  # dict형 format(argv)

print('{:<20}'.format('좌측 정렬'))  # 정렬
print('{:>20}'.format('우측 정렬'))
print('{:^20}'.format('중앙 정렬'))

import math

print('원주율은 대략 {:f} 입니다.'.format(math.pi))
print('원주율은 대략 {:.2f} 입니다.'.format(math.pi))

print('{:+f}; {:+f}'.format(3.14, -3.14))  # 양수, 음수 기호 반드시 출력
print('{: f}; {: f}'.format(3.14, -3.14))  # 기호는 공백, 음수 기호만 출력
print('{:-f}; {:-f}'.format(3.14, -3.14))  # 기호는 공백, 음수 기호만 출력

print('{:,}'.format(100000000)) # 천단위 구분자
print('{:%}'.format(5/12)) # 백분율
print('{:.2%}'.format(5/12)) # 백분율 자릿수 지정



