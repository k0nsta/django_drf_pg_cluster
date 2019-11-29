# Pull base image
FROM python:3.7.2-slim

# Instal psycopg2 dependencies
RUN apt-get update
RUN apt install -y gcc g++ python3-dev musl-dev \
    && apt install -y libffi-dev libpq-dev

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create dynamic directories
RUN mkdir /logs /uploads

# Set work directory
WORKDIR /code

# Install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Install project dependencies
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --ignore-pipfile --system

COPY ./compose/django/django-entrypoint.sh /django-entrypoint.sh
RUN chmod +x /django-entrypoint.sh

COPY ./compose/django/start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT [ "/django-entrypoint.sh" ]