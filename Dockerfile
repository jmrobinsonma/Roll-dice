FROM jmrobinson/diceappv2
RUN mkdir /dice
VOLUME /dice
WORKDIR /dice
COPY . /dice
RUN pip3 install -r requirements.txt
CMD ["python3", "diceapp.py"]
