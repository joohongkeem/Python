# Run module(Hot key : F5)
print("#20180702","Made by joohongkeem",sep=' ',end='#\n')
print("--------------------------------------")

price = 120000
vat = 0.1           #부가가치세율
final_price = price + (price * vat)
print(final_price)

print("--------------------------------------")

# 변수 할당
a,b = 10,20         # a,b 뒤에 숫자 하나만 쓰면 에러발생
z=90
c=d=e=z
print(a,b,c,d,e)

print("--------------------------------------")

# Swap
a,b = 10, 20
print(a,b)
a,b = b,a
print(a,b)

a,b,c=10,20,30
print(a,b,c)
a,b,c=b,c,a
print(a,b,c)

print("--------------------------------------")

# 예약어
# python이 이미 사용하기로 지정해 둔 문자열

# (예약어의 종류를 확인하는법)
import keyword
print(keyword.kwlist)

# 주의사항 : False, True 의 가장 앞 글자가 대문자!
# >> false, true는 변수명으로 사용이 가능하다
true,false = 10,20
print(true,false)

print("--------------------------------------")

choice = input("Yes or No : ")
if(choice=='Yes'):
    print("You are 'Yes-Man'!!")
elif(choice=='No'):
    print("You are 'No-Man'!!")
else:
    print("You are Crazy!!")
