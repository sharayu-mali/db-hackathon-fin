# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Embed mock data at build time
# RUN python embedder.py
# Copy requirements inline (you can also use requirements.txt)
COPY ./app ./app
COPY ./app/embedder.py ./embedder.py
# Expose port
EXPOSE 8000

# Launch FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
