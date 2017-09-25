#!/usr/bin/env python
from base import *

img = '/Users/mallred/Downloads/ratthumb.jpg'
img = '/Users/mallred/Downloads/cat.jpeg'
client = vision.ImageAnnotatorClient()
with open(img, 'rb') as image_file:
    content = image_file.read()
image = types.Image(content=content)
response = client.label_detection(image=image)
labels = response.label_annotations
pp.pprint(labels)


