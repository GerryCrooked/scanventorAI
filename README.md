# scanventorAI
Raspberry Pi Barcode Scanner with AI Integration 

This repository contains the necessary files to deploy an inventory system via docker and Raspberry Pi-based barcode scanner(s) with AI-assisted product recognition. The scanner updates stock in a centralized MySQL database, and the AI can either be used locally or connected to a shared AI for enhanced learning.

# scanventorAI Server
the server consists of 3 components: 
**- MySQL-Database**
**- Web-App (Flask)**
**- AI-component (local / shared)**




# RaspberryPi Clients
## Features

- Raspberry Pi-based barcode scanner
- MySQL database integration to update stock on scan with location tracking
- AI product recognition (local or shared)
- Simple touchscreen interface for item confirmation
- Scalable across multiple Raspberry Pi devices
- Docker support for easy deployment

## Prerequisites

- A Raspberry Pi with a touchscreen and barcode scanner
- Python 3.x
- Git
- Docker installed on the Raspberry Pi

## Hardware recommendations

**Barcode Scanner**

https://de.aliexpress.com/item/1005004266461375.html?spm=a2g0o.detail.0.0.3ae7S9EpS9EpTf&mp=1&_gl=1*16mtcbo*_gcl_aw*R0NMLjE3MjU4ODU5NDQuQ2p3S0NBand1ZnEyQmhBbUVpd0FuWnF3OGdrclZXNjhEd2kwbFg2b18wd3Nmek1xXzYxWi1KYncta0tVSndZU2hVRmpncUVZRGJkdDZob0NTdzhRQXZEX0J3RQ..*_gcl_dc*R0NMLjE3MjU4ODU5NDQuQ2p3S0NBand1ZnEyQmhBbUVpd0FuWnF3OGdrclZXNjhEd2kwbFg2b18wd3Nmek1xXzYxWi1KYncta0tVSndZU2hVRmpncUVZRGJkdDZob0NTdzhRQXZEX0J3RQ..*_gcl_au*MjYyMzYxODU4LjE3MjU1MjM4NDQ.*_ga*MTc5OTY5MzUxNi4xNzE3NTg3NDA5*_ga_VED1YSGNC7*MTcyNzE2MTQyMi4xNi4xLjE3MjcxNjI2MzcuNTkuMC4w&gatewayAdapt=glo2deu

**RaspberryPi 4**

https://de.aliexpress.com/item/1005006639443404.html?spm=a2g0o.productlist.main.9.24b568fclLf1iE&algo_pvid=61523994-e574-40f1-8e7d-5bf931961017&algo_exp_id=61523994-e574-40f1-8e7d-5bf931961017-4&pdp_npi=4%40dis%21EUR%2168.39%2168.39%21%21%21523.66%21523.66%21%40211b617b17271627219216500e612f%2112000037896915614%21sea%21DE%212445467539%21X&curPageLogUid=HRYVUJgeBe7d&utparam-url=scene%3Asearch%7Cquery_from%3A

**TFT Touchdisplay for RaspberryPi**

https://de.aliexpress.com/item/1005006739026067.html?spm=a2g0o.productlist.main.5.6ba852794E0Kgb&algo_pvid=0e70e415-8c1b-4dac-a579-7a4a7b940b26&algo_exp_id=0e70e415-8c1b-4dac-a579-7a4a7b940b26-2&pdp_npi=4%40dis%21EUR%21100.96%2133.99%21%21%21773.05%21260.30%21%40211b617b17271628767501257e612f%2112000038141306666%21sea%21DE%212445467539%21X&curPageLogUid=egfLz3k2r2JX&utparam-url=scene%3Asearch%7Cquery_from%3A

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/raspberry-pi-barcode-scanner.git
   cd raspberry-pi-barcode-scanner

2. **Run the install script**:
   sudo chmod +x install.sh
   ./install.sh
   
3. **Configuration:** During intallation, you´ll be promted to enter your environment variables such as:
   **- MySQL Username**
   **- MySQL Password**
   **- MySQL Host**
   **- Hostname (Location)**
   You can also select whether to use the **shared AI** or a **local AI**

4. **Run the barcode scanner:**
   After intallation, start the scanner using:

   ```bash
   docker-compose up

## Installation Touchscreen

5. **Install Drivers for Touchscreen Display**
   ```bash
   sudo apt-get update
   sudo apt-get install -y cmake
   
Follow the driver's installation instructions for your screen.


7. **Tourchscreen Calibration**
   ```bash
   sudo apt-get install -y xinput-calibrator   
