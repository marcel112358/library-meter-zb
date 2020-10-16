import os
import re
import requests
import schedule
from datetime import datetime
import time
import functools
from pathlib import Path


DATA_FOLDER = Path('zb-library-data')


def catch_exceptions(cancel_on_failure=False):
    def catch_exceptions_decorator(job_func):
        @functools.wraps(job_func)
        def wrapper(*args, **kwargs):
            try:
                return job_func(*args, **kwargs)
            except:
                import traceback
                print(traceback.format_exc())
                if cancel_on_failure:
                    return schedule.CancelJob
        return wrapper
    return catch_exceptions_decorator


@catch_exceptions(cancel_on_failure=False)
def job():
    r = requests.get('https://www.zb.uzh.ch/themes/zb/assets/js/gauge.value.js')

    m = re.search('gauge.set\((.+?)\);', r.text)
    if m:
        found = m.group(1)

        file = DATA_FOLDER / f'{datetime.now().strftime("%Y%m%d")}.txt'

        if not DATA_FOLDER.exists():
            DATA_FOLDER.mkdir()

        if not file.exists():
            f = open(DATA_FOLDER / f'{datetime.now().strftime("%Y%m%d")}.txt', 'a')
            f.write(f'datetime,volume\n')
            f.close()

        f = open(DATA_FOLDER / f'{datetime.now().strftime("%Y%m%d")}.txt', 'a')
        f.write(f'{datetime.now().strftime("%Y/%m/%dT%H:%M:%S")},{found}\n')
        f.close()


if __name__ == '__main__':
    for hour in range(8, 20):
        for minute in range(0, 60):
            execution_time = f'{hour:02d}:{minute:02d}'
            schedule.every().monday.at(execution_time).do(job)
            schedule.every().tuesday.at(execution_time).do(job)
            schedule.every().wednesday.at(execution_time).do(job)
            schedule.every().thursday.at(execution_time).do(job)
            schedule.every().friday.at(execution_time).do(job)

    for hour in range(8, 17):
        for minute in range(0, 60):
            execution_time = f'{hour:02d}:{minute:02d}'
            schedule.every().saturday.at(execution_time).do(job)
            schedule.every().sunday.at(execution_time).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)