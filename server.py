from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print("Received Data:", data)
    return jsonify({"message": "Data Received", "position": [2.5, 3.5]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
