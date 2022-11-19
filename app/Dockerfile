FROM python:3.10.6
WORKDIR /app
COPY ./app /app
RUN pip install flask
RUN pip install -U pip
ENV FLASK_APP=/app/app.py
CMD ["python", "/app/app.py"]
