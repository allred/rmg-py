#!/usr/bin/env python
# purpose: list images 
# TODO:
# - imgur
# - "section": "ratmongo"
import sys
from base import *

'''
r_imgur = imgur.upload_from_path(
  path = path_img,
)
'''
items = imgur.get_account_image_ids('redlotor')
for i in items:
  print(i.link)
