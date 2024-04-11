from flask import Flask, render_template, request
import mysql.connector as mydb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    # コネクションの作成
    conn = mydb.connect(
        host='localhost',
        port='3306',
        user='testuser',
        password='testpass',
        database='test'
    )
    
    # DB操作用にカーソルを作成
    cur = conn.cursor()
    
    # SQL文
    cur.execute("SELECT * FROM fluits2")
    
    rows = cur.fetchall()
    
    # データベース接続を閉じる
    cur.close()
    conn.close()
    
    # 取得したデータを表示
    return render_template('data.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)