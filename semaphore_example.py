import threading
import time
from threading import Semaphore

class SharedResource:
    def __init__(self):
        self.value = 0
        self.semaphore = Semaphore(1)  # Binary semaphore

    def increment_with_semaphore(self):
        """Example of using semaphore"""
        with self.semaphore:
            current = self.value
            time.sleep(0.1)  # Simulate some work
            self.value = current + 1
            print(f"Value after semaphore increment: {self.value}")

def main():
    # Create shared resource
    resource = SharedResource()
    
    print("\n=== Semaphore Example ===")
    threads = []
    for _ in range(3):
        t = threading.Thread(target=resource.increment_with_semaphore)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main() 