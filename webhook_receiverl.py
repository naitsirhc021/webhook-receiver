from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data from the request
    data = request.json
    
    # Display the received data in the console
    print("Received Webhook Data:")
    print(data)
    
    # Return a success response
    return jsonify({"status": "success", "message": "Webhook received"}), 200

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(port=5000, debug=True)
