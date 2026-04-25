#/usr/bin/python3
#-*- coding:utf-8 -*-
#task_02_requests.py

import unittest
from study_181130_request.task_01_requests import HttpRequests

COOKIES=None

class TestHttpRequests(unittest.TestCase):

    def setUp(self):
        pass

    def __init__(self,url,param,http_method,excepted,methodName):
        self.param=param
        self.http_method=http_method
        self.url=url
        self.excepted=excepted
        super(TestHttpRequests,self).__init__(methodName)

    def test_api(self):
        global COOKIES
        res=HttpRequests().http_requests(self.url,self.param,self.http_method,COOKIES)
        try:
            self.assertEqual(self.excepted,res.json()['msg'])
        except AssertionError as e:
            print('断言结果是：{}'.format(e))
            raise e

        if res.cookies:
            COOKIES=res.cookies
