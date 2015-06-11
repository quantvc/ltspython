# encoding:utf-8

from __future__ import absolute_import

from unittest import TestCase
from ltsapi import common


class TestCommon(TestCase):

    def test_check_lts_parameter(self):
        request_id2 = "a"
        request_id3 = 1.2
        request_id4 = True

        self.assertRaises(Exception, common.check_lts_parameter_type, reuqest_id=request_id2)
        self.assertRaises(Exception, common.check_lts_parameter_type, reuqest_id=request_id3)
        self.assertRaises(Exception, common.check_lts_parameter_type, reuqest_id=request_id4)

        is_last1 = "0"
        is_last2 = 1

        self.assertRaises(Exception, common.check_lts_parameter_type, is_last=is_last1)
        self.assertRaises(Exception, common.check_lts_parameter_type, is_last=is_last2)
