FROM python

WORKDIR /app/

COPY ./requirements.txt /requirements.txt

#ENV SERVER_PORT=${SERVER_PORT}
ARG SERVER_PORT
ENV SERVER_PORT $SERVER_PORT

ARG DOCKER_SERVER_PORT
ENV DOCKER_SERVER_PORT $DOCKER_SERVER_PORT

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./app /app

CMD ["python", "main.py"]

