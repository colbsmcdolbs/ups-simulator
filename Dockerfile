FROM python:3.8.5-alpine3.12

WORKDIR /src

COPY . .

CMD [ "python3", "./src/Main.py" ]
