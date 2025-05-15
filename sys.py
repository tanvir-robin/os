import os
import sys
import time

def main():
    print(f"🔵 Parent Process ID: {os.getpid()}")
    
    pid = os.fork()  # Create a child process

    if pid == 0:
        # Inside child process
        print(f"🧒 Child Process ID: {os.getpid()} (Parent: {os.getppid()})")
        print("⏳ Child sleeping for 10 seconds before execv... (Check Activity Monitor)")
        time.sleep(10)  # Wait so you can inspect the process
        print("🔁 Now replacing child process with child_script.py using execv()")
        os.execv(sys.executable, ['python', 'child.py'])  # Replace the process
    else:
        # Inside parent process
        print(f"👨 Parent waiting for child PID: {pid}")
        print("⏳ Parent sleeping for 15 seconds... (Check Activity Monitor)")
        time.sleep(15)
        os.wait()  # Wait for the child process to finish
        print("✅ Parent resumes after child exits.")

if __name__ == "__main__":
    main()
