from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Datenbankverbindung
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    barcode = data.get('barcode')
    action = data.get('action')
    user_id = data.get('user_id')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # AI Mode des Benutzers abrufen
    cursor.execute('SELECT ai_mode FROM users WHERE id = %s', (user_id,))
    ai_mode = cursor.fetchone()['ai_mode']
    
    cursor.execute('SELECT * FROM items WHERE barcode = %s', (barcode,))
    item = cursor.fetchone()

    if item:
        if action == 'WE':
            cursor.execute('UPDATE items SET stock = stock + 1 WHERE barcode = %s', (barcode,))
        elif action == 'WA':
            cursor.execute('UPDATE items SET stock = stock - 1 WHERE barcode = %s', (barcode,))
        conn.commit()
        return jsonify({"message": "Success"}), 200
    else:
        if ai_mode == 'shared':
            # Anfrage an die geteilte AI-API
            response = requests.get(f'http://ai-server:5001/get-ai-data/{barcode}')
            if response.status_code == 200:
                item_name = response.json()['item_name']
            else:
                item_name = "Neuer Artikel"  # Fallback
        else:
            item_name = "Neuer Artikel"  # Lokale AI

        cursor.execute('INSERT INTO items (barcode, name, stock) VALUES (%s, %s, %s)', (barcode, item_name, 1))
        conn.commit()
        return jsonify({"message": "New item added"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
