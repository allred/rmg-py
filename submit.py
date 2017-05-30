#!/usr/bin/env python
from base import *

title = 'testsubmission ' + randstring()

r_imgur = imgur.upload_from_path(
  path = '/Users/mallred/Downloads/ratthumb.jpg',
)
print(r_imgur)

r_reddit = subreddit.submit(
  title=title,
  #selftext='',
  url=r_imgur['link'],
)
print(r_reddit)

