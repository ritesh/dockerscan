#!/usr/bin/env python
 
import os
import subprocess
import time
import urllib
from pprint import pprint
from zapv2 import ZAPv2
import sys

target = 'http://target/WebGoat'
http_proxy = 'http://zaproxy:8090' 
#Give ZAP some time to start up
time.sleep(5)
zap = ZAPv2(proxies={'http': http_proxy})
 
print 'Accessing target %s' % target
zap.urlopen(target)
time.sleep(2)
print 'Spidering target %s' % target
zap.spider.scan(target)
time.sleep(2)
while (int(zap.spider.status()) < 100):
    print 'Spider progress %: ' + zap.spider.status()
    time.sleep(2)
print 'Spider completed'
time.sleep(5)
print 'Scanning target %s' % target
zap.ascan.scan(target)
while (int(zap.ascan.status()) < 100):
    print 'Scan progress %: ' + zap.ascan.status()
    time.sleep(5)
print 'Scan completed'
reportname = "reports/zapreport-%s.xml" % (time.strftime("%d-%m-%Y-%H%M", time.localtime()))
with open(reportname, "w") as f:
    f.write(zap.core.xmlreport())
zap.core.shutdown()
