from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the db-service URL as a global variable
DB_SERVICE_URL = 'http://db-service:5000/save'

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
    response = requests.post(DB_SERVICE_URL, json=save_data)

    # Check the response from the db-service (optional)
    if response.status_code == 200 or response.status_code == 201:
        return jsonify({'result': result, 'message': 'Saved successfully!'})
    else:
        return jsonify({'result': result, 'message': 'Failed to save.'}), 500

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
