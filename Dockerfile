FROM python:3.9-slim as app

ARG APP_DIR="/airpa/dash-example"
ARG BUILD_DEP="build-essential"
ARG RUN_DEP="make curl git vim zip unzip"

RUN mkdir -p ${APP_DIR}
COPY requirements.txt ${APP_DIR}/requirements.txt

RUN apt-get update && \
    /usr/local/bin/python -m pip install --upgrade pip && \
    apt-get install -y ${BUILD_DEP} && \
    apt-get install -y ${RUN_DEP} && \
    pip install -r ${APP_DIR}/requirements.txt && \
    rm -r ${APP_DIR}/requirements.txt && \
    apt-get remove -y ${BUILD_DEP}

WORKDIR ${APP_DIR}
COPY src/ ${APP_DIR}/src

EXPOSE 5000
CMD ["python", "src/index.py"]

FROM app as dev

COPY requirements.dev.txt ${APP_DIR}/requirements.dev.txt

RUN pip install -r ${APP_DIR}/requirements.dev.txt && \
    rm -r ${APP_DIR}/requirements.dev.txt && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -r awscliv2.zip aws/