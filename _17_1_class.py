# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180704","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")


# 파이썬 클래스
#
# - 새로운 이름 공간을 지원하는 단위 : 데이터의 설계도
# - 데이터와 데이터를 변경하는 함수(메서드) 를 같은 공간 내에 작성
# - 클래스를 정의하는 것은 새로운 자료형을 정의하는것이고,
#   인스턴스는 이 자료형의 객체를 생성하는 것이다.
# - 클래스와 인스턴스는 각자의 이름공간을 가지게 되며, 유기적인 관계로 연결된다.
#
#       클래스 용어 정리
#       - 클래스 : class 문으로 정의하며, 멤버와 메서드를 가지는 객체
#       - 클래스 객체 : 어떤 클래스를 구체적으로 가리킬 때 사용
#       - 인스턴스 : 클래스를 호출하여 만들어지는 객체
#       - 인스턴스 객체 : 인스턴스화 된 객체
#       - 멤버 : 클래스가 갖는 변수
#       - 메서드 : 클래스 내에 정의된 함수
#       - 속성 : 멤버 + 메서드
#       - 상위 클래스 : 기반 클래스. 어떤 클래스의 상위에  있으며 여러 속성을 상속해준다
#       - 하위 클래스 : 파생 클래스. 상위 클래스로부터 여러 속성을 상속 받는다.
#
#       클래스 이용의 장점
#       - 프로그램의 규모가 커졌을 때 의미 있는 집합체 단위로 프로그램을 정리할 수 있다.
#       - 설계도(Class)가 있으므로 인스턴스를 양산할 수 있다.
#

var = '파이썬 프로그래밍'
print(id(var))      # 2122710987304
print(type(var))    # <class 'str'>
str
print(type(str))    # <class 'type'>   -> str 클래스는 type 클래스의 객체
print(type(type))   # <class 'type'>   -> type도 type 클래스의 객체
print(id(str))      # 140703182196816

print(var.__class__)    # <class 'str'>     -> var 객체의 지역변수 __class__

print(var)                                  # 파이썬 프로그래밍
print(var.replace('파이썬','Python'))     # Python 프로그래밍
print(var)                                  # 파이썬 프로그래밍


print("-------------------------------------------------")



# this 포인터
# - 클래스 내부에 자동 선언되는 클래스 포인터
# - 선언된 객체의 주소를 저장하고 있다.
# - 클래스 내부에서만 사용할 수 있다.
#       > static 멤버함수 내부에선 사용 불가능
# - 상수 포인터이다 (임의 변경 불가능)
#
# ★C++의 'this'가 Python에서는 'self'★
#

class BusinessCard:
    def set_info(self, name, email, addr):      # BusinessCard 클래스에 set_info라는 메서드를 추가
                                                # 클래스 내부의 메서드의 첫번째 인자는 반드시 self여야 한다!!
        self.name = name
        self.email = email                      # 메서드 인자로 전달된 name, email, addr 값을
        self.addr = addr                        # self.name, self.email, self.addr 이라는 변수에 대입 ! (바인딩!)

member1 = BusinessCard()                        # 새롭게 정의된 클래스로 인스턴스를 생성
                                                # 붕어빵 틀을 만들었으므로, 붕어빵을 구워보는 것!
print(member1)                                  # <__main__.BusinessCard object at 0x00000224D0639208>
member1.set_info("김주홍","joohongkeem@naver.com","Gunpo")
                                                # member1을 통해 self.name, self.email, self.addr로 접근했다.
                                                # 'self.변수명' 의 변수를 '인스턴스 변수'라고 한다.
                                                # 인스턴스 변수는 클래스 인스턴스 내부의 변수를 의미한다
                                                # 위의 코드는 member1이라는 인스턴스를 생성한 후
                                                # set_info 메서드를 호출하며 값을 바인딩한 것!
                                                # 클래스를 정의하는 순간에는 인스턴스의 이름을 모르므로
                                                # self라는 단어를 사용하여 대신 사용하는 것!
print(member1.name, member1.email, member1.addr)    # 김주홍 joohongkeem@naver.com Gunpo

print("-------------------------------------------------")

# 클래스의 생성과 메서드의 정의

class Point:
    def set_x(self,x):
        self.x=x
    def get_x(self):
        return self.x
    def set_y(self,y):
        self.y = y
    def get_y(self):
        return self.y

# 인스턴스 객체 생성과 메서드 호출
# (방법1)Bound Instance Method 호출
#
def main():
    bound_class_method()

def bound_class_method():
    p = Point()             # Point 인스턴스 생성
    p.set_x(10)
    p.set_y(20)
    print(p.get_x(), p.get_y(), sep = ',')


if __name__ == '__main__':
    main()                      # 10,20

# (방법2)Unbound Instance Methond 호출
#
def main():
    unbound_class_method()

def unbound_class_method():
    p = Point()             # Point 인스턴스 생성
    Point.set_x(p,10)       # 객체를 첫 번째 인자에 할당하고 있음에 유의
    Point.set_y(p,20)       # 객체를 첫 번째 인자에 할당하고 있음에 유의
    print(Point.get_x(p), Point.get_y(p), sep = ',')


if __name__ == '__main__':
    main()                      # 10,20


print("-------------------------------------------------")

# 정적 메서드(static method)와 클래스 메서드(class method)
#
# 정적메소드라 함은 클래스에서 직접 접근할 수 있는 메소드입니다.
# 파이썬에서는 클래스에서 직접 접근할 수 있는 메소드가 두가지가 있습니다.staticmethod와 classmethod 입니다.
# 하지만 파이썬에서는 다른언어와는 다르게 정적메소드임에도 불구하고 인스턴스에서도 접근이 가능합니다. 이 차이에 유의해야합니다.
# 에디터에서 static_method.py파일을 작성합니다.
# 인스턴스 메소드는 첫번째 인자로 객체 자신 self자신을 입력합니다.
# classmethod는 첫번째 인자로 클래스를 입력합니다.
# staticmethod는 특별히 추가되는 인자가 없습니다.

class CustomClass:

    # instance method
    def add_instance_method(self, a, b):
        return a + b

    # classmethod
    @classmethod
    def add_class_method(cls, a, b):
        return a + b

    # staticmethod
    @staticmethod
    def add_static_method(a, b):
        return a + b

# 인스턴스 메소드를 클래스에서 바로 접근해보자.
print(CustomClass.add_instance_method(None,3,5))        # 8

# 클래스 메소드를 클래스에서 바로 접근해보자.
# print(CustomClass.add_instance_method(CustomClass, 3, 5))     # 에러 (첫번째 인자 생략해야함)
print(CustomClass.add_class_method(3,5))

# 스태틱 메소드를 클래스에서 바로 접근해보자.
print(CustomClass.add_static_method(3,5))

# 클래스 메소드와 스태틱 메소드는 객체에서 접근이 가능하다★
a = CustomClass
print(a.add_class_method(3,5))
print(a.add_static_method(3,5))

# 스태틱 메소드와 클래식 메소드의 차이점?
#         >> '상속'에서 차이가 두드러진다
#
# - 스태틱 메소드에서는 부모클래스의 속성 값을 가져오지만
#   클래스 메소드에서는 cls인자를 활용하여 cls의 클래스속성을 가져온다.
#
class Language:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language):
    default_language = "한국어"

a = KoreanLanguage.static_my_language()
b = KoreanLanguage.class_my_language()

a.print_language()      # 나의 언어는English
b.print_language()      # 나의 언어는한국어

print("-------------------------------------------------")

# __str__ 메서드 : 객체를 문자열로 반환하는 함수
# __repr__ 메서드 : __str__과 비슷하지만 "문자열로 객체를 다시 생성할 수 있기 위해" 사용
#                   >> Eval을 수행하면 다시 그 해당 객체가 생성될 수 있어야 한다.

class Point:
    def set_x(self,x):
        self.x=x
    def get_x(self):
        return self.x
    def set_y(self,y):
        self.y = y
    def get_y(self):
        return self.y
    def __str__(self):
        return "Point = ({0},{1})".format(self.x,self.y)
    def __repr__(self):
        return "\"Point=({0}, {1})\"".format(self.x, self.y)

p = Point()
p.set_x(1)
p.set_y(2)
print(p)               # Point = (1,2)
print(repr(p))         # "Point=(1, 2)"
p2 = eval(repr(p))
print(p2)              # Point=(1, 2)

# __str__
#   > 구분 : 비공식적 문자열 출력
#   > 목적 : 사용자가 보기 쉽게
#   > 대상 : 사용자(End User)
#
# __repr__
#   > 구분 : 공식적 문자열 출력
#   > 목적 : 문자열로 객체를 다시 생성할 수 있도록
#   > 대상 : 개발자(Developer)

print("-------------------------------------------------")
# 클래스 설계
#
# 자바에서는
# class Employee {
#       private int no;
#       private String name;
#       private String department;
#
#       public Employee(int no, String name, String department){
#               this.no = no;
#               this.name = name;
#               this.department = department;
# }
# Emplyee e = new Employee(001,"joohongkeem", "R&D");


class Card1:
    def set_info(self,name,email,addr):
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):
        print("Name:",self.name)
        print("E-mail:",self.email)
        print("Addr:",self.addr)

member1 = Card1()
member1.set_info("Joohongkeem","joohongkeem@naver.com","Gunpo")
member1.print_info()
                        # Name: Joohongkeem
                        # E-mail: joohongkeem@naver.com
                        # Addr: Gunpo

print("-------------------------------------------------")

# 클래스 생성자
#
# >> 어떻게 하면 클래스 인스턴스 생성과 초깃값 입력을 한번에 할 수 있을까?
# >> __init__(self) 를 이용하자!
#

class MyClass:
    def __init__(self):
        print("객체 생성")                      # 객체 생성

c1 = MyClass()


class Card2:
    def __init__(self,name,email,addr):
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):
        print("Name:",self.name)
        print("E-mail:",self.email)
        print("Addr:",self.addr)

# man1 = Card2()            # 3개의 인자를 전달하지 않으면 오류 발생!
man1 = Card2("김주홍","메일 없음","군포")
man1.print_info()
                        # Name: 김주홍
                        # E-mail: 메일 없음
                        # Addr: 군포
print("-------------------------------------------------")

# 네임 스페이스
#
# - 변수가 객체를 바인딩할 때, 그 둘 사이의 관계를 저장하고 있는 공간
#   예를 들어, a = 2 라고 하면,
#   a라는 변수가 2라는 객체가 저장된 주소를 갖고 있는데
#   이러한 관계가 저장된 공간이 바로 네임스페이스!
# - 클래스가 정의되면, 하나의 독릭접인 네임스페이스가 생성된다.
#   그리고 클래스 내에 정의된 변수나 메서드는 해당 네임스페이스 안에
#   파이썬 딕셔너리 타입으로 저장이 된다.
# - 인스턴스를 통해 변수에 접근하려고 시도하면,
#   먼저 인스턴스의 네임스페이스에서 검색해보고, 해당 되는 변수가 없다면
#   인스턴스의 클래스의 네임스페이스에서 검색하게 된다. (그 때도 없으면 Error)
#

print("-------------------------------------------------")

# 클래스 변수와 인스턴스 변수
#
class Account:
    num_accounts = 0

    def __init__(self, name):           # __init__ (생성자) : 인스턴스 생성시 자동 호출
        self.name = name
        Account.num_accounts += 1

    def __del__(self):                  # __del__(소멸자) : 인스턴스 소멸시 자동 호출
        Account.num_accounts -= 1

Kim = Account("Kim")        # Kim 인스턴스 생성
Lee = Account("Lee")        # Lee 인스턴스 생성

print(Kim.num_accounts)      # 2
print(Lee.num_accounts)      # 2
        # 먼저 인스턴스내의 네임스페이스에서 num_accounts를 찾았지만 해당 이름이 없으므로
        # 클래스의 네임스페이스로 이동한 후 다시 그 이름을 찾은 것!
        #
        # 여러 인스턴스 간에 서로 공유해야 하는 값은 클래스 변수를 통해 바인딩해야 한다!
print(Account.num_accounts)     # 이렇게 클래스 변수에 접근할 수도 있다!

# 즉, 클래스 변수는 여러 인스턴스가 공유하는 'num_accounts'이고,
# 인스턴스 변수는 여러 인스턴스가 각각 갖고 있는 'name'이다

print("-------------------------------------------------")

# Information Hiding, Name Mangling : 접근 제한자

# 일반적으로 선언한 클래스 변수엔 이렇게 접근이 가능하다.
#       public : 변수             -> 객체 외부에서 접근 가능
#       private : __변수          -> 객체 외부, 상속받은 객체도 접근 불가능
#       protected : _변수         -> 객체 외부에서 접근 불가능

class BookReader:
    country = 'South Korea'

print(BookReader.country)            # South Korea
BookReader.country = 'USA'
print(BookReader.country)            # USA


# 접근 제한을 주고 선언한 클래스 변수엔 이러한 접근이 불가능하다.
#
class BookReader1:
    __country = 'South Korea'          # 접근 제한(private)

# print(BookReader1.__country)             # AttributeError: type object 'BookReader' has no attribute 'country'
A = BookReader1()
#print(A.__country)                         # AttributeError: 'BookReader1' object has no attribute '__country'

BookReader1.__country = 'USA'
print(BookReader1.__country)             # USA       -> 왜 요고는 잘 나오지!?!?!
print(A.__country)                       # USA       -> 요것도 잘 나오넹.....
                                         # 여기선 잘 되지만, shell에선 에러 발생
                                         # 파이썬의 클래스는 절대적인 private, protected를 지원하지 않는다!

# 접근 제한을 준 클래스 변수엔, 함수를 통해 접근한다!
#

class BookReader:
    __country = 'South Korea'
    def set_country(self, country):     # Setter
        self.__country = country
    def get_country(self):              # Getter
        return self.__country

br = BookReader()
print(br.get_country())                 # South Korea
br.set_country('USA')
print(br.get_country())                 # USA

print("-------------------------------------------------")

# 상속
#
# - 다른 클래스에서 이미 구현된 메서드나 속성을, 상속한 클래스에서는 그대로 사용 가능
#

class Parent:
    def can_sing(self):
        print("Sing a Song")

father = Parent()
father.can_sing()               # Sing a Song

class LuckyChild(Parent):      # 새로 정의할 클래스 이름 다음에 괄호를 사용한 후
    pass                       # 그 괄호 안에 상속받고자 하는 클래스 이름을 지정

child1 = LuckyChild()
child1.can_sing()               # Sing a Song
                                # 상속받았기 때문에, can_sing() 함수가 없음에도 사용가능
class Human():
    country = 'South Korea'
    def __init__(self,name):                # name : 인스턴스 변수
        self.name = name
    def eat(self):                          # 상위 클래스인 Human에 새로운 메소드 추가
        print(self.name + ' is eating')

class BookWriter(Human):                    # Human 클래스 상속
    def write_book(self):
        print(self.name + 'is writing Book!')

bw = BookWriter("Joohongkeem")
bw.write_book()
bw.eat()

print(bw.__class__)         # <class '__main__.BookWriter'> : bw의 클래스는 BookWriter
print(BookWriter.__class__) # <class 'type'>
print(BookWriter.__bases__) # (<class '__main__.Human'>,) : BookWriter 클래스의 부모클래스는 Human 클래스
print(Human.__class__)      # <class 'type'>
print(Human.__bases__)      # (<class 'object'>,) : Human클래스의 부모 클래스는 object! (최상위)


# 다중 상속
#

class Developer:
    def coding(self):
        print(self.name + 'is developer')

class ProgramBookWriter(Human, Developer):              # 다중 상속
    def write_book(self):
        print(self.name + 'is writing Program Book')

pwb = ProgramBookWriter("Joohongkeem")
pwb.eat()
pwb.coding()                # 상속받은 coding함수와 eat함수를 모두 사용할 수 있다.
pwb.write_book()
#pwb.__bases__              # 이건 안된다 ! __bases__ 는 인스턴스가 아닌 클래스 뒤에 사용
print(ProgramBookWriter.__bases__)      # (<class '__main__.Human'>, <class '__main__.Developer'>)

print("-------------------------------------------------")

# 다형성
#
# - 부모 클래스로부터 물려받은 가상 함수를 자식 클래스 내에서 오버라이딩 하여 사용하는것
#   (오버라이딩 - 부모클래스와 같은 이름을 가진 메소드를 덮어쓰기 한다)
#       > 동일한 코드이지만, 동작방법과 결과가 다른 것을 의미한다.
#       > 다형성의 쉬운 예제는 '오버로딩'이다
#

class Developer:
    def __init__(self,name):
        self.name = name
    def coding(self):
        print(self.name + ' is developer')

class PythonDeveloper(Developer):
    #def __init__(self,name):
    #    self.name = name
    #def coding(self):
    #    print(self.name + ' is Python developer')
    pass
class JavaDeveloper(Developer):
    def __init__(self,name):
        self.name = name
    def coding(self):
        print(self.name + ' is Java developer')

class CppDeveloper(Developer):
    def __init__(self,name):
        self.name = name
    def coding(self):
        print(self.name + ' is Cpp developer')

pd = PythonDeveloper('joohongkeem')
jd = JavaDeveloper("heoseunghoi")
cd = CppDeveloper("moontaeseung")
pd.coding()             # joohongkeem is developer
jd.coding()             # heoseunghoi is Java developer
cd.coding()             # moontaeseung is Cpp developer


class CppDeveloper(Developer):
    def coding(self):
        super().coding()                              # 부모 클래스에 있는 함수 호출 ★super()★
        print(self.name + ' is Cpp develover')
cd = CppDeveloper("moontaeseung")
cd.coding()             # moontaeseung is developer
                        # moontaeseung is Cpp develover
                        # 부모 클래스 메소드 출력 결과, 자식 클레스 메소드 출력 결과가 함께 출력된다!!



print("-------------------------------------------------")


print("-------------------------------------------------")

# self 이해하기     https://wikidocs.net/1742 보고 더 적어보기

# - 메서드의 첫번째 인자가 항상 self여야 한다는 말은 사실 틀리다!
class Foo:
    def func1():
        print("function 1")

    def func2(self):
        print("function 2")
f = Foo()
f.func2()                       # function 2 출력
#f.func1()                      # 에러발생
                                # 에러내용 : func1()은 인자가 없지만 하나를 받았다
                                # 즉, 메서드의 첫 번째 인자로 항상 인스턴스가 전달된다.
