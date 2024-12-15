FROM python:3.12-slim

# Set the working directory
WORKDIR /fastapi

COPY ./requirements.txt /fastapi/requirements.txt
COPY ./app /fastapi/app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "fastapi", "run", "app/main.py", "--port", "8000" ]