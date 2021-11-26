# Blog Demo Project

## Blog app with ASGI server

### Summary
**Blog App** is build with Python / Django framework. In this project we are using ASGI(Asynchronous Server Gateway 
Interface) server. The main advantage of using ASGI is that it allows background coroutine so the application is able 
to do other things such listening for events on an external trigger. Can set asynchronous feature for realtime updates or chat/message feature. Ex. comment feature for blog.

### Key enhancement
- Asynchronous functionality

### Instructions
Follow below instructions to setup and run the **blog site** in local env.

### Prerequisites

- Python 3.6+

### Recommended tools

Creating a virtual python environment dedicated for this application is strongly recommended to prevent your local 
system from breaking unexpectedly.

- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

        $ pyenv install 3.6.9
        $ pyenv virtualenv 3.6.9 blogsite

### Setting up

1. Clone this repository and confirm if virtual env is activated if you use **pyenv** above.

        $ git clone https://github.com/nitinvi-dev/blog.git
        $ cd blog
        $ python --version
        Python 3.6.9

2. Run `pip install -r requirements.txt`

3. Run `python manage.py migrate` to create database tables.

4. Run `python manage.py createsuperuser` to create superuser to login and manage django admin.

5. Run `export DJANGO_ALLOW_ASYNC_UNSAFE=True` before starting server.

6. Run `gunicorn project.asgi:application -k uvicorn.workers.UvicornWorker` and visit below links.
    - http://localhost:8000/admin to create blogs.
    - http://localhost:8000 to view blogs.


## Crypto App

### Summary
**Crypto App** is project which traces the **TRC20** transactions of **USDT**. We've configured django-celery and 
django-celery-beat for running periodic tasks, So with the help of celery we've created a task which will send
daily summary of transaction. First when the task is executed it will fetch the TRC20 transactions and net balance of 
a give address with the help of one function, After that it will run another function which sends the
message on telegram regarding transaction summary.

### Key enhancements
- Daily summary updates to telegram from trongrid

### Instructions
Follow below instructions to setup and run the **Crypto App** in local env.

### Prerequisites

- Expect [Redis](https://redis.io/) is running locally on port **6379**

### Setting up

1. Run `celery -A project worker -l info` to start celery worker.

2. Open new terminal activate environment and Run `celery -A project beat -l info` to start celery beat.

3. You're good to go!!


## WSGI and ASGI

**WSGI**
- takes a single request and returns response at a time.

**ASGI**
- receive and send where you as an application has to receive and send messages both are asynchronous callable.




