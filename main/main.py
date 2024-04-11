from flask import Flask, render_template, request
import mysql.connector as mydb

app = Flask(__name__)

def get_db_connection():
    return mydb.connect(
        host='localhost',
        port='3306',
        user='testuser',
        password='testpass',
        database='test'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM fluits2")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('data.html', rows=rows)

@app.route('/save_data', methods=['POST'])
def save_data():
    num1 = request.form['num1']
    text = request.form['text']
    num2 = request.form['num2']
    num3 = request.form['num3']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO fluits2 (id, name, price, stock) VALUES (%s, %s, %s, %s)", (num1, text, num2, num3))
    conn.commit()
    cur.close()
    conn.close()
    return get_data()

if __name__ == '__main__':
    app.run(debug=True)