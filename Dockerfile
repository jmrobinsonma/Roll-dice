FROM python:3.8
WORKDIR /usr/src/app
COPY . /usr/src/app
CMD ["python3", "diceapp.py"]
