FROM python:3.11-slim

WORKDIR /code

# Copy igc_lib requirements to the expected location
COPY requirements.txt /code/igc_lib/requirements.txt

# Copy xcmetrics requirements
COPY service/xcmetrics/requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application code
COPY service/xcmetrics /code/app

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
