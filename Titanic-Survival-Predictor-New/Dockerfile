# Use the official Python image
FROM python:3.9  

# Set the working directory
WORKDIR /app  

# Copy the local files into the container
COPY . .  

# Install dependencies  
RUN pip install -r requirements.txt  

# Expose the Streamlit port  
EXPOSE 8501  

# Run the Streamlit app  
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

