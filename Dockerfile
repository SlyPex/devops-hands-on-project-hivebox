FROM python:3.11.13-alpine3.22 AS builder
COPY requirements.txt .
RUN pip install --no-cache-dir --no-deps -r requirements.txt

FROM python:3.11.13-alpine3.22
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY main.py VERSION /app/
USER 1000:1000
ENTRYPOINT [ "python3", "main.py" ]