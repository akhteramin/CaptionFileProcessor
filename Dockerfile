FROM python:3.6

ENV APP_DIR /caption-file-reader

RUN mkdir -p ${APP_DIR}

WORKDIR APP_DIR

ADD requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "caption_processor.py", "--dir", "Reference" ]