FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /smart
ADD . /smart
COPY requirements.txt /smart/requirements.txt
RUN pip install -r requirements.txt
COPY . /smart
