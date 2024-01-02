FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=application.py
ENV FLASK_DEBUG=1
ENV API_KEY=MY_API_KEY

CMD ["python", "-m", "flask", "run"]