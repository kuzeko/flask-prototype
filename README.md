# Skeleton for an app 

If you need a web-server in python able to server static files, JSON, and process requests.

## Python Prototype

This is in python, sometimes is useful for quick web-app prototypes or as interface to a demo.

For the GUI you can  install the static css and js from some framework, I like a lot [Semantic UI](https://semantic-ui.com/introduction/getting-started.html).

## Flask Web-App

It uses Fask inside docker thanks to [tiangolo/uwsgi-nginx-flask](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/).


### Docker

```bash
docker build  -t my-name/flask-app -f flask-server.dockerfile .

docker run --rm -it --publish=80:80 \
    --volume=`pwd`/logs:/logs \
    my-name/flask-app
```

### Directory tree

```bash
.
├── Pipfile
├── README.md
├── flask-app
│   ├── config.py
│   ├── core                       # Here inser modules
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── routes.py              # Change routes here
│   ├── entrypoint.sh
│   ├── main.py
│   ├── requirements.txt
│   ├── static                     # Here put your static files
│   │   ├── css                       
│   │   ├── fonts
│   │   ├── images
│   │   └── js
│   ├── templates                  # Flask templates
│   │   ├── base.html
│   │   ├── error.html
│   │   └── index.html
│   └── uwsgi.ini
├── flask-server.dockerfile
└── logs                           # When the app runs, logs go here

```