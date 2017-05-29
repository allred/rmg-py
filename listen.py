#!/usr/bin/env python
from base import *

#print(reddit.read_only)
#print(subreddit.title)

def getexif(file_temp):
  i = Image.open(file_temp.name)
  # FIXME: imgur strips exif, get exif from the smallest reddit thumbnail
  info = i._getexif()
  #pp.pprint(inspect.getmembers(info))
  #for tag, value in info.items():
    #decoded = TAGS.get(tag, tag)
    #pp.pprint(decoded)
    #pp.pprint(value)

def retrieve_imgur(url):
  file_temp = tempfile.NamedTemporaryFile(
    delete=False,
    mode='w+b',
    prefix='rmg-imgur',
    suffix='.jpg',
  )
  print(file_temp.name)
  m = re.search('^.*\/(\S+?)$', url)
  img = imgur.get_image(m.group(1))
  #pp.pprint(inspect.getmembers(img))
  url_img = img.link
  urllib.request.urlretrieve(url_img, file_temp.name)
  return file_temp

def retrieve_reddit(url):
  file_temp = tempfile.NamedTemporaryFile(
    delete=False,
    mode='w+b',
    prefix='rmg-reddit-',
    suffix='.jpg',
  )
  print(file_temp.name)
  urllib.request.urlretrieve(url, file_temp.name)
  return file_temp

for submission in subreddit.stream.submissions():
  #pp.pprint(inspect.getmembers(submission))
  if submission.preview:
    #pp.pprint(submission.preview['images'][0]['resolutions'][-1]['url'])
    #url = submission.preview['images'][0]['resolutions'][-1]['url']
    url_preview_reddit = submission.preview['images'][0]['resolutions'][0]['url'] 
    print(url_preview_reddit)
    file_reddit = retrieve_reddit(url_preview_reddit)
    url_imgur = submission.url
    file_imgur = retrieve_imgur(url_imgur)
    getexif(file_reddit)
    print(submission.title)
