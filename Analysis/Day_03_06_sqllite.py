# Day_04_03_sqlite.py
import sqlite3
import Day_02_07_csv
# sql : Structured Query Language

def createDB(filename):
    conn = sqlite3.connect(filename)
    cur  = conn.cursor()

    query = 'CREATE TABLE kma (prov text, city text, mode text, date text, desc text)'
    cur.execute(query)

    conn.commit()
    conn.close()
#
# filename='Data/kma.sqlite'
# createDB(filename)


def insert(filename, row):
    conn = sqlite3.connect(filename)
    cur  = conn.cursor()

    # INSERT INTO 테이블명 (COLUMN_LIST) VALUES (COLUMN_LIST에 넣을 VALUE_LIST);
    base = 'INSERT INTO kma VALUES ("{}", "{}", "{}", "{}", "{}")'
    query = base.format(row[0], row[1], row[2], row[3], row[4])
    cur.execute(query)

    conn.commit()
    conn.close()


rows = Day_02_07_csv.readCsv_2('Data/kms.txt')
# print(*rows, sep='\n')

# filename = 'Data/kma.sqlite'
# for row in rows:
#     insert(filename, row)



def insertAll(filename, rows):
    conn = sqlite3.connect(filename)
    cur  = conn.cursor()

    # INSERT INTO 테이블명 (COLUMN_LIST) VALUES (COLUMN_LIST에 넣을 VALUE_LIST);
    base = 'INSERT INTO kma VALUES ("{}", "{}", "{}", "{}", "{}")'

    for row in rows:
        query = base.format(row[0], row[1], row[2], row[3], row[4])
        cur.execute(query)

    conn.commit()
    conn.close()

def fetch(filename):
    conn = sqlite3.connect(filename)
    cur  = conn.cursor()

    query = 'SELECT * FROM kma'
    rows = []
    for row in cur.execute(query):
        rows.append(row)

    # conn.commit()
    conn.close()
    return rows

def fetchWhere(filename, search):
    conn = sqlite3.connect(filename)
    cur  = conn.cursor()

    query = 'SELECT * FROM kma WHERE city = "{}"'.format(search)
    rows = []
    for row in cur.execute(query):
        rows.append(row)

    # conn.commit()
    conn.close()
    return rows


filename='Data/kma.sqlite'
# rows = fetch(filename)
rows = fetchWhere(filename, '안동')
print(*rows, sep='\n')



# rows = Day_04_02_csv.readCsv_2('Data/kma.csv')
# print(*rows, sep='\n')

# filename = 'Data/kma.sqlite'
# createDB(filename)

# for row in rows:
#     insert(filename, row)

# insertAll(filename, rows)

# rows = fetch(filename)
# rows = fetchWhere(filename, '부산')
# print(*rows, sep='\n')








