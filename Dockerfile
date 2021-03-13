FROM 327667905059.dkr.ecr.us-east-1.amazonaws.com/docker-base-image-python-3-7:1

RUN apt-get update && apt-get install -y python-pip

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt && \
  pip install --no-cache-dir newrelic

ENTRYPOINT ["newrelic-admin", "run-program"]

CMD ["python", "app/main.py"]
