import pyodbc

con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)}; DBQ=')
print("Connected")
con.execute("insert into ")
con.commit()
con.close()
print("zala")
