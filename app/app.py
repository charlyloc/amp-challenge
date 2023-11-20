from flask import Flask, redirect
import mysql.connector
import json

app = Flask(__name__)

# Database Configuration
db_config = {
    'user': 'carlos',
    'password': 'pass123',
    'host': 'db',
    'database': 'amp',
    'port': '3306'
}

# Connect to Database
def db_connection():
    connection = None 
    try:
        connection = mysql.connector.connect(**db_config)
    except mysql.connector.Error as e:
        print(e)
    return connection

# Root path redirects to /greetings
@app.route('/')
def default():
    return redirect("/greetings", code=302)

# GET /greetings Returns total number of rows and last 3 rows
@app.route('/greetings')
def greetings():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) AS total FROM messages")
    total_rows = cursor.fetchone()['total']
    cursor.execute("SELECT * FROM messages ORDER BY timestamp DESC LIMIT 3")
    last_three_rows = cursor.fetchall()
    for row in last_three_rows:
        if 'timestamp' in row:
            row['timestamp'] = row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
    conn.close()
    return f"Total rows: {total_rows}\nLast three rows: {json.dumps(last_three_rows)}"

# POST /messages Adds a new row and returns its content
@app.route('/messages', methods=['POST'])
def add_message():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("INSERT INTO messages (content) VALUES ('Default message')")
    conn.commit()
    new_id = cursor.lastrowid
    cursor.execute("SELECT * FROM messages WHERE id = %s", (new_id,))
    new_row = cursor.fetchone()
    if 'timestamp' in new_row:
        new_row['timestamp'] = new_row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
    conn.close()
    return f"New row added: {json.dumps(new_row)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

