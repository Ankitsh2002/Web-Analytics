from flask import Flask, render_template, request, jsonify
import mysql.connector
import re
from mysql.connector import Error

app = Flask(__name__)

# MySQL Database Configuration
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ankit@2002',
    'database': 'portfolio_db'
}

def get_db_connection():
    """Centralized MySQL connection function with error handling"""
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_db():
    """Initialize database and create tables if they don't exist"""
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS leads 
                           (id INT AUTO_INCREMENT PRIMARY KEY, 
                            name VARCHAR(255) NOT NULL, 
                            email VARCHAR(255) NOT NULL, 
                            message TEXT, 
                            source VARCHAR(255) NOT NULL, 
                            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
            conn.commit()
            print("MySQL database and table initialized successfully.")
        except Error as e:
            print(f"Error initializing database: {e}")
        finally:
            if conn.is_connected():
                conn.close()

# Route Handlers
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO leads (name, email, message, source) 
                               VALUES (%s, %s, %s, %s)''', 
                               (name, email, message, 'contact'))
                conn.commit()
                return jsonify({'message': 'Thank you! I\'ll get back to you soon.'})
            except Error as e:
                print(f"Database error: {e}")
                return jsonify({'message': 'Error saving your message.'}), 500
            finally:
                if conn.is_connected():
                    conn.close()
        else:
            return jsonify({'message': 'Database connection error.'}), 500
    return render_template('contact.html')

@app.route('/lead-gen', methods=['POST'])
def lead_gen():
    name = request.form['name']
    email = request.form['email']
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO leads (name, email, message, source) 
                           VALUES (%s, %s, %s, %s)''', 
                           (name, email, 'N/A', 'lead-gen'))
            conn.commit()
            return jsonify({'message': 'Thanks for signing up!'})
        except Error as e:
            print(f"Database error: {e}")
            return jsonify({'message': 'Error processing signup.'}), 500
        finally:
            if conn.is_connected():
                conn.close()
    else:
        return jsonify({'message': 'Database connection error.'}), 500

@app.route('/leads')
def view_leads():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute('''SELECT id, name, email, message, source, timestamp 
                           FROM leads ORDER BY timestamp DESC''')
            leads = cursor.fetchall()
            return render_template('leads.html', leads=leads)
        except Error as e:
            print(f"Database error: {e}")
            return render_template('error.html', message='Error retrieving leads'), 500
        finally:
            if conn.is_connected():
                conn.close()
    else:
        return render_template('error.html', message='Database connection error'), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
