FROM python:3.8
ENV SECRET_KEY ^pgnbyclrl9+r&l78uu=ca$m_bt4yv-i8acvvtjvk*$wv7w11-
ENV DEBUG True
ENV DB_HOST db
ENV AMBIENTE docker
ENV PYTHONUNBUFFERED=1
RUN mkdir /access_val
WORKDIR /access_val
COPY requirements.txt /access_val/
RUN pip install -r /access_val/requirements.txt
ADD . /access_val/
# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /access_val
USER appuser
EXPOSE 8000