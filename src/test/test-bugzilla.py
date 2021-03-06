#!/usr/bin/python -tt
#-*- coding: UTF-8 -*-

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# (C) 2011 - Tim Lauridsen <timlau@fedoraproject.org>
'''
Unit tests for bugzilla bug handling
'''


import sys
import os.path
sys.path.insert(0,os.path.abspath('../'))

import os
import os.path
import unittest
from FedoraReview.bugz import ReviewBug
from bugzilla import Bugzilla
from base import *

class BugzillaTests(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName)
        self.bug = ReviewBug(TEST_BUG)
        
    def setUp(self):
        if not os.path.exists(TEST_WORK_DIR):
            os.makedirs(TEST_WORK_DIR)
        self.bug.set_work_dir(TEST_WORK_DIR)

    def test_find_urls(self):
        ''' Test that we can get the urls from a bugzilla report'''
        rc = self.bug.find_urls()
        self.assertTrue(rc)
        self.assertEqual(self.bug.srpm_url,
        'http://timlau.fedorapeople.org/files/test/review-test/python-test-1.0-1.fc14.src.rpm')
        self.assertEqual(self.bug.spec_url,
        'http://timlau.fedorapeople.org/files/test/review-test/python-test.spec')


    def test_download_files(self):
        ''' Test that we can download the spec and srpm from a bugzilla report'''
        # download files
        rc = self.bug.download_files()
        self.assertTrue(rc)
        print("SRPM : %s " % self.bug.srpm_file)
        print("SPEC : %s " % self.bug.spec_file)
        # check the downloaded files locations
        srpm = TEST_WORK_DIR + 'python-test-1.0-1.fc14.src.rpm'
        spec = TEST_WORK_DIR + 'python-test.spec'
        self.assertEqual(self.bug.srpm_file, srpm)
        self.assertEqual(self.bug.spec_file, spec)
        # check that the downloaded files exists
        self.assertTrue(os.path.exists(srpm))
        self.assertTrue(os.path.exists(spec))
        
    def test_login(self):
        ''' test login to bugzilla 
        You need to use BZ_USER=<user> BZ_PASS=<password> make test to active the login test
        '''
        # Test failed login
        rc = self.bug.login(user='dummmy', password='dummy')
        self.assertEqual(rc,False)
        if 'BZ_USER' in os.environ and 'BZ_PASS' in os.environ:
            user = os.environ['BZ_USER']
            password = os.environ['BZ_PASS']
            rc = self.bug.login(user=user, password=password)
            self.assertEqual(rc, True)

suite = unittest.TestLoader().loadTestsFromTestCase(BugzillaTests)
unittest.TextTestRunner(verbosity=2).run(suite)
