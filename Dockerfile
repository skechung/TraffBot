FROM python:3.7

COPY requirements.txt /root/
#Dependencies
RUN pip3 install -r root/requirements.txt
RUN apt-get update && apt-get install -y gunicorn && useradd -m traffbot

COPY src/server /home/traffbot
WORKDIR /home/traffbot
RUN chown -R traffbot:traffbot /home/traffbot
WORKDIR /home/traffbot/app
USER traffbot
EXPOSE 9000

CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]