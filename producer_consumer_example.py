import threading
import time
from threading import Condition

class SharedResource:
    def __init__(self):
        self.value = 0
        self.condition = Condition()  # Condition variable

    def producer_consumer_example(self):
        """Example of producer-consumer using condition variables"""
        def producer():
            with self.condition:
                self.value += 1
                print(f"Producer produced: {self.value}")
                self.condition.notify()

        def consumer():
            with self.condition:
                while self.value == 0:
                    print("Consumer waiting...")
                    self.condition.wait()
                print(f"Consumer consumed: {self.value}")
                self.value = 0

        # Create producer and consumer threads
        producer_thread = threading.Thread(target=producer)
        consumer_thread = threading.Thread(target=consumer)
        
        consumer_thread.start()
        time.sleep(0.5)  # Give consumer time to start waiting
        producer_thread.start()

def main():
    # Create shared resource
    resource = SharedResource()
    
    print("\n=== Producer-Consumer Example ===")
    resource.producer_consumer_example()

if __name__ == "__main__":
    main() 