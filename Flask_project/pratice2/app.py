from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = '1234'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'my_flask_db'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/add', methods=['POST'])
def add_user():
    # Validate Content-Type
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 415
    
    data = request.json
    name = data.get('name')
    email = data.get('email')

    # Validate Input
    if not name or not email:
        return jsonify({'error': 'Name and email are required fields.'}), 400

    # Insert data into the database
    cursor = mysql.connection.cursor()
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'User added successfully!'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    # Fetch data from the database
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()

    # Format the response as a list of dictionaries
    formatted_users = [{'id': row[0], 'name': row[1], 'email': row[2]} for row in users]

    return jsonify(formatted_users)

if __name__ == '__main__':
    app.run(debug=True)
