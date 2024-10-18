from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Base URLs for each microservice
SUM_SERVICE_URL = "http://sum-service:5000"
SUB_SERVICE_URL = "http://sub-service:5000"
MUL_SERVICE_URL = "http://mul-service:5000"
DIV_SERVICE_URL = "http://div-service:5000"



@app.route('/')
def index():
    return render_template("index.html")

# Endpoint to add two numbers using the sum microservice (POST request)
@app.route('/sum', methods=['POST'])
def add():
    data = request.json  # Receive the JSON body
    print(data, flush=True)
    a = data['number1']
    b = data['number2']
    
    # Send a POST request to the sum microservice
    response = requests.post(f"{SUM_SERVICE_URL}/api/sum", json={"number1": a, "number2": b})
    return jsonify(response.json())

# Endpoint to subtract two numbers using the sub microservice (POST request)
@app.route('/sub', methods=['POST'])
def subtract():
    data = request.json  # Receive the JSON body
    a = data['number1']
    b = data['number2']
    
    # Send a POST request to the sub microservice
    response = requests.post(f"{SUB_SERVICE_URL}/api/sub", json={'number1': a, 'number2': b})
    return jsonify(response.json())

# Endpoint to multiply two numbers using the mul microservice (POST request)
@app.route('/mul', methods=['POST'])
def multiply():
    data = request.json  # Receive the JSON body
    a = data['number1']
    b = data['number2']
    
    # Send a POST request to the mul microservice
    response = requests.post(f"{MUL_SERVICE_URL}/api/mul", json={'number1': a, 'number2': b})
    return jsonify(response.json())

# Endpoint to divide two numbers using the div microservice (POST request)
@app.route('/div', methods=['POST'])
def divide():
    data = request.json  # Receive the JSON body
    a = data['number1']
    b = data['number2']
    
    # Send a POST request to the div microservice
    response = requests.post(f"{DIV_SERVICE_URL}/api/div", json={'number1': a, 'number2': b})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
