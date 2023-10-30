FROM python:3.9.18-alpine3.17

LABEL type="telegram_bot" team="pashabezk, dimbikey, rendex85, kubachinIlya"

WORKDIR /src

COPY ./src_good /src

RUN pip install --no-cache-dir -r /src/requirements.txt

ENV TOKEN="DO_NOT_ADD_TOKEN_ON_DOCKERFILE"

CMD ["python3", "/src/main.py"]
