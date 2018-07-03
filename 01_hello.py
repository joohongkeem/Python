# File - New File - Writing... - run module(Hot key : F5)
print("#20180702","Made by joohongkeem",sep=' ',end='#\n')
print("--------------------------------------")

print("Hello Python")

print("--------------------------------------")

a="Hello"
print("a="+a)
print("a*3="+a*3)

print("--------------------------------------")

a=5
b=2
print("a =",a,",b =",b)
print("a + b ="+str(a+b))
print("a - b ="+str(a-b))
print("a * b ="+str(a*b))
print("a / b ="+str(a/b))
print("a % b =",(a%b))
print("a // b =",(a//b))
print("a ** b =",(a**b))

print("--------------------------------------")

var1 = "aaa"
var2 = "aaa"
print("var1="+var1,"var2="+var2)
print("var1==var2 ->",var1==var2)
print("var1 is var2 ->",var1 is var2)
print("var1 is not var2 ->",var1 is not var2)
print("id(var1)=",id(var1),"id(var2)=",id(var2))

print("--------------------------------------")

a=3
print("a="+str(a))
if(a>0):					#Identation !! (recommend : space 4 times)
	print("Positive Num")
elif(a==0):
	print("Zero Num")
else:
	print("Negative Num")
	
print("--------------------------------------")

type(2+3j) # <class 'complex'>
var1=1+3j
var2=var1.conjugate()
print("var1=",var1,"var2=",var2)
print("var1*var2=",var1*var2)

print("--------------------------------------")

int(3.5)      # 3
2e3           # 2000.0
float("1.6")  # 1.6
float("inf")  # inf
float("-inf") # -inf
bool(0)       # False. 숫자에서 0만 False임,
bool(-1)      # True
bool("False") # True
a = None      # a는 None
a is None     # a가 None 이므로 True 

print("--------------------------------------")



