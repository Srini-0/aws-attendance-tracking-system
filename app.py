from flask import Flask, request, jsonify, render_template
import pymysql
import os

# Database connection details
DB_HOST = os.environ.get('DB_HOST', 'attendance-db.c0ruc64m0izz.us-east-1.rds.amazonaws.com')
DB_USER = os.environ.get('DB_USER', 'admin')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'Attendance!db123')
DB_NAME = os.environ.get('DB_NAME', 'attendance_db')

def get_db():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        autocommit=True
    )

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mark', methods=['POST'])
def mark_attendance():
    data = request.get_json() or request.form
    name = data.get('name')
    date = data.get('date')

    if not name or not date:
        return jsonify({"message": "name and date are required"}), 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO attendance (name, date) VALUES (%s, %s)", (name, date))
    cur.close()
    conn.close()

    return jsonify({"message": "Attendance marked!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '80'))
    app.run(host='0.0.0.0', port=port)
