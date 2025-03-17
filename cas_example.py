import threading
import time
import ctypes

class AtomicInteger:
    def __init__(self, value=0):
        self._value = ctypes.c_int(value)
        self._lock = threading.Lock()

    def get(self):
        """Get the current value"""
        return self._value.value

    def compare_and_swap(self, expected_value, new_value):
        """
        Atomic compare and swap operation
        Returns True if successful, False otherwise
        """
        with self._lock:
            if self._value.value == expected_value:
                self._value.value = new_value
                return True
            return False

    def increment(self):
        """Atomic increment operation using CAS"""
        while True:
            current = self.get()
            if self.compare_and_swap(current, current + 1):
                return current + 1

    def decrement(self):
        """Atomic decrement operation using CAS"""
        while True:
            current = self.get()
            if self.compare_and_swap(current, current - 1):
                return current - 1

def worker(atomic_int, operation):
    """Worker function to demonstrate CAS operations"""
    if operation == "increment":
        value = atomic_int.increment()
        print(f"Thread {threading.current_thread().name} incremented to: {value}")
    else:
        value = atomic_int.decrement()
        print(f"Thread {threading.current_thread().name} decremented to: {value}")
    time.sleep(0.1)

def main():
    atomic_int = AtomicInteger(0)
    
    print("\n=== Compare-and-Swap (CAS) Example ===")
    print("Initial value:", atomic_int.get())
    
    # Create multiple threads to demonstrate CAS operations
    threads = []
    
    # Create increment threads
    for _ in range(3):
        t = threading.Thread(target=worker, args=(atomic_int, "increment"))
        threads.append(t)
        t.start()
    
    # Create decrement threads
    for _ in range(2):
        t = threading.Thread(target=worker, args=(atomic_int, "decrement"))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    print(f"\nFinal value: {atomic_int.get()}")
    print("Note: The value should be 1 (3 increments - 2 decrements)")

if __name__ == "__main__":
    main() 