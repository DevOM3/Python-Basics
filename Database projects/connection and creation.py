import sqlite3

con = sqlite3.connect("db1")
# con.execute("CREATE TABLE DB1(NAME VARCHAR(20) NOT NULL, PH_NO NUMBER(13), ROLL NUMBER(6));")
con.commit()
con.close()
