FROM python:3.9-slim

WORKDIR /app

COPY insert_script.py /app/insert_script.py

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]
#CMD ["python", "insert_scrip.py"]
