import requests
import serial
import os

# Verbindung zum Barcode-Scanner über USB
ser = serial.Serial('/dev/ttyUSB0', 9600)

def scan_barcode():
    barcode = ser.readline().decode('utf-8').strip()
    return barcode

def send_to_server(barcode, action):
    url = os.getenv('SERVER_URL') + "/scan"
    data = {'barcode': barcode, 'action': action}
    response = requests.post(url, json=data)
    print(response.json())

if __name__ == "__main__":
    while True:
        action = input("Wareneingang (WE) oder Warenausgang (WA)? ")
        barcode = scan_barcode()
        send_to_server(barcode, action)
