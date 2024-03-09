FROM python:3.10-slim-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p app

COPY ./App app

EXPOSE 5000

CMD [ "python", "app.py", "--host", "0.0.0.0", "--port", "5000" ]