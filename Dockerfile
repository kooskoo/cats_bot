FROM cats:0.3

WORKDIR /cats

COPY . /cats

RUN apt-get update \
    && pip3 install pip --upgrade \
    && pip3 install -r requirements.txt

EXPOSE 80/tcp

CMD python3.7 bot.py