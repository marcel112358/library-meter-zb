import requests
import re
from datetime import datetime

r = requests.get('https://www.zb.uzh.ch/themes/zb/assets/js/gauge.value.js')

m = re.search('gauge.set\((.+?)\);', r.text)
if m:
    found = m.group(1)
    print(datetime.now().strftime("%Y/%m/%dT%H:%M:%S"), found, sep=',')