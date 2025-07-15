# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY app.py .
COPY saved_model.pkl .
COPY requirements.txt .
COPY templates/ ./templates/
COPY static/ static/

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
