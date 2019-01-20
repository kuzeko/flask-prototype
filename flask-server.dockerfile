FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN pip install --upgrade pip


# Flask App Requirements
RUN mkdir -p /app
WORKDIR /app
VOLUME /app
COPY ./flask-app/requirements.txt /app/requirements.txt
RUN cat /app/requirements.txt | grep -v '^#'  | grep -v '^-i' | xargs -n 1 pip install

# If you want to lint on build?
#RUN pip install pylint

# Actual Code goes Last so that previous things do not need to be re-run
COPY ./flask-app /app

#RUN pylint /app/xolap /app/core /app/main.py

EXPOSE 80
ENV STATIC_PATH /app/static
ENV FLASK_APP=main.py
ENV FLASK_DEBUG=0

ENTRYPOINT ["flask"]
CMD ["run", "--host", "0.0.0.0", "--port", "80"]

