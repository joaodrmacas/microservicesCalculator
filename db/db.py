from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

# MongoDB connection
# Retrieve env variable called MONGO_URI
# If it doesn't exist, use the default value
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://root:root@mongodb:27017/mydatabase')
client = MongoClient(MONGO_URI)
db = client.mydatabase  # Replace with your database name
log_collection = db.logs  # The 'logs' collection

@app.route('/save', methods=['POST'])
def save_log():
    data = request.get_json()

    # Extract result and operation from the request data
    result = data.get('result')
    operation = data.get('operation')

    # Create a log entry
    log_entry = {
        'operation': operation,
        'result': result,
        'timestamp': datetime.now()  # Log the time the request was received
    }

    # Insert the log entry into the 'logs' collection
    log_collection.insert_one(log_entry)

    # Return a success message
    return jsonify({'message': 'Log saved successfully'}), 201

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
