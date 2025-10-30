import mysql.connector as sql

df = sql.connect(host = 'localhost',
                 user = 'root',
                 password = '12345',
                 use_pure = True)

cr = df.cursor()

# print(df)