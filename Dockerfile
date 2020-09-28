FROM python:3.8-alpine3.12

WORKDIR /src

COPY . .

ENTRYPOINT python3 ./src/Main.py
