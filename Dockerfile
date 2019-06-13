FROM python:3.7.3

RUN apt-get update

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy

COPY . /app

ENTRYPOINT ["./script/entrypoint.sh"]
