import threading
import time
import queue

class SharedResource:
    def __init__(self):
        self.queue = queue.Queue()  # Message passing example

    def message_passing_example(self):
        """Example of message passing using queue"""
        def sender():
            for i in range(3):
                self.queue.put(f"Message {i}")
                print(f"Sent: Message {i}")
                time.sleep(0.5)

        def receiver():
            while True:
                try:
                    message = self.queue.get(timeout=2)
                    print(f"Received: {message}")
                except queue.Empty:
                    print("No more messages")
                    break

        # Create sender and receiver threads
        sender_thread = threading.Thread(target=sender)
        receiver_thread = threading.Thread(target=receiver)
        
        sender_thread.start()
        receiver_thread.start()

def main():
    # Create shared resource
    resource = SharedResource()
    
    print("\n=== Message Passing Example ===")
    resource.message_passing_example()

if __name__ == "__main__":
    main() 