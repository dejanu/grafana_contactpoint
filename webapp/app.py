#!/usr/bin/env python3


# from prometheus_client import start_http_server

from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

# Create a metric to track time spent and requests made.
from prometheus_client import Counter
c = Counter('my_failures_total', 'Total number of failures')

@app.route('/', methods = ['GET'])
def index():
    """A dummy index route"""
    return "Hello, World!"

@app.route('/fail', methods = ['GET'])
def fail():
    """A dummy route that fails"""
    c.inc()  # Increment the failure counter
    return "This route always fails", 500

if __name__ == '__main__':
    ## start a HTTP server in a daemon thread
    # start_http_server(8081)
    # print("Prometheus metrics server started on port 8081")
    ## Keep the server running: do stuff to keep the main thread running aka server in a background
    # while True:
    app.run(host='0.0.0.0', port=8081)