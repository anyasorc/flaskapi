from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json  # Assuming JSON data is sent
    amt = data['amt']
    return jsonify(amt)

if __name__ == '__main__':
    app.run(debug=True)
