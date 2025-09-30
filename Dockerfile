FROM python:3.10-slim

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Download FastText model
RUN apt-get update && apt-get install -y wget && \
    wget -O lid.176.bin https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy server
COPY server.py .

EXPOSE 5000

CMD ["python", "server.py"]
