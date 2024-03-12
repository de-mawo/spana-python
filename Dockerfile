FROM python:3.11-slim

# Set working directory
WORKDIR /usr/src/web

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy the local .env file to the working directory in the image
COPY .env ./

# Install dependencies
COPY requirements.txt /usr/src/web
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy every content from the local file to the image
COPY . /usr/src/web

COPY ./entrypoint.sh /usr/src/web

# Set permissions for the working directory
RUN chown -R appuser:appgroup /usr/src/web

# Set environment variables
ENV DATABASE_URI=""
ENV REDIS_URI=""
RUN while read -r line; do export $line; done < .env

# Switch to the non-root user
USER appuser

# Set execute permission for the entrypoint script
RUN chmod +x /usr/src/web/entrypoint.sh


# Use shell form for ENTRYPOINT to execute the script directly
# ENTRYPOINT ["/usr/src/web/entrypoint.sh"]

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]

