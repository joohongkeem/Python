# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180703","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

#1. 구구단의 1단만 출력

i=1
while i<10:
    print("1 x {0} = {0}".format(i))
    i+=1

print("-------------------------------------------------")

#2. 구구단 중 원하는 단수 입력 받아 해당 단을 출력

N = (int)(input("원하는 단수 : "))
i=1
while i<10:
    print("{0} x {1} = {2}".format(N,i,N*i))
    i+=1
    
print("-------------------------------------------------")

#3. 구구단 전체 출력

N = 1
while N<10:
    i = 1
    print("   %d 단"%N)
    while i<10:
        print("{0} x {1} = {2}".format(N,i,N*i))
        i+=1
    N+=1
    
print("-------------------------------------------------")

#4. 입력 받은 문자열(영문)의 대소문자 변경

str1 = input("영문자열 입력 : ")
print("( 모두 대문자 ) : %s"%str1.upper())
print("( 모두 소문자 ) : %s"%str1.lower())
print("(대소문자 반전) : %s"%str1.swapcase())

print("-------------------------------------------------")

#5. 입력 받은 문자열 순서 뒤집기

str2 = input("문자열 입력 : ")
print("( 순서 반전 ) : %s"%str2[::-1])   

print("-------------------------------------------------")

#6. 도서목록 만들기

print("\n                              [책 목록]")
print("   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("   |       제목      |  출판년도   |  출판사   |  페이지 수 |  추천여부 |")
print("   |ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("   | Python          |   2010      |   비트    |     510    |    T      |")
print("   | Machine Learning|   2014      |   한국    |     380    |    T      |")
print("   | Java            |   2010      |   비트    |     400    |    F      |")
print("   | Deep Learning   |   2015      |   한국    |     600    |    T      |")
print("   | IOT             |   1999      |   한국    |     550    |    T      |")
print("   ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("")
print("")


#6-1. 책목록 만들기 (list, dict 사용)
#
    
BookList = [ ("Python",2010,"비트",510,True),
             ("Machine Learning", 2014, "한국", 380, True),
             ("Java", 2010, "비트", 400, False),
             ("Deep Learning", 2015, "한국", 600, True),
             ("IOT", 1999, "한국", 550, True)]


KEYS = ("제목","출판년도","출판사","페이지 수", "추천여부")
BookDict = list()
i = 0
while i<5:
    BookDict.append(dict(zip(KEYS,BookList[i])))                # Dict들로 이루어진 List 생성
    i+=1


#6-2. 페이지 수가 500이상인 책 제목 리스트 출력
#

List_500pages = list()
i=0
while i<5:
    if(BookDict[i].get("페이지 수") >= 500):
        List_500pages.append(BookDict[i].get("제목"))
    i+=1

print("  1. 500페이지 이상인 책 리스트 :", List_500pages, end='\n\n')


#6-3. 추천 도서 출력
#

List_Recommend = list()             
for i in BookDict:                      # ★이런식으로 표현해도 잘 된다★
    if(i.get("추천여부") == True):
        List_Recommend.append(i.get("제목"))
    
        
print("  2. 추천도서 리스트 :", List_Recommend, end='\n\n')

#6-4. 총 페이지 수 출력
#

total = 0
i=0
while i<5:
    total += BookDict[i].get("페이지 수")
    i+=1

print("  3. 총 페이지 수 :",total, end='\n\n')


#6-5. 출판사 목록 출력
#

Set_Maker = set()
for i in BookDict:
    Set_Maker.add((i.get("출판사")))

print("  4. 출판사 목록 :",list(Set_Maker), end='\n\n')

print("-------------------------------------------------")
