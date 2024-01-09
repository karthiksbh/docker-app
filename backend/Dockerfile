FROM python:3.11-slim

WORKDIR /backend

COPY . /backend

RUN apt-get update -y
RUN apt-get install pkg-config -y
RUN apt-get install -y python3-dev build-essential
RUN apt-get install -y default-libmysqlclient-dev

RUN pip install -r requirements.txt

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
