# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app

# Expose port 8000 (or any port your model server uses)
EXPOSE 8000

# Copy the model serving script
COPY serve_model.py /app/

# Start the model server
CMD ["python", "serve_model.py"]
