from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    
    # Extract numbers from the request data
    num1 = data.get('number1')
    num2 = data.get('number2')
    
    # Perform the sum operation
    result = num1 + num2
    
    # Return the result as JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
