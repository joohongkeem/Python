# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180704","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 연산자 재정의(Operator Overloading)
#
# - 연산자에 대해 클래스에 새로운 동작을 정의하는 것
# - 파이썬의 클래스는 새로운 데이터 형을 정의하는 것이므로
#   그에 상응하는 연산자의 재정의가 필요할 수 있다.
# - 연산자가 정의되어 있지 않으면 TypeError가 발생
# - 파이썬에서는 사용하는 거의 모든 연산에 대해 새롭게 정의할 수 있다.
#       > 수치 연산자 오버로딩
#       > 역이항 연산자 오버로딩
#       > 확장 산술 연산자 오버로딩
#       > 비교 연산자 오버로딩
#

print("-------------------------------------------------")

# 1. 수치 연산자 오버로딩
#
#   연산자         연산자 메서드
#     +             __add__
#     -             __sub__
#     *             __mul__
#     /             __truediv__
#     //            __floormod__
#     %             __mod__
#   divmod()        __divmod__
#   pow(),**        __pow__
#     <<            __lshift__
#     >>            __rshift__
#     &             __and__
#     ^             __xor__
#     |             __or__
#

class Mystring:
    def __init__(self,s):
        self.s = s
    def __add__(self,other):
        return self.s + other

print(Mystring("Life is too short, ")+ "You need Python!!!")
            # Life is too short, You need Python!!!

print("-------------------------------------------------")

# 2. 역이행 연산자 오버로딩
#
#   연산자         연산자 메서드
#     +             __radd__
#     -             __rsub__
#     *             __rmul__
#     //            __rfloormod__
#     %             __rmod__
#   divmod()        __rdivmod__
#   pow(),**        __rpow__
#     <<            __rlshift__
#     >>            __rrshift__
#     &             __rand__
#     ^             __rxor__
#     |             __ror__
#

class Mystring:
    def __init__(self,s):
        self.s = s
    def __add__(self,other):
        return "(__add__호출)" + self.s + other
    def __radd__(self, other):
        return "(__radd__호출)" + other  + self.s
print(Mystring("Life is too short, ")+ "You need Python!!! ")
                # (__add__호출)Life is too short, You need Python!!!
print("Life is too short," + Mystring("You need Python!!!"))
                # (__radd__호출)Life is too short,You need Python!!!


print("-------------------------------------------------")

# 3. 확장 산술 연산자 오버로딩
#
#   연산자         연산자 메서드
#     +=             __iadd__
#     -=             __isub__
#     *=             __imul__
#     //=            __ifloormod__
#     /=             __idiv__
#     %=             __imod__
#     **=            __ipow__
#     <<=            __ilshift__
#     >>=            __irshift__
#     &=             __iand__
#     ^=             __ixor__
#     |=             __ior__
#

# 4. 비교 연산자 오버로딩
#
#   연산자         연산자 메서드
#     <              __lt__
#     <=             __le__
#     >              __gt__
#     >=             __ge__
#     ==             __eq__
#     !=             __ne__
#