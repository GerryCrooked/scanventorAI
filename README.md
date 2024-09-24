# scanventorAI

ScanventorAI is a barcode scanning application that utilizes a Raspberry Pi for inventory management. It features a web server for managing scanned items and a TensorFlow-based AI for item recognition.

## Project Structure

- **/server**: Contains the server code, including the AI server and web application.
- **/raspberrypi**: Contains the Raspberry Pi application code.

## Installation and Configuration

### Server Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/GerryCrooked/scanventorAI.git
   cd scanventorAI/server
   
2. **Environment variables**:
   change the environment variables in the .env according to your environment

3. **Build and start the Docker Containers:**
   ```bash
   docker-compose up --build -d


### Raspberry Pi Setup

1. **Clone the Raspberry Pi Repository:**
   ```bash
   git clone https://github.com/GerryCrooked/scanventorAI.git
   cd scanventorAI/raspberrypi

2. **Installation**
   ```bash
   chmod +x install.sh
   ./install.sh

3. **Configuration during the installation process**
   *- hostname*
   *- database URL*
   *- Database username and password*
   *- install display driver*
   *- calibrate screen*

# License
this project is licensed under the MIT License. See the LICENSE file for details.
