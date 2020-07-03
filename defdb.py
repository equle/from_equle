import sqlite3

def dbcon():
    return sqlite3.connect('mytestdb.db')

## insert 
def insert_data(id, pw):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw)
        c.execute("INSERT INTO student VALUES (?, ?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return "입력되었습니다."

## 전부 선택
def select_all():
    ret = list()
    try:
        conn = dbcon()
        c = conn.cursor()
        c.execute('SELECT * FROM student')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        conn.close()
        return ret

## 하나만 선택
def select_num(num):
    ret = ()
    try:
        conn = dbcon()
        c = conn.cursor()
        setdata = (num,)
        c.execute('SELECT * FROM student WHERE num = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        conn.close()
        return ret

## users table 생성 함수
def create_table():
    ret = list()
    try:
        query = '''
            CREATE TABL "users" (
                "id" varchar(50),
                "pw" varchar(50),
                "name" varchar(50),
                PRIMRY KEY("id")
            )
        '''
        conn = dbcon()
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        conn.close()
    return ret