# Use the offical Streamlit base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Streamlit runs on port 8501 by default, so expose it
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "movie_app.py"]