#! /usr/bin/python

# Python's bundled WSGI server
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape


def application(environ, start_response):
    # Returns a dictionary in which the values are lists
    d = parse_qs(environ['QUERY_STRING'])

    # content that will be displayed on web
    response_body = "Query info:\n  %s" % str(d)
 
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]

# Instantiate the server
httpd = make_server(
    'localhost', # The host name
    8888, # A port number where to wait for the request
    application # The application object name, in this case a function
)

# Wait for a single request, serve it and quit
# httpd.handle_request()

# Run server foreverly
httpd.serve_forever()
