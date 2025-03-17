import concurrent.futures
import time

def task(name):
    """Example task function"""
    print(f"Task {name} started...")
    time.sleep(1)  # Simulate some work
    print(f"Task {name} completed!")
    return f"Result from Task {name}"

def main():
    print("\n=== ThreadPoolExecutor Example ===")
    
    # Create a thread pool with 3 workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit multiple tasks
        futures = [executor.submit(task, i) for i in range(1, 6)]
        
        # Process completed tasks as they finish
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                print(f"Got result: {result}")
            except Exception as e:
                print(f"Task generated an exception: {e}")
    
    print("\nAll tasks completed!")

if __name__ == "__main__":
    main() 