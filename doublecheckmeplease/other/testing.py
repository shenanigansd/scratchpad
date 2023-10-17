import jaydebeapi
connection = jaydebeapi.connect('com.filemaker.jdbc.Driver', 'jdbc:filemaker://192.168.10.6/Data_ODBCMapping', ['extro', 'extro'],'/home/darb/programming/scripting/vendor//fmjdbc.jar',)
cursor = connection.cursor()
cursor.execute("SELECT * FROM des WHERE ID_Design=66568")
#cursor.fetchall()
print(cursor.description)

