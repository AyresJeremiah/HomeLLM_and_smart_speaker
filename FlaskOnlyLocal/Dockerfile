# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install necessary dependencies, including flac and pocketsphinx
RUN apt-get update && apt-get install -y flac \
    && pip install pocketsphinx

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
