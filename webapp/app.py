#!/usr/bin/env python3

# Don't forget to set the environment variables before running this script:
# export FLASK_RUN_PORT="8081

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
from prometheus_client import Gauge
c = Gauge('my_failures_total', 'Total number of failures')
c.set(0)  # Set the failure gauge

@app.route('/', methods = ['GET'])
def index():
    """A dummy index route"""
    return "Hello, World!"

@app.route('/fail', methods = ['GET'])
def fail():
    """A dummy route that fails"""
    c.inc()
    return "This route always fails", 500

@app.route('/success', methods = ['GET'])
def success():
    """A dummy route that succeeds"""
    c.set(0)  # Reset the failure gauge
    return "This route always succeeds", 200

if __name__ == '__main__':
    ## start a HTTP server in a daemon thread
    # start_http_server(8081)
    # print("Prometheus metrics server started on port 8081")
    ## Keep the server running: do stuff to keep the main thread running aka server in a background
    # while True:
    app.run(host='0.0.0.0', port=8081)