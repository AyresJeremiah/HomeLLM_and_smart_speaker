# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir transformers torch flask

# Expose port 8000 (or any port your model server uses)
EXPOSE 8000

# Copy the model serving script
COPY serve_model.py /app/

# Start the model server
CMD ["python", "serve_model.py"]
