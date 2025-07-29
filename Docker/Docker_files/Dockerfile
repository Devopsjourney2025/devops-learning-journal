# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . /app

# Install dependencies
RUN pip install flask

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
