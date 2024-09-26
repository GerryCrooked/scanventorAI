from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('model/barcode_model.h5')

def identify_barcode(barcode):
    prediction = model.predict([barcode])  # Placeholder prediction
    return prediction

@app.route('/identify', methods=['POST'])
def identify():
    data = request.json
    barcode = data['barcode']
    
    # Use the AI model to identify the barcode
    item_name = identify_barcode(barcode)
    
    return jsonify({"item_name": item_name})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
