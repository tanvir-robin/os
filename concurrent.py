import concurrent.futures
import time

def task(name):
    print(f"Task {name} started...")
    time.sleep(2)  
    print(f"Task {name} completed!")
    return f"Result from Task {name}"

# Using ThreadPoolExecutor for concurrency
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(1, 6)]  

    for future in concurrent.futures.as_completed(futures):
        print(future.result())  

print("All tasks completed concurrently!")
