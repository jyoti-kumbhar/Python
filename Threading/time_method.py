import threading
import time

#define a function
def function(thread_name , sleep_time):
    print(f"{thread_name} starting\n") #print statement
    
    start_time = time.time()   #start time
    time.sleep(sleep_time)     #sleep time
    end_time = time.time()     #end time

    #print statement
    print(f"{thread_name} finished after {end_time - start_time:0.2f} seconds\n")

#create two threads
thread1 = threading.Thread(target=function, args = ("Thread 1" , 2))
thread2 = threading.Thread(target=function, args = ("Thread 2" , 4))
    
#start the threads   
thread1.start()
thread2.start()

#joining the threads 
thread1.join()
thread2.join()
