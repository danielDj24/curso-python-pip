FROM python:3.8

WORKDIR /APP
COPY requirements.txt /APP/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /APP/requirements.txt

COPY . /APP/

CMD bash -c "while true; do sleep 1; done"