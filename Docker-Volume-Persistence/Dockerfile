# Use a lightweight Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy local files into the container
COPY . /app

# Install dependencies (if any)
RUN pip install flask

# Expose the application port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

