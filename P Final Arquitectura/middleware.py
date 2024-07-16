class WSGIMiddleware:
    def __init__(self, app):
        self.app = app
        self.app.wsgi_app = self.middleware(self.app.wsgi_app)

    def middleware(self, app):
        def middleware_func(environ, start_response):
            request_method = environ['REQUEST_METHOD']
            request_path = environ['PATH_INFO']
            headers = {key: value for key, value in environ.items() if key.startswith('HTTP_')}
            content_length = environ.get('CONTENT_LENGTH')
            request_data = environ['wsgi.input'].read(int(content_length)) if content_length else None

            print(f"Received {request_method} request to {request_path} with data: {request_data}")

            return app(environ, start_response)

        return middleware_func
