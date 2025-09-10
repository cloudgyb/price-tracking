import threading

def task():
    print("Task...\n")

_scheduler = threading.Timer(10, task)

def start():
    _scheduler.start()
