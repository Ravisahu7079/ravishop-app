# Base image
FROM python:3.12-slim

# Working directory
WORKDIR /app

# Dependencies pehle copy karo (caching ke liye)
COPY requirements.txt .

# Dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# App code copy karo
COPY . .

# Port expose karo
EXPOSE 5000

# App start karo
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
