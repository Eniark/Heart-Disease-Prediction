FROM python:3.8-alpine

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

WORKDIR /web

CMD ["python", "app.py"]