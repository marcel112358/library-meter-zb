from __future__ import print_function

import requests
import re
from datetime import datetime
import time

while 1:
    r = requests.get('https://www.zb.uzh.ch/themes/zb/assets/js/gauge.value.js')
    m = re.search('gauge.set\((.+?)\);', r.text)
    if m:
        found = m.group(1)
        print(datetime.now().strftime("%Y/%m/%dT%H:%M:%S"), found, sep=',')
    time.sleep(10)