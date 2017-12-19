FROM python:3-alpine
MAINTAINER fankunpeng
RUN pip install flask
COPY ./task.py /usr/local/services/task/
ENTRYPOINT ["python", "/usr/local/services/task/task.py"]
