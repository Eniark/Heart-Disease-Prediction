FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR .

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

RUN chmod +x /scripts/run_app.sh

WORKDIR /myfolder

ENTRYPOINT [ "/scripts/run_app.sh" ]