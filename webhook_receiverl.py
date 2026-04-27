from flask import Flask, request, jsonify
import requests
import urllib3

# Suppress InsecureRequestWarning warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    print("Received Webhook Data:")
    print(data)

    # Example: forwarding data to another HTTPS endpoint
    # without validating its SSL certificate
    try:
        response = requests.post(
            "https://example.com/api/endpoint",
            json=data,
            verify=False  # <-- Disables SSL certificate verification
        )
        print(f"Forwarded response status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error forwarding data: {e}")

    return jsonify({"status": "success", "message": "Webhook received"}), 200

if __name__ == '__main__':
    app.run(port=6767, debug=True)