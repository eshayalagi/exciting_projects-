import time
from plyer import notification

while True:
    print("pls drink water!")
    notification.notify(
        title="Please drink some water",
        message="You need to drink some water",
        timeout=10
    )
    time.sleep(3600)   # wait for 1 hour
