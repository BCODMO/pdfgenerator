#FROM ubuntu:latest
FROM surnet/alpine-python-wkhtmltopdf:3.7.3-0.12.5-full

#RUN apt-get update \
#  && apt-get install -y python3-pip python3-dev \
#  && cd /usr/local/bin \
#  && ln -s /usr/bin/python3 python \
#  && pip3 install --upgrade pip

#RUN apt-get update \
#    && apt-get install -y \
#	xvfb \
#	xfonts-100dpi \
#	xfonts-75dpi \
#	xfonts-scalable \
#	xfonts-cyrillic \
#	wkhtmltopdf

COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

EXPOSE 5001 

CMD [ "app.py" ]

