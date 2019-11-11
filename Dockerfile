FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install pipenv gunicorn
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
CMD ["python", "run.py"]