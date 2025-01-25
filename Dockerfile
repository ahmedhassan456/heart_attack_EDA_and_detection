FROM python:3.10.12

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "deployment/app.py" ]