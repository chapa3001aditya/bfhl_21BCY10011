from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    
    if not isinstance(data, list):
        return jsonify({"is_success": False, "error": "Invalid input format"}), 400
    
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    highest_lowercase_alphabet = max([x for x in alphabets if x.islower()], default="", key=lambda x: ord(x))
    
    response = {
        "is_success": True,
        "user_id": "aditya_chapa_30012004",
        "email": "chapa3001aditya@gmail.com",
        "roll_number": "21BCY10011",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
    
    return jsonify(response), 200

@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
