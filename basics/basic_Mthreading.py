# 1. create a task
import os,sys,time, threading,multiprocessing, random as r

def task(command):
    timewait=r.randint(3,13)
    print('we will wait for %d seconds.'%(timewait))
    time.sleep(timewait)
    print("task has been executed succeessfully!")
    return
command="what's kept in a mere name?"
# task(command)

# based on time
timestart=time.time()
nof_Threads=10
activeThreads = threading.activeCount()
print("Active Threads=", activeThreads)

for i in range(nof_Threads):
    command=str(i+1)
    print("%sth  Thread is created."%(command))
    t=threading.Thread(target=task,args=(command,))
    t.start()
time.sleep(1)
# Waiting for all the threads to finish
while True:
    if threading.activeCount()==activeThreads:
        break
    else:
        print("Threads running(%d left)..."%(threading.activeCount()))
        time.sleep(1)
print("All threads have ended now!")
print("Total time taken: %f seconds"%(round(time.time()-timestart,4)))        

# based on number of cores
timestart=time.time()
nof_Threads=10
activeThreads = threading.activeCount()
print("Active Threads=", activeThreads)
nof_Cores=multiprocessing.cpu_count() 
print("Number of cores avaiable: ",nof_Cores)  

for i in range(nof_Threads):
    command=str(i+1)
    print("%sth  Thread is created."%(command))
    t=threading.Thread(target=task,args=(command,))
    t.start()
    while True:
        if threading.activeCount()-activeThreads <= nof_Cores:
            break
        time.sleep(1)
time.sleep(1)
# Waiting for all the threads to finish
while True:
    if threading.activeCount()==activeThreads:
        break
    else:
        print("Threads running(%d left)..."%(threading.activeCount()))
        time.sleep(1)
print("All threads have ended now!")
print("Total time taken: %f seconds"%(round(time.time()-timestart,4)))        

