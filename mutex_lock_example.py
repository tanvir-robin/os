import threading
import time
from threading import Lock

class SharedResource:
    def __init__(self):
        self.value = 0
        self.lock = Lock()  # Mutex lock

    def increment_with_mutex(self):
        """Example of using mutex lock to fix race condition"""
        with self.lock:  # Enter critical section
            current = self.value
            time.sleep(0.1)  # Simulate some work
            self.value = current + 1
            print(f"Value after mutex increment: {self.value}")
        # Exit critical section

    def increment_without_mutex(self):
        """Demonstrates race condition without mutex"""
        current = self.value
        time.sleep(0.1)  # Simulate some work
        self.value = current + 1
        print(f"Value without mutex: {self.value}")

def main():
    resource = SharedResource()
    
    print("\n=== Mutex Lock Example ===")
    print("Running with mutex lock (correct synchronization):")
    threads = []
    for _ in range(3):
        t = threading.Thread(target=resource.increment_with_mutex)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"\nFinal value with mutex: {resource.value}")
    print("Note: The value should always be 3!")

if __name__ == "__main__":
    main() 