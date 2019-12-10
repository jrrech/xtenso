FROM python:3.7-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY . /xtenso
RUN pip install -e /xtenso
WORKDIR /xtenso
ENV FLASK_APP=xtenso
CMD [ "flask", "run", "--host=0.0.0.0" ]
