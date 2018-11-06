from gevent.pywsgi import WSGIServer
from app import app
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', help='Source for the video', choices=('camera', 'video'), required=True)
    parser.add_argument('--source_uri', help='Path for the video file or the camera', required=True)

    args = parser.parse_args()
    app.config['ARGS'] = args

    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

if __name__ == '__main__':
    main()