import mysql.connector
import RPi.GPIO as GPIO
import time
import subprocess

# User-defined parameters
hostname = "YOUR_HOSTNAME"  # Placeholder, should be replaced by the install script input
db_url = "YOUR_DB_URL"      # Placeholder
db_user = "YOUR_DB_USER"    # Placeholder
db_password = "YOUR_DB_PASSWORD"  # Placeholder

# Set up GPIO for barcode scanner button
BUTTON_PIN = 18  # Adjust based on your setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to connect to the database
def connect_db():
    return mysql.connector.connect(
        host=db_url,
        user=db_user,
        password=db_password,
        database='your_database_name'  # Replace with your actual database name
    )

# Function to scan barcode and update inventory
def scan_barcode():
    # Simulate barcode reading, replace this with actual barcode scanning logic
    barcode = input("Scan a barcode: ")
    return barcode.strip()

# Function to update stock in the database
def update_stock(barcode, action):
    try:
        db = connect_db()
        cursor = db.cursor()

        # Check if the item exists in the database
        cursor.execute("SELECT location FROM stock WHERE barcode = %s", (barcode,))
        result = cursor.fetchone()

        if result:
            location = result[0]
            if action == "WE":
                cursor.execute("UPDATE stock SET quantity = quantity + 1 WHERE barcode = %s", (barcode,))
            elif action == "WA":
                cursor.execute("UPDATE stock SET quantity = quantity - 1 WHERE barcode = %s", (barcode,))
            db.commit()
            print(f"Updated {action} for {barcode} at {location}.")
        else:
            # Insert new item with default quantity and location
            cursor.execute("INSERT INTO stock (barcode, quantity, location) VALUES (%s, %s, %s)", (barcode, 1, hostname))
            db.commit()
            print(f"Added new item {barcode} with quantity 1 at location {hostname}.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        db.close()

# Main loop
try:
    while True:
        print("Press the button to scan a barcode...")
        GPIO.wait_for_edge(BUTTON_PIN, GPIO.FALLING)
        time.sleep(0.2)  # Debounce delay

        barcode = scan_barcode()
        action = input("Enter action (WE for Wareneingang, WA for Warenausgang): ").strip().upper()
        if action in ["WE", "WA"]:
            update_stock(barcode, action)
        else:
            print("Invalid action. Please enter 'WE' or 'WA'.")

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
