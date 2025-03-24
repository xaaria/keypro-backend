# https://hub.docker.com/_/python

FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt ./

# Install deps.
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port. Make sure Djano runs on this port
EXPOSE 8000

# Do not remove 0.0.0.0:
# https://stackoverflow.com/questions/49476217/docker-cant-access-django-server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]