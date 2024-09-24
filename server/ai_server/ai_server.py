import os
from flask import Flask, request, jsonify

app = Flask(__name__)

shared_ai_db = {}

@app.route('/submit-ai-data', methods=['POST'])
def submit_ai_data():
    data = request.json
    barcode = data.get('barcode')
    item_name = data.get('item_name')
    
    if barcode and item_name:
        shared_ai_db[barcode] = item_name
        return jsonify({"message": "AI data shared successfully"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

@app.route('/get-ai-data/<barcode>', methods=['GET'])
def get_ai_data(barcode):
    item_name = shared_ai_db.get(barcode, None)
    if item_name:
        return jsonify({"item_name": item_name}), 200
    else:
        return jsonify({"message": "No shared data found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
