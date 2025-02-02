FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app
# to create docker image : docker build -t language-detection-app .
# to run docker image : docker run -p 80:80 language-detection-app
# http://localhost:8080