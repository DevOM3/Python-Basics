import sqlite3

con = sqlite3.connect("db1")
con.execute("UPDATE DataBase1 SET NAME='OM_LONDHE' WHERE ROLL=186027")
con.commit()
con.close()
