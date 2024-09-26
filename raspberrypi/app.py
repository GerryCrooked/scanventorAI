import os
import mysql.connector
import requests  # For API requests
from barcode_scanner import scan_barcode

# Load environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
recall_api_url = os.getenv('RECALL_API_URL')  # URL for checking food recalls
ai_server_url = os.getenv('AI_SERVER_URL', 'http://<server-ip>:5001/identify')

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = db_connection.cursor()

# Function to check if the product has been recalled
def check_recall_status(barcode):
    response = requests.get(f"{recall_api_url}?barcode={barcode}")
    if response.status_code == 200:
        data = response.json()
        return data.get("is_recalled", False)  # Assuming API returns this field
    return False

def process_barcode(barcode):
    # Check if barcode is known in the database
    cursor.execute("SELECT * FROM inventory WHERE barcode=%s", (barcode,))
    result = cursor.fetchone()
    
    if result:
        # Update inventory count for known barcode
        new_quantity = result['quantity'] + 1  # Assuming 'quantity' is the column name
        cursor.execute("UPDATE inventory SET quantity=%s WHERE barcode=%s", (new_quantity, barcode))
    else:
        # Send the barcode to the AI server for identification
        response = requests.post(ai_server_url, json={"barcode": barcode})
        item_name = response.json().get("item_name")

        # Check if the item has been recalled
        is_recalled = check_recall_status(barcode)

        # Insert new item into the database
        cursor.execute(
            "INSERT INTO inventory (barcode, name, quantity, is_recalled) VALUES (%s, %s, %s, %s)",
            (barcode, item_name, 1, is_recalled)
        )
    
    db_connection.commit()

if __name__ == "__main__":
    while True:
        barcode = scan_barcode()  # Scan a barcode using a connected USB barcode scanner
        process_barcode(barcode)
