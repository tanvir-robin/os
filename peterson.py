import multiprocessing
import time
import random


class PetersonsAlgorithm:
    def __init__(self):
        self.flag = multiprocessing.Array(
            'i', [0, 0])  # Shared array for flags
        self.turn = multiprocessing.Value(
            'i', 0)       # Shared variable for turn

    def process(self, pid):
        other = 1 - pid  # Get the other process ID
        for _ in range(5):  # Each process runs 5 times
            # Entry Section
            self.flag[pid] = 1
            self.turn.value = other
            while self.flag[other] == 1 and self.turn.value == other:
                pass  # Busy wait

            # Critical Section
            print(f"Process {pid} is entering critical section")
            time.sleep(random.uniform(0.5, 1.5))  # Simulate work
            print(f"Process {pid} is leaving critical section")

            # Exit Section
            self.flag[pid] = 0

            # Remainder Section
            time.sleep(random.uniform(0.5, 1.5))


if __name__ == "__main__":
    peterson = PetersonsAlgorithm()
    p1 = multiprocessing.Process(target=peterson.process, args=(0,))
    p2 = multiprocessing.Process(target=peterson.process, args=(1,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Execution complete")