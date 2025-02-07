# Use a smaller and more optimized base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first for better caching
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the application files
COPY ./app /app/app

# Expose the port FastAPI will run on
EXPOSE 80

# Start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# to create docker image : docker build -t language-detection-app .
# to run docker image : docker run -p 80:80 language-detection-app
# http://localhost:8080