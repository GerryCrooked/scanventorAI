# scanventorAI - Barcode Inventory System

scanventorAI is a barcode-based inventory tracking system that uses Raspberry Pi devices and a 1D barcode scanner. It tracks inventory by scanning barcodes and updating the quantities in a centralized MySQL database. The system can automatically identify unknown barcodes using an integrated AI, powered by TensorFlow, and manage multiple warehouse locations.

## Features
- **Inventory Management**: Handle goods coming in (increment inventory) and going out (decrement inventory).
- **AI Integration**: Automatically identify unknown barcodes via TensorFlow integration.
- **Dockerized Database**: The MySQL database runs as a standalone Docker container on a separate server, e.g., Proxmox.
- **Multi-location Support**: Manage inventories from multiple locations using Raspberry Pi clients.
- **Threshold Alerts**: Get notified when inventory levels fall below customizable thresholds.
- **Touchscreen-friendly**: Optimized for touchscreen buttons.
- **Local & Shared AI Options**: Choose between running a local AI model or using shared AI data with other users.

## Architecture

- **MySQL Database**: Runs as a Docker container on a server (e.g., Proxmox).
- **Raspberry Pi Client**: Handles barcode scanning and sends data to the MySQL database.
- **TensorFlow AI**: Integrated with the Raspberry Pi for identifying unknown barcodes.

## Prerequisites

### For the Database Server (on Proxmox or any other server):
- **Docker** and **Docker Compose** installed.
- **MySQL** Docker image.

### For the Raspberry Pi Client:
- **Raspberry Pi** with a 1D barcode scanner.
- **Python 3.9+** with TensorFlow installed.
- **Docker** installed (for easier deployment of client components).

## Setup Instructions

### Step 1: Setup the MySQL Database on Proxmox (or other server)

1. **Clone the Repository on your Proxmox Server**
   ```bash
   git clone https://github.com/GerryCrooked/scanventorAI.git
   cd scanventorAI


2. **Configure Environment Variables**
   Create a .env file in the scanventorAI/server directory with the following variables:
   ```bash
   MYSQL_ROOT_PASSWORD=<your-mysql-root-password>
   MYSQL_DATABASE=<database-name>
   MYSQL_USER=<your-mysql-user>
   MYSQL_PASSWORD=<your-mysql-password>

3. **Build and Run Docker Containers**
   ```bash
   cd server
   docker-compose up --build -d
   ```
   This will:
   - Set up the MySQL database inside a Docker container.
   - Expose the database for external connections (make sure to configure firewall settings).

### Step 2: Setup the Raspberry Pi Client

1. **Clone the Repository on your Raspberry Pi**
   ```bash
   git clone https://github.com/GerryCrooked/scanventorAI.git
   cd scanventorAI/raspberrypi

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Configure Environment Variables for the Client**
   Create a .env file in the scanventorAI/raspberrypi directory with the following variables:
   ```bash
   DB_HOST=<proxmox-server-ip>
   DB_USER=<your-mysql-user>
   DB_PASSWORD=<your-mysql-password>
   DB_NAME=<database-name>
   AI_MODE=<local or shared>
   THRESHOLD_ALERT=<your-threshold-value>
   
4. **Set up systemd for automatic startup**
   create a new systemd service file so that the Raspberry Pi clients runs automatically on boot:
   ```bash
   sudo nano /etc/systemd/system/scanventorAI.service
   ```

   add the following content to the file:
   ```ini
   [Unit]
   Description=ScanventorAI Barcode Client
   After=network.target
   ```
   
   [Service]
   ExecStart=/usr/bin/python3 /path/to/scanventorAI/raspberrypi/app.py
   WorkingDirectory=/path/to/scanventorAI/raspberrypi
   EnvironmentFile=/path/to/scanventorAI/raspberrypi/.env
   Restart=always
   User=pi
   
   [Install]
   WantedBy=multi-user.target
   ```

   Make sure to replace /path/to/scanventorAI with the actual path where you cloned the repository.

5. **Enable and Start the systemd Service**
   enable the service so it starts at boot:
   ```bash
   sudo systemctl enable scanventorAI.service
   ```

   Start the service manually for the first time:
   ```bash
   sudo systemctl start scanventorAI.service


### Step 3: Access the Application
Database Access: You can connect to the MySQL database running on the Proxmox server using a MySQL client or application.
Client Logging: The Raspberry Pi client logs interactions with the database and AI recognition.
