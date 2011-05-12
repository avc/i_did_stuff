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
  
  def test_return_0_when_no_options(self):
    self.assertEqual(did.main(''), 0)
    self.assertEqual(did.main('something cool'), 0)
  
  #skip
  # def test_unrecognized_option_returns_error(self):
  #   self.assertNotEqual(did.main('-l'), 0)


if __name__ == '__main__':
  unittest.main()
  