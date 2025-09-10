import schedule
import time
import threading
import datetime

def __task():
    date = datetime.datetime.now()
    print(f"schedule task...{date}\n")

def __worker():
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule.every(10).seconds.do(__task)
schedule_thread = threading.Thread(target=__worker, daemon=True)

def start():
    schedule_thread.start()
