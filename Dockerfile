FROM python:3.8
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip3 install -r requirements.txt
CMD ["python3", "diceapp.py"]
