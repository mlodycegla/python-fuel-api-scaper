FROM python:3
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD python -m flask --app flaskr/__init__.py run -h 0.0.0.0 -p 5000