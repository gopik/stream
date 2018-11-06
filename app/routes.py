from flask import Response, render_template
from app import app
from app.camera import Camera

@app.route('/')
@app.route('/index')
def index():
    user = {
        'name' : 'Name'
    }
    return render_template('index.html', title='Home', user=user)


@app.route('/video')
def video():
    return Response(gen_video(), mimetype='multipart/x-mixed-replace; boundary=image')

def gen_video():
    args = get_args()
    if args.source == 'video':

       camera = Camera(args.source_uri)
       for image in camera:
           yield (b'--image\r\n' b'Content-type: image/jpeg\r\n\r\n' + image + b'\r\n')

def get_args():
    return app.config['ARGS']