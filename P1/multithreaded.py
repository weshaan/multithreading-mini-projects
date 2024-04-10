# import os
# os.getcwd()

import random as r,threading, string as s,shutil,os, time
inputDir="sampleDirectory"
totalFiles=5
fileSize=5

try:
    shutil.rmtree("./%s/"%(inputDir))
    os.mkdir(inputDir)
except:
    os.mkdir(inputDir)

def task(filename):
    itr=50
    filename="./%s/%s"%(inputDir,filename)
    while(True):
        fp=open(filename,"a")
        for j in range(itr):
            for k in range(itr):
                string= ''.join(r.sample(s.ascii_letters,50))
                fp.write(string+"\n"+string+"\n"+string+"\n"+string+"\n"+string+"\n")
        fp.close()
        if os.path.getsize(filename)>=fileSize:
               break
    return None
  
startTime=time.time()
nof_threads=5
activeThreads=threading.activeCount()

print("Execution has started!")
for i in range(totalFiles):
    filename="test%d.txt"%(i+1)
    command=filename
    t=threading.Thread(target=task,args=(command,))
    t.start()

    print("file %sth created!"%(filename))
    while True:
        if threading.activeCount()-activeThreads+1<=nof_threads:
            break
        time.sleep(1)

while True:
    if threading.activeCount()==activeThreads:
        break
    else:
        print("Thread running (%d left)"%(threading.activeCount()-activeThreads))
        time.sleep(1)
print("all threads have ended now")
print("execution finidhed!")
print("total time taken is %f seconds"%(round(time.time()-startTime,4)))