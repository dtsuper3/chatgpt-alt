from flask import Flask, request, jsonify
from gpt import generateText

app = Flask(__name__)

# Route for the home page
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask server!"

# Route for a simple API endpoint
@app.route('/api/generate', methods=['POST'])
def get_data():
    # data = request.json  # Assuming JSON data is sent in the request
    # Process the data or perform any required operations    
    response = generateText()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
