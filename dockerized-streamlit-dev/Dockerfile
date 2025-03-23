# Use an official Python base image  
FROM python:3.10  

# Set the working directory inside the container  
WORKDIR /app  

# Copy the current directory contents into the container  
COPY . .  

# Install required Python libraries  
RUN pip install --no-cache-dir streamlit  

# Expose the default Streamlit port  
EXPOSE 8501  

# Command to run the Streamlit app  
CMD ["streamlit", "run", "app.py"]

