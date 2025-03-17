import threading
import time

class SharedResource:
    def __init__(self):
        self.value = 0
        self.race_condition_value = 0

    def increment_without_sync(self):
        """Demonstrates race condition"""
        current = self.race_condition_value
        time.sleep(0.1)  # Simulate some work
        self.race_condition_value = current + 1
        print(f"Race condition value: {self.race_condition_value}")

    def increment_with_sync(self):
        """Demonstrates correct synchronization"""
        current = self.value
        time.sleep(0.1)  # Simulate some work
        self.value = current + 1
        print(f"Synchronized value: {self.value}")

def main():
    resource = SharedResource()
    
    print("\n=== Race Condition Example ===")
    print("Running without synchronization (race condition):")
    threads = []
    for _ in range(3):
        t = threading.Thread(target=resource.increment_without_sync)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"\nFinal race condition value: {resource.race_condition_value}")
    print("Note: The value might not be 3 due to race condition!")

if __name__ == "__main__":
    main() 