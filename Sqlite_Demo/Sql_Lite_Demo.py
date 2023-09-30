import sqlite3
conn=sqlite3.connect("sqlite_demo.db")
conn.execute('''
    Create table student(
             st_id INT AUTO_INCREMENT PRIMARY KEY,
             st_name VARCHAR(50),
             st_class VARCHAR(20),
             st_email VARCHAR(30)
             )
''')
conn.close()