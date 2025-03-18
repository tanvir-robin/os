import threading


class TickTock:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()  # Lock for synchronization

    def increment(self, use_lock=False):
        if use_lock:
            with self.lock:  # Ensure atomic increments
                self.count += 1
        else:
            self.count += 1  # Unsynchronized increment

# Main function


def main(use_lock=False, num_threads=2, num_iterations=100000):
    tt = TickTock()

    def run():
        for _ in range(num_iterations):
            tt.increment(use_lock)

    threads = [threading.Thread(target=run) for _ in range(num_threads)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Count :", tt.count)


if __name__ == "__main__":
    # Run different cases
    print("Case 1: (Thread not started)")
    print("Count : 0")  # Simulate Case 1

    print("\nCase 2: (Single Thread, No Race Condition)")
    main(use_lock=True, num_threads=1, num_iterations=10000)

    print("\nCase 3: (Multiple Threads, No Lock - Race Condition)")
    main(use_lock=False, num_threads=2, num_iterations=100000)

    print("\nCase 4: (Multiple Threads, Proper Synchronization)")
    main(use_lock=True, num_threads=2, num_iterations=100000)
