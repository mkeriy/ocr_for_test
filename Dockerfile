FROM python:3.9
WORKDIR /code

## Un-comment below lines to install dependencies
COPY ./requirements.txt code/requirements.txt

RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir --upgrade -r code/requirements.txt
# Install production dependencies.
COPY ./app /code/app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]