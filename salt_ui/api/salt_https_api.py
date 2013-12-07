#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================

import urllib2,cookielib,urllib,yaml,json

class salt_api_token(object):
    def __init__(self,data,url,token=None):
        self.data = data
        self.url = url
        self.headers = {
            'User-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            "Accept":"application/x-yaml",

        }
        self.headers.update(token)


    def run(self):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        req = urllib2.Request(self.url,urllib.urlencode(self.data),self.headers)
        req.add_header("Referer","http://opts.jumei.com")
        resp = urllib2.urlopen(req)
        context = resp.read()
        return yaml.load(context)

