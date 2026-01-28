Dockerfile
# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
