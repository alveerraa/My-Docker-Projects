# Use a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies (if any)
RUN pip install -r requirements.txt

# Expose the required port
EXPOSE 5002

# Define the command to run the service
CMD ["python", "app.py"]

