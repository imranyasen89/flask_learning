from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create DB table
conn = sqlite3.connect('form.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age TEXT,
    email TEXT,
    city TEXT
)
''')

conn.commit()
conn.close()


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        city = request.form['city']

        conn = sqlite3.connect('form.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students (name, age, email, city) VALUES (?, ?, ?, ?)",
            (name, age, email, city)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)