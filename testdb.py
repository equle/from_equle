import sqlite3

conn = sqlite3.connect('mytestdb.db')

## Cursor 객체 생성
c = conn.cursor()

## 테이블 생성
#c.execute("CREATE TABLE student (num varchar(50), name varchar(50))")

## excute에 db 적용
conn.commit()

## 데이터 입력
#c.execute("INSERT INTO student VALUES('20191027','김윤서')")
#c.execute("INSERT INTO student VALUES('20202020','이공이')")

## 데이터 불러와 출력
for row in c.execute('SELECT * FROM student'):
    print(row)

## 학번을 검색해 정보 출력
num = ('20202020', '이공이')
c.execute('SELECT * FROM student WHERE num = ? and name = ?', num)

## 아래의 쿼리문을 쓰게 되면 SQL 인젝션 공격에 강할 가능 성이 있다.
# "SELECT * FROM student WHERE num = %s" % num   ==   "SELECT * FROM student WHERE num = 20202020"

print(c.fetchone())
# fetchone = 1개
# fetchall = 전부

## 접속 db 닫기
conn.close()