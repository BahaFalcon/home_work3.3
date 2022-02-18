import psycopg2

conn = psycopg2.connect(dbname='titanicdb', user='postgres')
cur = conn.cursor()

cur.execute(
    """CREATE TABLE passengers( id integer, survived integer, class integer, name text,
     sex varchar(50), age integer, sibsp integer, parch integer, ticket varchar(255),
     fare numeric NULL, cabin varchar(255) NULL, embarked varchar(50) ) """
)
with open(r'titanic.txt', 'r') as f:
    next(f)
    cur.copy_from(f, 'passengers', sep='|')

conn.commit()
#1
cur.execute("""
    SELECT * FROM passengers where survived=0
""")
#2
cur.execute("""
    SELECT class FROM passengers where class=1 and sex=female and survived=1
""")
#3
cur.execute("""
    SELECT avg(age) FROM  passengers where age<20 and sex=male and survived=1
""")
#4
cur.execute("""
    SELECT name FROM passengers where age>30 and survived=1
""")
#5
cur.execute("""
    SELECT name FROM passengers where sex=female and embarked=C
""")
#6
cur.execute("""
    SELECT name FROM passengers where sibsp>1
""")
cur.close()
conn.close()
