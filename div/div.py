from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/div', methods=['POST'])
def divide_numbers():
    data = request.get_json()

    # Extract numbers from the request data
    num1 = data.get('number1')
    num2 = data.get('number2')

    # Check if the second number is zero
    if num2 == 0:
        return jsonify({'error': 'Division by zero is not allowed.'}), 400

    # Perform the division
    result = num1 / num2

    # Return the result as JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
