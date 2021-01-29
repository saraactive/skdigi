FROM python:3
WORKDIR /home/node_microservice/

ADD app.py /
RUN pip install flask
RUN pip install flask_restful
EXPOSE 8080
CMD [ "python", "./app.py"]
