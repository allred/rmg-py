#!/usr/bin/env python
from base import *


img = '/Users/mallred/Downloads/ratthumb.jpg'
img = '/Users/mallred/Downloads/cat.jpeg'
img_bytes = open(img, 'rb')
out = rekog.detect_labels(
  Image={
    "Bytes": img_bytes.read(),
        },
)
print({"out": out['Labels']})
