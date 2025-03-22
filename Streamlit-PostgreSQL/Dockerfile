# Use Python as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the app files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

