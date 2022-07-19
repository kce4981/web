FROM python:3.8
EXPOSE 8080

WORKDIR /app

ADD flask_app ./flask_app
COPY ./main.py ./
COPY ./requirements.txt ./
COPY ./config.json ./

RUN pip install -r requirements.txt


CMD ["python3", "main.py"]