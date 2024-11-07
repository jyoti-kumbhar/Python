import threading
import time

#define a function1
def function1():
    start_time = time.time()   #start time
    time.sleep(2)              #sleep time
    end_time = time.time()     #end time
    print("FUNCTION 1\n")      #print statement

    #excution time
    print( f"Excution time {end_time - start_time:0.2f}\n")

#define a function2
def function2():
    start_time = time.time()   #start time
    time.sleep(3)              #sleep time
    end_time = time.time()     #end time
    print("FUNCTION 2\n")      #print statement

    #excution time 
    print( f"Excution time {end_time - start_time:0.2f}\n")



#create two threads
thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)
    
#start the threads   
thread1.start()
thread2.start()

#joining the threads 
thread1.join()
thread2.join()
