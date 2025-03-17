import threading
import time

def worker():
    thread_id = threading.get_ident()
    for i in range(5):
        print(f"Thread {thread_id} is running...")
        time.sleep(1)

t= threading.Thread(target=worker)
t.start()

t.join()

print("Thread is Finished")
