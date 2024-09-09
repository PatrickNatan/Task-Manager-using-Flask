FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip cache purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

ENV FLASK_APP=todo_project/run.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
