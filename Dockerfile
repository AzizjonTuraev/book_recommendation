FROM python:3.11.11
WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*  
    # Clean up to reduce image size

COPY . .                                          
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "server.server_api:app", "--reload"]

### Commands to run the Dockerfile
# docker build -t recommendation_books:latest -f Dockerfile .
# docker run -p 8000:8000 recommendation_books:latest