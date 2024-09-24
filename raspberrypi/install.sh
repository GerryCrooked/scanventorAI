#!/bin/bash

# Create folder structure and copy scanner.py
mkdir /opt/scanventorAI
cp ./scanner.py /opt/scanventorAI

# Welcome Message
echo "Welcome to the Raspberry Pi Barcode Scanner setup!"

# User Inputs
read -p "Enter your device hostname: " hostname
read -p "Enter your database URL: " db_url
read -p "Enter your database username: " db_user
read -sp "Enter your database password: " db_password
echo ""

# Install Display Driver
echo "Installing display driver..."
sudo apt-get update
sudo apt-get install -y xserver-xorg xserver-xorg-input-evdev xserver-xorg-input-calibrator
sudo apt-get install -y xserver-xorg-input-multitouch

# Create a configuration file for the touchscreen
sudo bash -c 'cat <<EOT >> /usr/share/X11/xorg.conf.d/99-calibration.conf
Section "InputClass"
    Identifier "calibration"
    MatchProduct "Your Touchscreen Product Name"
    Option "Calibration" "1234 5678 1234 5678"  # Placeholder, replace with actual values
    Option "SwapAxes" "0"
EndSection
EOT'

# Calibrate Touchscreen
echo "Calibrating touchscreen..."
xinput_calibrator

# Create a systemd service
cat <<EOT >> /etc/systemd/system/barcode-scanner.service
[Unit]
Description=Barcode Scanner Service

[Service]
ExecStart=/usr/bin/python3 /opt/scanventorAI/scanner.py
WorkingDirectory=/opt/scanventorAI
Restart=always

[Install]
WantedBy=multi-user.target
EOT

# Reload systemd and enable service
sudo systemctl daemon-reload
sudo systemctl enable barcode-scanner.service
sudo systemctl start barcode-scanner.service

echo "Installation complete! Your Raspberry Pi is set up."
