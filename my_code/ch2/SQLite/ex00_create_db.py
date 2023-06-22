import sqlite3
from sqlite3 import Error

# 파일에 db 생성
con = sqlite3.connect('./apps/db/db.db')
cursor_db = con.cursor()

# 메모리에 db 생성
try:
    con = sqlite3.connect('memory')
    print('Create DB in memory')
except Error:
    print(Error)
finally:
    con.close()