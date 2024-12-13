FROM python:3.12.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /aban-tether

COPY requirements.txt /aban-tether/
RUN python -m venv venv \
&& . venv/bin/activate \
&& pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir --timeout=30 -r requirements.txt

COPY . /aban-tether/

EXPOSE 8000

CMD ["venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "aban-tether.wsgi:application"]