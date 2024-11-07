#DAEMON THREADS
import threading
import time

def daemon_function():
    
    count = 10
    while True:
        print(f"Rocket launch in: {count}\n")
        count -= 1
        time.sleep(1)  # Simulate some work

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_function, daemon=True)
daemon_thread.start()

# Main thread continues
print("Rocket Launched started\n")
time.sleep(11)  # Main thread does some work
print("Roccket Lauched finished\n")



