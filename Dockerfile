FROM python:3.8.9
LABEL project = dishrank

COPY ./src ./src
ADD ./requirements.txt requirements.txt
ADD ./wait-for-it.sh wait-for-it.sh

RUN chmod +x ./wait-for-it.sh
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir
