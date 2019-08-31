FROM python:alpine3.7
COPY mongodb.py /var
COPY requirements.txt /var
WORKDIR /var
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["mongodb.py"]

