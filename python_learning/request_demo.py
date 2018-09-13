#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import requests
import json


#r = requests.get('https://github.com/timeline.json')

# add timeout 超时
r = requests.get('https://github.com/timeline.json', timeout=1.5)
print "r.url :" + r.url

#add payload params
payload = {'key1': 'value1', 'key2': 'value2'}
r2 = requests.get("http://httpbin.org/get", params=payload)
print "r2 url :" + r2.url

#定制请求头
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)


print "type of r.text is :" + str(type(r.text))
print r.text

print "================"
#print r.json()
print type(r.json())

print "响应状态码================"
print r.status_code

print "响应头================"
#print r.headers