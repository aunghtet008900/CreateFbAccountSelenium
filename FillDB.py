import sqlite3
from RandomData import get_gender, get_firstname,\
    get_last_name, get_year, get_month, get_day

conn = sqlite3.connect('project.db', isolation_level=None)

count_new_users = 0;

while count_new_users<10:
    gender = get_gender()
    firstname =  get_firstname(gender)
    lastname = get_last_name()
    year = get_year()
    month = get_month()
    day = get_day()
    #email = firstname + lastname + str(year) + str(month) + str(day)
    #email = email[:30]
    email = "qweasdzxcert@protonmail.com"
    password = firstname[:4]+"*"+lastname[:4]+str(day)
    where = (firstname,lastname,year)
    if conn.execute("SELECT COUNT(ID) FROM USER WHERE FIRSTNAME=? AND LASTNAME=? AND YEAR=?",where).fetchone()[0] == 0:
        insert = (count_new_users,gender,firstname,lastname,year,month,day,email,password)
        res = conn.execute("INSERT INTO USER  VALUES (?,?,?,?,?,?,?,?,?)",insert)
        count_new_users += 1


conn.close()