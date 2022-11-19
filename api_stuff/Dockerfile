FROM python:3.10.6
WORKDIR /api_stuff
COPY ./ /api_stuff
RUN pip install uvicorn
RUN pip install fastapi
RUN pip install httpx
RUN pip install -U pip
ENV FLASK_APP=/api_stuff/api/api.py
CMD ["python", "/api_stuff/api/api.py"]
