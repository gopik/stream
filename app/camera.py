import imageio
import time

def Camera(path):
    image_reader = imageio.get_reader(path)
    for img in image_reader:
        yield imageio.imwrite('<bytes>', img, 'jpg')
