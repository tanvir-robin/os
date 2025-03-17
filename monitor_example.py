import threading
import time
from threading import Condition, Lock

class Monitor:
    def __init__(self):
        self.lock = Lock()
        self.condition = Condition(self.lock)
        self.value = 0
        self.is_empty = True

    def produce(self):
        """Producer method using monitor pattern"""
        with self.condition:
            while not self.is_empty:
                print("Buffer full, producer waiting...")
                self.condition.wait()
            
            self.value += 1
            self.is_empty = False
            print(f"Produced: {self.value}")
            self.condition.notify()

    def consume(self):
        """Consumer method using monitor pattern"""
        with self.condition:
            while self.is_empty:
                print("Buffer empty, consumer waiting...")
                self.condition.wait()
            
            print(f"Consumed: {self.value}")
            self.is_empty = True
            self.condition.notify()

def main():
    monitor = Monitor()
    
    print("\n=== Monitor Example (Producer-Consumer) ===")
    
    # Create producer and consumer threads
    producer = threading.Thread(target=monitor.produce)
    consumer = threading.Thread(target=monitor.consume)
    
    # Start consumer first to demonstrate waiting
    consumer.start()
    time.sleep(0.5)  # Give consumer time to start waiting
    producer.start()
    
    # Wait for threads to complete
    producer.join()
    consumer.join()

if __name__ == "__main__":
    main() 