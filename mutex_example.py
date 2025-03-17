import threading
import time
from threading import Lock

class SharedResource:
    def __init__(self):
        self.value = 0
        self.lock = Lock()  # Mutex lock

    def increment_with_mutex(self):
        """Example of using mutex lock"""
        with self.lock:
            current = self.value
            time.sleep(0.1)  # Simulate some work
            self.value = current + 1
            print(f"Value after mutex increment: {self.value}")

def main():
    # Create shared resource
    resource = SharedResource()
    
    print("\n=== Mutex Lock Example ===")
    threads = []
    for _ in range(3):
        t = threading.Thread(target=resource.increment_with_mutex)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main() 