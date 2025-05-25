FROM apache/spark-py:3.4.0

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .