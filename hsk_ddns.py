#!/usr/bin/env python
#coding:utf8

import os
import time
import requests

class HskClient:
    hsk_api, hostname, username, password, update_interval = '', '' , '', '', ''
    def hsk_ddns_update(self):
        hsk_ddns_update_url = 'http://' + self.username + ':' + self.password + '@' + self.hsk_api \
                              + '?hostname=' + self.hostname
        time_now=time.asctime(time.localtime(time.time()))
        response = requests.get(hsk_ddns_update_url)
        print ('update_time:', time_now, 'result:', response.text)

# 花生壳api地址（一般为固定），动态域名，用户名，密码，更新间隔（秒）
hsk_api='ddns.oray.com/ph/update'
hostname=os.environ.get('hostname')
username=os.environ.get('username')
password=os.environ.get('password')

if __name__ == '__main__':
    hsk_client=HskClient()
    hsk_client.hsk_api=hsk_api
    hsk_client.hostname=hostname
    hsk_client.username=username
    hsk_client.password=password
    hsk_client.hsk_ddns_update()
