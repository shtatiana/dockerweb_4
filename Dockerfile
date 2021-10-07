FROM python:3.8-alpine

WORKDIR /webapp4

COPY . /webapp4

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "webapp.py"]