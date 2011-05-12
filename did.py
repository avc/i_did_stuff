#!/usr/bin/env python
# encoding: utf-8
"""
timer.py

Created by Anthony Chan on 2011-05-11.
Copyright (c) 2011 Anthony Chan. All rights reserved.

"""

import sys
import getopt
import time

help_message = '''
This program lets you track how you spend your time.

You put a marker down at different points in the day when you start something or accomplish something (or any time in between). This will help you later estimate how much time you spend on your activities. You can be as precise as you want to be; this tool just helps you by giving you a little reminder of what you did at around that time.

Try:
did something cool
did start writing a program 3 hours ago
  (The "ago" part is optional. It will add some time to the activity.)
did finish writing the I Did Stuff app
  (It will determine how long you worked on it by subtracting when you started it.)

did -l
  (List what you did in the past 24 hours)

did -l 1
  (List last thing you did.)

did -l yesterday (or just y)
  (List what you did yesterday. Good for achievement record.)
'''


class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg

def main(argv=None):
  if argv is None:
    argv = sys.argv
    
  try:
    try:
      opts, args = getopt.getopt(argv[1:], "lho:v", ["help", "output="])
    except getopt.error, msg:
      raise Usage(msg)
  
    # option processing
    for option, value in opts:
      if option == "-l":
        print >> sys.stderr, "hello"
        # did.show_tasks(value)
      if option == "-v":
        verbose = True
      if option in ("-h", "--help"):
        raise Usage(help_message)
      if option in ("-o", "--output"):
        output = value
    
    return 0
  
  except Usage, err:
    print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
    return 2


# Class

import twitter
import config
import os

class did:

  def __init__(self):
    """ Log into Twitter
    >>> d = did()
    """
    cfg = config.Config(os.path.expanduser('~/.didstuff'))
    
    self.twitter = twitter.Api(consumer_key = cfg.consumer_key,
      consumer_secret = cfg.consumer_secret,
      access_token_key = cfg.access_token_key,
      access_token_secret = cfg.access_token_secret)
    self.updates = self.twitter.GetUserTimeline('did_stuff')
  
  def show_tasks(self, what):
    """
    >>> d = did()
    >>> d.show_tasks(1)
    Test message from python-twitter.
    """
    if what == 1:
      print self.updates[0].text


if __name__ == "__main__":
  import doctest
  doctest.testmod()
  sys.exit(main())
