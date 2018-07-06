# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180706","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# - Database.db 파일에 IOTclass 테이블을 생성
# - my_class 테이블의 구조는 이름, 생년월일, 주소, 전화번호, 프로젝트명 으로 함
# - 14명의 레코드를 추가
# - IOT 반의 멤버 전원 목록을 출력
# - IOT 반의 프로젝트 개수 출력
# - 이름이 김주홍인 멤버의 정보를 출력
# - IOT 반에서 성이 "김"씨인 멤버만 출력
# - 허승회 멤버의 주소를 "서울시 강남구 역삼동" 으로 수정
# - 이무원씨는 취업을 하였으므로 정보를 제거하자
# - 영상처리 프로젝트를 수행하는 멤버를 출력하시오


import sqlite3  # SQLite3 탑재


# 테이블 생성용 함수
def create_table():
    conn = sqlite3.connect('database.db')  # 데이터베이스 커넥션 생성

    cur = conn.cursor()  # 커서 확보

    # IOTclasee 테이블 생성
    cur.execute('''CREATE TABLE IOTclass (
                        name text,
                        age integer,
                        birthday date,
                        bloodtype char[2],
                        address text,
                        phonenum text,
                        project text
                )'''
                )

    conn.commit()       # 데이터베이스 반영

    conn.close()        # 커넥션 닫기

def insert_lists():
    conn = sqlite3.connect('database.db')  # 데이터베이스 커넥션 생성
    cur = conn.cursor()  # 커서 확보

    # 데이터 입력
    cur.execute("INSERT INTO IOTclass VALUES ('김주홍', 27,'1992-12-08', 'B', '경기도 군포시', '01020049134', '영상처리')")

    # 데이터 입력 SQL
    insert_sql = 'INSERT INTO IOTclass VALUES (?, ?, ?, ?, ?, ?,?)'

    # 튜플을 이용한 데이터 입력
    cur.execute(insert_sql, ('허승회',28, '1991-11-06','B','경기도 안산시', '01032413923', '영상처리'))

    # 책의 정보를 담고 있는 튜플들의 리스트
    classmates = [
        ('김용석', 41, '1991-11-24', 'B', '경기도 안산시', '01074125896', '영상처리'),
        ('김용완', 38, '1989-03-02', 'O', '경기도 안양시', '01099998888', '드론'),
        ('김중근', 31, '1970-04-08', 'B', '서울특별시 도봉구', '01012345678', '영상처리'),
        ('김도환', 29, '1980-03-14', 'A', '대전광역시', '01021345678', '자율주행'),
        ('문태승', 30, '1965-04-18', 'B', '대구광역시', '01021456788', '드론'),
        ('박정효', 31, '1975-02-16', 'O', '경기도 군포시', '01054731578', '영상처리'),
        ('백경규', 28, '1989-02-07', 'AB', '경기도 수원시', '01097513487', '자율주행'),
        ('서재학', 28, '1992-12-31', 'A', '부산광역시', '01025876413', '드론'),
        ('오유준', 24, '1991-09-27', 'B', '경기도 포천시', '01024134578', '드론'),
        ('송은아', 27, '1997-09-24', 'A', '서울특벽시', '01098799997', '통신'),
        ('임지훈', 32, '1967-08-29', 'B', '경기도 의정부시', '01023487563', '자율주행'),
        ('정지윤', 31, '1985-07-24', 'O', '경기도 안양시', '01027998754', '영상처리'),
        ('한태승', 54, '1997-07-18', 'B', '경기도 군포시', '01024136877', '통신'),
        ('이무원', 34, '1968-09-12', 'AB', '부산광역시', '01032819324', '영상처리'),
        ('우준민', 19, '1954-11-01', 'B', '경기도 안산시', '01054723135', '통신'),
        ('유승훈', 29, '1997-12-08', 'AB', '서울특별시', '01054875687', '영상처리'),
    ]

    # 여러 데이터 입력
    cur.executemany(insert_sql, classmates)
    conn.commit()       # 데이터베이스 반영
    conn.close()        # 커넥션 닫기



# 아래 두개 함수는 처음에 한번만 호출, 이미 있으면 create안하고, insert 안하는 방법 찾아보기!!
#create_table()                  # 테이블 생성 함수 호출
#insert_lists()                  # 데이터 입력 함수 호출

conn = sqlite3.connect('database.db')                         # 데이터베이스 커넥션 생성
cur = conn.cursor()                                             # 커서 확보


print('[1] 전체 데이터 출력하기')
cur.execute('SELECT * FROM IOTclass')                       # 조회용 SQL 실행
classmates = cur.fetchall()  # 조회한 데이터 불러오기
for man in classmates:  # 데이터 출력하기
    print(man)

print('=============================================')

print('[2] 전체 프로젝트 종류 출력하기')
cur.execute('SELECT DISTINCT project FROM IOTclass ')    # 조회용 SQL 실행
projects = cur.fetchall()                                       # 조회한 데이터 불러오기
for project in projects:
    print(project[0])

print('=============================================')

print('[3] \'김주홍\'멤버 정보 출력')
cur.execute('SELECT * FROM IOTclass WHERE name = \'김주홍\'')
joohong = cur.fetchone()
print(joohong)

print('=============================================')

print('[4] 성이 \'김\'씨인 멤버 정보 출력')
cur.execute('SELECT name FROM IOTclass WHERE name like \'김%\'')
kim = cur.fetchall()
for member in kim:
    print(member[0])

print('=============================================')

print('[5] \'허승회\' 멤버의 주소를 \'서울시 강남구 역삼동\' 으로 수정')
print('수정 전')
cur.execute('SELECT * FROM IOTclass WHERE name is \'허승회\'')
hsh = cur.fetchone()
print(hsh)

cur.execute('UPDATE IOTclass set address = \'서울특별시 강남구\' WHERE name is \'허승회\'')

print('수정 후')
cur.execute('SELECT * FROM IOTclass WHERE name is \'허승회\'')
hsh = cur.fetchone()
print(hsh)

print('=============================================')

print('[6] 취업한 \'이무원\' 멤버의 정보를 제거')
cur.execute('DELETE FROM IOTclass WHERE name is \'이무원\'')
cur.execute('SELECT * FROM IOTclass')                       # 조회용 SQL 실행
classmates = cur.fetchall()  # 조회한 데이터 불러오기
for man in classmates:  # 데이터 출력하기
    print(man)

print('=============================================')
print('[7] 영상처리 프로젝트를 수행하는 멤버를 출력')
cur.execute('SELECT name FROM IOTclass WHERE project is \'영상처리\'')
videos=cur.fetchall()
for man in videos:
    print(man[0])

print('=============================================')
print('[8] 생년월일순으로 모든 멤버 출력')
cur.execute('SELECT * FROM IOTclass ORDER BY birthday')
mates = cur.fetchall()
for man in mates:
    print(man)

print('=============================================')
print('[9] 이름을 다나가순으로 모든 멤버 출력')
cur.execute('SELECT * FROM IOTclass ORDER BY name DESC')
mates = cur.fetchall()
for man in mates:
    print(man)

print('=============================================')
print('[10] 이름은 가나다순, 나이는 오름차순으로 모든 멤버 출력')
cur.execute('SELECT * FROM IOTclass ORDER BY age, name')
mates = cur.fetchall()
for man in mates:
    print(man)
print('=============================================')
conn.close()  # 커넥션 닫기