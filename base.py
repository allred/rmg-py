#!/usr/bin/env python
import boto3
import datetime
from google.cloud import vision
from google.cloud.vision import types
from imgurpython import ImgurClient
import inspect
import os
from PIL import Image 
from PIL.ExifTags import TAGS
import pprint
import praw
import random
import re
import string
import tempfile
import time
import urllib.request

imgur = ImgurClient(
  os.environ['RMG_IMGUR_CLIENT_ID'],
  os.environ['RMG_IMGUR_CLIENT_SECRET'],
)

pp = pprint.PrettyPrinter(indent=2)

reddit = praw.Reddit(
  user_agent='ratmongo'
)
subreddit = reddit.subreddit('ratmongo')

rekog = boto3.client('rekognition')

def randstring(size=6, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

