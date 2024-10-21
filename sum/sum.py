from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the db-service URL as a global variable
DB_SERVICE_URL = 'http://db-service:5006/save'

@app.route('/api/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    
    # Extract numbers from the request data
    num1 = data.get('number1')
    num2 = data.get('number2')
    
    # Perform the sum operation
    result = num1 + num2
    
    # Prepare data for the external POST request
    save_data = {
        'result': result,
        'operation': 'sum'
    }
    
    # Make a POST request to the db-service
    try:
        response = requests.post(DB_SERVICE_URL, json=save_data)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        app.logger.error(f"Error saving to db-service: {e}")

    # Return the result even if saving to db-service fails
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
