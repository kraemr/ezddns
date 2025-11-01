FROM python:3.12-alpine
# Set environment variable for port (default 5000)
ENV PORT=5000
# Install build dependencies (if needed for requests, etc.)
RUN apk add --no-cache build-base
# Install Python dependencies
RUN pip install --no-cache-dir flask requests
# Copy app (assuming you’ll add it later)
WORKDIR /app
COPY . /app
# Expose the port defined by $PORT
EXPOSE ${PORT}
# Run the app (you can override this with docker run)
CMD ["sh", "-c", "python ezddns.py --port=${PORT}"]
