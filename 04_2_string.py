# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180703","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 문자열

s = " "
str1 = "Hello World"
str2 = "Life is too short, you need Python"
print(type(s),type(str1),type(str2))
print(str1+s+str2)


# 여러줄의 문자열 정의는 """ ~~~ """ 또는 ''' ~~~ ''' 를 활용하자
str3 = """ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
1234567890
가나다라마바사아자차카타파하"""
print(str3)

print("-------------------------------------------------")

# 문자열의 연산 - 연결과 반복
first_name = "JooHong"
last_name = "Kim"
full_name = first_name+" "+last_name
print(full_name)
print(first_name,last_name)

laugh = "Ha"
print(laugh*20)

#print("Python" + 3)    # 에러발생 - 문자열 객체와 수치형 객체는 + 연산 불가능
print("Python"+str(3))


print("-------------------------------------------------")

# 문자열의 연산 - 인덱싱, 슬라이싱, len

# 참고
arr="a개똥아"
print(arr[0])   # a
print(arr[1])   # 개
print(arr[2])   # 똥
print(arr[3])   # 아
#print(arr[4])  # 에러

str = "Life is too short, You need Python!!"

print(len(str))     # len() : 시퀀스형의 길이를 반환

print(str[2])       # 2번째 문자 출력 "f"
print(str[8:11])    # 8~11 출력 "too"
print(str[-8:-1])   # -8~-1 출력 "Python!"
print(str[-8:])     # -8~0 출력 "Python!!"
print(str[5:])      # is too short ~~~~ 출력

#str[0] = "1" # 에러발생 - 문자열은 변경 불가(immutable) 자료형이다

print("-------------------------------------------------")

# 문자열 메서드 - 대소문자

s = "i like Smoking"
print(s)
print(s.upper())        # 문자열을 대문자로 변환
print(s.lower())        # 문자열을 소문자로 변환
print(s.swapcase())     # 대문자 <-> 소문자 전환
print(s.capitalize())   # 문자열의 첫글자를 대문자로 변환
print(s.title())        # 각 단어의 첫글자를 대문자로 변환


print("-------------------------------------------------")


# 문자열 메서드 - 검색 관련

s = "I Like Python. I Like C Also, But I don't Like JAVA"

print(s)

print(s.count('Like'))      # 문자열 내 검색어 개수를 반환 -> 3

print(s.find('Like'))       # 문자열 내 첫번째 검색된 위치의 인덱스를 반환 -> 2
print(s.find('Like',5))     # 인덱스 5부터 검색 -> 17
print(s.find('JS'))         # 문자열 내 검색어가 존재하지 않을경우 '-1' -> -1
print(s.rfind('Like'))      # 우측부터 검색하여 문자열 내 첫번째 검색어의 인덱스 반환 -> 42

#print(s.index('JS'))       # 문자열 내 검색된 위치의 인덱스를 반환
                            # find와의 가장 큰 차이는, 문자열 안에 검색어가 없다면 오류가 발생
print(s.index('Like'))      # 문자열 내에 검색어가 있다면 find함수와 같다.
print(s.rindex('Like'))     # 문자열 내에 검색어가 있따면 rfind함수와 같다.

print(s.startswith('I Like'))   # 문자열이 지정된 검색어로 시작하는지 여부 반환
print(s.startswith('Python'))   # 문자열이 지정된 검색어로 시작하는지 여부 반환
print(s.startswith('Like',2))   # 인덱스 2에서, 문자열이 지정된 검색어로 시작하는지 여부 반환
print(s.startswith('Python',2)) # 인덱스 2에서, 문자열이 지정된 검색어로 시작하는지 여부 반환

print(s.endswith('JAVA'))           # 문자열이 지정된 검색어로 끝나는지 여부 반환
print(s.endswith('JAVA',5))         # 인덱스 5부터 끝까지 endswith함수를 적
print(s.endswith('Python',0,13))    # 인덱스 0부터 13까지 endswith함수를 적용


print("-------------------------------------------------")

# 문자열 메서드 - 편집, 치환 관련

s = ' Spam and Ham '
print(s)
print(s.strip())            # 문자열 내 좌우의 공백문자 제거
print(s.lstrip())           # 문자열 내 좌측의 공백문자 제거
print(s.rstrip())           # 문자열 내 우측의 공백문자 제거


s = '<><abc><><defg><><>'
print(s)
print(s.strip('<>'))        # 문자열 내 좌우의 '<>'문자 제거
                            # 출력결과 : abc><><defg
                            # <><와 ><>가 제거된다

s = 'Hello Java'
print(s.replace('Hello','Fuckin'))  # 문자열 내 지정된 검색어를 다른 문자열로 치환

print("-------------------------------------------------")

# 문자열 메서드 - 정렬 관련

s= 'Alice and the Heart Queen'

print(s.center(40))         # 30칸 할당 후 중앙정렬
print(s.center(40,'@'))     # 40칸 할당 후 중앙정렬, 빈칸은 @로 채움
print(s.ljust(40,'@'))      # 40칸 할당 후 좌측정렬, 빈칸은 @로 채움
print(s.rjust(40,'@'))      # 40칸 할당 후 우측정렬, 빈칸은 @로 채움

print('20'.zfill(10))       # 자리수를 지정하고 빈 공간을 0으로 채움
print('1234'.zfill(10))     # 이 때, .zfill(숫자) 임을 기억하자 (, X)

print("-------------------------------------------------")

# 문자열 메서드 - 분리, 결합 관련

s= 'spam and ham'

t = s.split();          # 문자열을 공백문자(혹은 지정된 문자)를 기준으로 분리
print(t)                # 분리된 값은 리스트 형태로 들어간다.
t = s.split(' and ')    # ' and ' 문자 기준으로 spam, ham 이 분리된다.
print(t)

s2 = " ".join(t)        # List에 있는 문자열을 지정된 기호로 합침    
print(s2)               # ""부분이 없으면 에러
s2 = ":".join(t)
print(s2)

s3 = ["one","two","three","four","five"]
s3 = ":".join(s3)
print(s3)
print(s3.split(':',2))  # 문자열을 ':' 기준으로 2개만 분리
                        # 2개는 각각의 리스트로, 나머지는 하나의 리스트로
                        # -> 총 3개의 list
                        # ['one', 'two', 'three:four:five']
                        
print(s3.rsplit(':',2)) # 문자열을 ':' 기준으로 우측부터 2개만 분리
                        # ['one:two:three', 'four', 'five']

s4 = """1st line
2nd line
3rd line
4th line
"""
print(s4.splitlines()); # 문자열을 개행문자를 기준으로 분리
                        #['1st line', '2nd line', '3rd line', '4th line']

print("-------------------------------------------------")

# 문자열 메서드 - 판별 관련

print('1234'.isdigit()) # 문자열이 숫자로 구성되어 있는지 여부 반환
print('abcd'.isdigit())

print('1234'.isalpha()) # 문자열이 알파벳으로 구성되어 있는지 여부 반환
print('abcd'.isalpha())

print('abcd'.islower()) # 문자열이 소문자로 구성되어 있는지 여부 반환
print('ABCD'.islower())

print('abcd'.isupper()) # 문자열이 대문자로 구성되어 있는지 여부 반환
print('ABCD'.isupper())

print('\n\n'.isspace()) # 문자열이 공백문자로 구성되어 있는지 여부 반환
print(' '.isspace())    # [주의] 개행문자는 공백문자로 취급한다 !!!!!
print(''.isspace())         # False
print('\n\n \n'.isspace())  # True

print("-------------------------------------------------")

# 문자열 메서드 - 서식 메서드_ 문자열 포맷 코드

    # %s : 문자열(string)
    # %c : 문자 1개(character)
    # %d : 정수(integer)
    # %f : 부동 소수(floating point)
    # %o : 8진수
    # %x : 16진수
    # %% : Literal %
    #
    # 서식 메서드에 출력 포멧을 추가 지정하는 것도 가능
    # ex) %2.4f -> 정수부 2자리, 소수부 4자리

print("I have %d apples" % 20)
print("Interest rate is %f" %1.24)
print("Interest rate is %2.4f" %1.24)

print("-------------------------------------------------")

# 문자열 메서드 - 고급 문자열 포매팅_ .format() 메서드

    # 문자열의 format 메서드를 이용하면 좀 더 편리한 방식으로 문자열 포맷을 지정할 수 있다.
    # format_map 메서드를 이용하면 이름 기반으로 map의 데이터 형식을 이용 포맷으로 지정할 수 있다.

    # 형식이 매우 복잡하므로 잘 기억하도록 !!
    
print("I have {} apples, and I ate {} apples.".format(5, 3))
print("I have {total} apples, and I ate {num} apples.".format(num=3,total=5))
print("I have {total} apples, and I ate {num} apples.".format_map({"total":5, "num":3}))

print("-------------------------------------------------")
