import mysql.connector as mydb

# コネクションの作成
conn = mydb.connect(
    host='localhost',
    port='3306',
    user='testuser',
    password='testpass',
    database='test'
)

# コネクションが切れた時に再接続してくれるよう設定します。
conn.ping(reconnect=True)

# 接続できているかどうか確認
print(conn.is_connected())

# DB操作用にカーソルを作成
cur = conn.cursor()

# SQL文
cur.execute("SELECT * FROM fluits2")

rows = cur.fetchall()

for row in rows:
    print(row)
