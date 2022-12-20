FROM python:3.8-alpine

COPY . .

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev

RUN pip install --upgrade pip setuptools && \
	pip install -r requirements.txt

WORKDIR /web

CMD ["python", "app.py"]