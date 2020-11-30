import sqlite3

con = sqlite3.connect("db1")
# con.execute("CREATE TABLE DB1(NAME VARCHAR(20) NOT NULL, PH_NO NUMBER(13), ROLL NUMBER(6));")
# con.execute("INSERT INTO DataBase1(NAME, PH_NO, ROLL) VALUES('BHARGAVI', 7276594468, 28)")
con.execute("INSERT INTO DataBase1(NAME, PH_NO, ROLL) VALUES('AJAY', 556236562, 941)")
con.commit()
con.close()
