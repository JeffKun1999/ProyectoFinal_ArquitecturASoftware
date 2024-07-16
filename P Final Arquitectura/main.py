import webbrowser
from threading import Timer
from app import app, controller
from middleware import WSGIMiddleware

middleware = WSGIMiddleware(app)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        controller.close_connection()