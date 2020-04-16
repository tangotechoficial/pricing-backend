FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN apt-get update \
    && apt-get -y install unzip \
    && apt-get -y install libaio-dev

ENV ORACLE_HOME=/opt/oracle/instantclient
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME

ENV OCI_HOME=/opt/oracle/instantclient
ENV OCI_LIB_DIR=/opt/oracle/instantclient
ENV OCI_INCLUDE_DIR=/opt/oracle/instantclient/sdk/include

CMD [ "ls -l" ]

# INSTALL INSTANTCLIENT AND DEPENDENCIES
RUN chmod +x ./install-instantclient.sh
RUN ./install-instantclient.sh \
    && pip install -r requirements.txt