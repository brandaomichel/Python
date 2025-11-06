import psycopg2

con = psycopg2.connect(
    host='',
    database='postgres',
    user='postgres',
    password='TesteCurso1'
)

cur = con.cursor()
con.close()

