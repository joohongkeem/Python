print("-------------------------------------------------")
print("# 20180706", "Made by joohongkeem#".rjust(38), sep=' ', end='\n')
print("-------------------------------------------------")

import sqlite3          # SQLite3 탑재


# 데이터 입력 함수
def insert_books():
    conn = sqlite3.connect('database.db')  # 데이터베이스 커넥션 생성
    cur = conn.cursor()  # 커서 확보

    # 데이터 입력
    cur.execute("INSERT INTO booklist VALUES ('개발자의 코드', '2013.02.28','A', 200, 0)")

    # 데이터 입력 SQL
    insert_sql = 'INSERT INTO booklist VALUES (?, ?, ?, ?, ?)'

    # 튜플을 이용한 데이터 입력
    cur.execute(insert_sql, ('클린 코드', '2010.03.04','B', 584, 1))

    # 책의 정보를 담고 있는 튜플들의 리스트
    books = [
        ('빅데이터 마케팅', '2014.07.02','A', 296, 1),
        ('구글드', '2010.02.10','B', 526, 0),
        ('강의력', '2013.12.12','A', 248, 1),
        ('점프 투 파이썬', '2013.05.02','B',321,0),
        ('마기','2012.01.02','A',120, 1)
    ]

    # 여러 데이터 입력
    cur.executemany(insert_sql, books)

    conn.commit()       # 데이터베이스 반영

    conn.close()        # 커넥션 닫기

if __name__ == "__main__":		# 외부에서 호출 시
    insert_books()                  # 데이터 입력 함수 호출

