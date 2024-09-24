#!/bin/bash

# Update und grundlegende Pakete installieren
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y python3 python3-pip python3-venv docker docker-compose git

# Python Virtual Environment und Abhängigkeiten einrichten
python3 -m venv venv
source venv/bin/activate

# Benötigte Python-Pakete installieren
pip install Flask mysql-connector-python tensorflow

# TensorFlow Model Setup (Placeholder)
echo "TensorFlow Model herunterladen oder trainieren
