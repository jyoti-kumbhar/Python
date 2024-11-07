#DAEMON THREADS
import threading
import time

def daemon_function():
    
    count = 10
    while True:
        print(f"Daemon thread: {count}\n")
        count -= 1
        time.sleep(1)  # Simulate some work

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_function, daemon=True)
daemon_thread.start()

# Main thread continues
print("Main thread started\n")
time.sleep(11)  # Main thread does some work
print("Main thread finished\n")



