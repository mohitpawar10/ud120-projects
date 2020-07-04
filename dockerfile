FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"