#! /usr/local/bin/python2.7.15
# -*- coding: utf-8 -*-

import atx

d = atx.connect("http://localhost:8100")
d.start_app("com.baidu.tieba")
d(text=u'首页').click()
d(text=u'我的').click()
