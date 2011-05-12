#!/usr/bin/env python
# encoding: utf-8
"""
timer_test.py

Created by Anthony Chan on 2011-05-11.
Copyright (c) 2011 Anthony Chan. All rights reserved.
"""

import did
import unittest

class did_tests(unittest.TestCase):
  def setUp(self):
    pass
  
  def test_tweet_when_no_options(self):
    self.assertEqual(did.main('something cool'), 0)


if __name__ == '__main__':
  unittest.main()
  