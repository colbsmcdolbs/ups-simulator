FROM python:3.9-alpine3.12

COPY . .

ENTRYPOINT python3 ./src/main.py
