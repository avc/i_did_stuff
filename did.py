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
'''


class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg


def main(argv=None):
  if argv is None:
    argv = sys.argv
    print time.time()
    
  try:
    try:
      opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
    except getopt.error, msg:
      raise Usage(msg)
  
    # option processing
    for option, value in opts:
      if option == "-v":
        verbose = True
      if option in ("-h", "--help"):
        raise Usage(help_message)
      if option in ("-o", "--output"):
        output = value
  
  except Usage, err:
    print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
    return 2


# Class

class did:
  def __init__(self):
    pass


if __name__ == "__main__":
  sys.exit(main())
