#!/usr/bin/env python
# purpose: delete image(s) from imgur
# - for anonymous image, {id} must be the deletehash
# - if the image belongs to the account, ID is sufficient
import sys
from base import *

for i in imgur.subreddit_gallery('ratmongo'):
  #pp.pprint(inspect.getmembers(i))
  print(i.link)
#r_imgur = imgur.delete_image('AnvpKox')
