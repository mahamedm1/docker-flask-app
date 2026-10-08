# Stage 1: Build Stage

FROM python:3.12-slim 

WORKDIR /app

COPY . .

RUN pip install flask redis

CMD ["python", "app.py"]