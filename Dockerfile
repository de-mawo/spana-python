FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies


# Set working directory
WORKDIR /usr/src/web


# Install dependencies
COPY requirements.txt /usr/src/web
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy every content from the local file to the image
COPY . /usr/src/web



CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]

