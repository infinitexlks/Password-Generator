from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_strong_password(password):
    # Check the password strength
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%^&+=]", password):
        return False
    return True

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if not is_strong_password(password):
        return jsonify({"error": "Password is not strong enough. It must be at least 8 characters long and include a mix of uppercase, lowercase, digits, and special characters."}), 400

    # Here you would normally save the user to your database
    # For this example, we just return a success message
    return jsonify({"message": "User signed up successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
