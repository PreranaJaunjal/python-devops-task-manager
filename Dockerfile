
# Official Python base image
FROM python:3.12-slim

WORKDIR /app

# Update Linux security packages
RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*

# Create a dedicated non-root user
RUN addgroup --system app && \
    adduser --system --ingroup app app

# Install Python dependencies
COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" && \
    pip install --no-cache-dir -r requirements.txt

# Copy application with correct ownership
COPY --chown=app:app app/ ./app/

# Run as non-root
USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
