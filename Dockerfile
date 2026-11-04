# UD3.2h: imagen y arranque del proyecto con Docker.
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY PilatesLife/ .
EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && exec python manage.py runserver 0.0.0.0:8000"]
