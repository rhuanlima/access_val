FROM python:3.8
ENV SECRET_KEY ^pgnbyclrl9+r&l78uu=ca$m_bt4yv-i8acvvtjvk*$wv7w11-
ENV DEBUG True
RUN mkdir /access_val
WORKDIR /access_val
# Installing OS Dependencies
COPY requirements.txt /access_val/
RUN pip install -r /access_val/requirements.txt
ADD . /access_val/
# Django service
EXPOSE 8000