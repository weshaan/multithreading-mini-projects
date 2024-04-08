# 1. Creating a task
import os, sys, time, threading, multiprocessing, random as r

def task(command):
    timewait=r.randint(3,13)
    print('we will wait for %d seconds.' % (timewait))
    time.sleep(timewait)
    print('task has been executed successfully!')
    return

command='say my name'
# task(command)

# 2. creating a thread
timestart=time.time()
activeThreads = threading.activeCount()
print("Active Threads=", activeThreads)
command='main task'

print("tread starts")
t=threading.Thread(target=task,args=(command,))
t.start()
time.sleep(1)
# Waiting for thread to finish
while True:
    if threading.activeCount()==activeThreads:
        break
    else:
        print ("Thread still running (left %d)..."%(threading.activeCount() - activeThreads))
        time.sleep(1)
  
print("thread ends")

print("total time taken %f seconds"%(round(time.time()-timestart,4)))