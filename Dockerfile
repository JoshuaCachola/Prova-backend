FROM python:3.8.2
RUN apt-get update && apt-get install -y netcat
RUN pip install pipenv
WORKDIR /app
COPY . /app
EXPOSE 8080
RUN pipenv install
CMD pipenv run waitress-serve --call 'app:create_app'