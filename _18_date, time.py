# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180705","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")


# 날짜와 시간
#
# - 날짜와 시간은 파이썬에서기본으로 제공하는 자료형에는 포함되어 있지 않지만 중요한 자료형
# - 날짜와 시간은 각각 date 객체와 time 객체를 이용하며,
#   이들 객체는 datetime 모듈에 포함되어 있기 때문에, 'import datetime'으로 불러와야 한다.
# - 주요 클래스
#       > datetime : 날짜와 시간을 모두 포함하는 클래스
#       > date : 날짜 관련 클래스
#       > time : 시간 관련 클래스
#

print("-------------------------------------------------")

# 날짜와 시간의 획득
#
# - datetime 모듈 내 datetime 클래스의 now() 메서드를 이용하면 현재 날짜와 시간을 얻을 수 있다.
# - datetime 클래스 생성자로 직접 날짜를 지정할 수 있다.
#       > 년, 월, 일, 시, 분, 초, 마이크로초 순으로 매개변수를 저장하게 되며,
#         최소 년월일은 지정해주어야 한다.
#

import datetime         # datetime 모듈 불러오기
dt1 = datetime.datetime.now()           # datetime모듈의 datetime클래스의 now() 메서드
print(dt1)                              # 2018-07-05 09:23:42.630815

dt2 = datetime.datetime(1992,12,8)
print(dt2)                              # 1992-12-08 00:00:00

print("-------------------------------------------------")

# datetime 클래스
#
# - 주요 속성
#       > year : 년
#       > month : 월
#       > day : 일
#       > hour : 시
#       > minute : 분
#       > second : 초
#       > microsecond : 마이크로초
#

print(dt1.year,dt1.month,dt1.day,dt1.hour,dt1.minute,dt1.second,dt1.microsecond)
                        # 2018 7 5 9 23 42 630815


# - 주요 메서드
#       > weekday() : 요일을 반환
#       > strftime() : datetime 을 문자형으로 포맷
#       > date() : 날짜 정보만 갖는 date 클래스로 변환
#       > time() : 시간 정보만 가지는 time 클래스로 변환
# (참고)
# - date는 datetime 클래스의 날짜 관련 속성과 요일 메서드를 이용 가능
# - time은 datetime 클래스의 시간 관련 속성 이용 가능
#

import datetime
dt = datetime.datetime.now()

print(dt.weekday())     # 월:0, 화:1, 수:2, 목:3, 금:4, 토:5, 일:6

print(dt.strftime("%Yyear %mmonth %dday"))  # 2018year 07month 05day
                                                # print(dt)는 그대로
                                                # %Y : 서기 년도 4자리
                                                # %y : 서기 년도 2자리 표시
                                                # %m : 2자리 월
                                                # %d : 2자리 일
                                                # %H : 시간 표시 (24시간)
                                                # %I : 시간 표시 (12시간)
                                                # %p : AM/PM 표시
                                                # %M : 2자리 분
                                                # %S : 2자리 초
                                                # %f : 6자리 마이크로초
                                                # %A : 영어로 요일을 표시
                                                # %a : 영어로 요일을 단축 표시
                                                # %B : 영어로 월을 표시
                                                # %b : 영어로 월을 단축 표시
print(dt.date())                # 2018-07-05
print(dt.time())                # 09:30:21.565845


# print(dt.strftime("%Y년 %m월 %d일"))
# - 이렇게 하면 Locale로 인해 UnicodeEncodeError 가 발생할 수 있다.
#   (★해결책★)
#   import locale
#   locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
#

import locale
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
print(dt.strftime("%Y년 %m월 %d일"))               # 2018년 07월 05일

print("-------------------------------------------------")

# datetime의 비교와 두 datetime의 차이 구하기
#
# - 두 개의 날짜는 대소 비교, 차이 값을 구할 수 있다.
# - 두 날짜의 차이는 datetime.timedelta 클래스로 반환, 날짜의 차이를 구할 수 있다.
#       > days, sconds, microseconds

import datetime
current = datetime.datetime.now()
past = datetime.datetime(1992, 12, 31)

print(current > past)                               # True

diff = current-past
print(diff)                                         # 9317 days, 9:33:53.291761
print(type(diff))                                   # <class 'datetime.timedelta'>3
print(diff.days, diff.seconds, diff.microseconds)   # 9317 34499 134494

# timedelta
#
# - timedelta 클래스의 주요 속성
#       > days : 일수
#       > seconds : 초 (0 ~ 863999)
#       > microseconds : 마이크로초(0 ~ 999999)
#
# - timedelta 클래스의 주요 메서드
#       > total_seconds() : 모든속성을 초단위로 모아서 반환
#
# - 두 datetime의 차이가 timedelta로 반환되었던 것과 반대로
#   datetime 클래스에 timedelta 값을 더해 새로운 날짜를 만들 수도 있다.
#

import datetime
current = datetime.datetime.now()
print(current)              # 2018-07-05 09:38:24.771412
diff = datetime.timedelta(days=30, seconds = 0, microseconds = 0)
print(current + diff)       # 2018-08-04 09:38:24.771412

print("-------------------------------------------------")

# 문자열을 datetime으로 변환
#
# - datetime 클래스의 strptime 메서드를 이용하면,
#   문자열로부터 날짜와 시간 저보를 읽어서 datetime 클래스로 변환할 수 있다.
#       > 첫 번째 인수 : 날짜와 시간 정보를 가진 문자열
#       > 두 번째 인수 : 문자열 해독을 위한 형식 문자열
#

import datetime
str = '2017시12월24일 23시59분'
print(datetime.datetime.strptime(str, '%Y시%m월%d일 %H시%M분'))
                    # 2017-12-24 23:59:00


print("-------------------------------------------------")