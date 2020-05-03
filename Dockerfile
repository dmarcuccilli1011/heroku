FROM python:3.7

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# install dependencies
COPY Pipfile Pipfile.lock /code/ 
RUN pip install pipenv && pipenv install --system


# copy project
COPY . /code/
