#!/usr/bin/env python
# purpose: submit an image to reddit/imgur
import sys
from base import *

title = 'testsubmission ' + randstring()

if len(sys.argv) > 1:
  path_img = sys.argv[1]
else:
  path_img = '/Users/mallred/Downloads/ratthumb.jpg'

r_imgur = imgur.upload_from_path(
  path = path_img,
)
print(r_imgur)

r_reddit = subreddit.submit(
  title=title,
  #selftext='',
  url=r_imgur['link'],
)
print(r_reddit)
