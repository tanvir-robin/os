from multiprocessing import Process
import time
import os

def worker():
    while True:
        print(f"Process ID: {os.getpid()} is running...")
        time.sleep(1)

if __name__ == "__main__":
    p=Process(target=worker)
    p.start()
    
    time.sleep(5)
    p.terminate()
    p.join()
    print("Process is terminated")
