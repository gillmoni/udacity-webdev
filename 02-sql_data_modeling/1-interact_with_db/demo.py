import psycopg2

connection = psycopg2.connect("dbname=example user=postgres password=1121")

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2')

cursor.execute('''
CREATE TABLE table2 (
id INTEGER PRIMARY KEY,
completed BOOLEAN NOT NULL DEFAULT False
);
''')

#method1
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);',(1, True))

#method2
cursor.execute('INSERT INTO table2 (id, completed)' + 
'VALUES (%(id)s, %(completed)s);',{
    'id':2,
    'completed':False
})

#method3, it's just a variation of #method2
data = {
    'id':3,
    'completed':True
}
SQL = 'INSERT INTO table2 (id, completed)' + 'VALUES (%(id)s, %(completed)s);'
cursor.execute(SQL, data)

connection.commit()

connection.close()
cursor.close()
