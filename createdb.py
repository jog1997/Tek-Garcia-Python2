##Database creation for MySQL
##commented out since it only has to run once
import sqlalchemy
import pymysql
'''

mydb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='4242'
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE Puppy")

my_cursor.execute('SHOW DATABASES')

for db in my_cursor:
    print(db)
'''


