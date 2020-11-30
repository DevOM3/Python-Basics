import pyodbc

query = "insert into menu(dishname, dishprice) values('softdrink', 25)"
con = pyodbc.connect(r'''Driver={Microsoft Access Driver (*.mdb, *.accdb)};
DBQ=C:\\Users\\ompra\\PycharmProjects\\RAVI SIR PYTHON\\tkinter projects\\sample.accdb;''')
con.execute(query)
con.commit()
con.close()
