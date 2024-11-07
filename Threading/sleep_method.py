from threading import Thread
from time import sleep


counter = 100

def product(by):
    global counter

    local_counter = counter
    local_counter -= by

    sleep(2)

    counter = local_counter
    print(f'counter={counter}\n')


# create threads
t1 = Thread(target=product, args=(10,))
t2 = Thread(target=product, args=(20,))

# start the threads
t1.start()
t2.start()


# wait for the threads to complete
t1.join()
t2.join()


print(f'The final counter is {counter}\n')                                  
