FROM python:3.6

WORKDIR /usr/src/app

RUN apt-get update && apt-get install libsodium-dev -y


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./server.py" ]
