# Tornado 

It is a Python web framework...Easily to set up the web server.
Here providing a very simple and easy example.

## Gunicorn

Gunicorn is a Python WSGI HTTP Server for UNIX. It is very simple to configure, compatible with many web frameworks and its fairly speedy.


## Installation

In order to use these features, you may need to install:
```
1. sudo apt-get install python-tornado
2. pip install gunicorn
```
## Example

First, you need to define the url with handler

```
    app = tornado.web.Application([
        (r"/", MainHandler)
    ])
```

After that, you can either use tornado it-self or gunicorn to start the server

### tornado

```
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()
```

### Gunicorn

```
    application = tornado.wsgi.WSGIAdapter(app)
    server = wsgiref.simple_server.make_server('', port, application)
    server.serve_forever()
```

## Version

Please take note that might minor changes of syntax on different version

```
    python          == 2.7.12
    python-tornado  == 4.2.1
    gunicorn        == 19.7.1
```
