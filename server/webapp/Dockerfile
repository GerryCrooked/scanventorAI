# Base image
FROM python:3.9-slim

# Install required packages for Apache2 and mod_wsgi
RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-wsgi-py3

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the Flask app to the container
COPY . /app
WORKDIR /app

# Configure Apache2
COPY ./webapp.conf /etc/apache2/sites-available/000-default.conf

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start Apache in the foreground
CMD ["apachectl", "-D", "FOREGROUND"]
