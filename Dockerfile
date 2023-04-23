
#
FROM python:3.8

USER root
#
WORKDIR /code

#
COPY Pipfile Pipfile.lock /code/

#
RUN pip install mysqlclient

RUN  pip install pipenv && pipenv install --dev --system --deploy

#
COPY ./ /code/

#
CMD ["python", "manage.py", "runserver"]