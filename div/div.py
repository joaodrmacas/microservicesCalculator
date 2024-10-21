from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the db-service URL as a global variable
DB_SERVICE_URL = "http://db-service:5006/save"

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

    # Prepare data for the external POST request
    save_data = {
        'result': result,
        'operation': 'division'
    }

    # Make a POST request to the db-service
    try:
        response = requests.post(DB_SERVICE_URL, json=save_data)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        app.logger.error(f"Error saving to db-service: {e}")

    # Return the result as JSON even if saving fails
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
