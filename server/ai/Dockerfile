# Dockerfile for AI Server
FROM tensorflow/tensorflow:latest
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy model and code
COPY . /app

# Expose the Flask API
EXPOSE 5001

# Run the Flask server
CMD ["python", "ai_server.py"]
