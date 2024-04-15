# import os
# os.getcwd()

import shutil, os, time, threading
inputDir='sampleDirectory'
outputDir = 'casedDirectory'
try:
    shutil.rmtree("./%s/"%(outputDir))
    os.mkdir(outputDir)
except:
    os.mkdir(outputDir)

def task(filename):
    inFile="./%s/%s"%(inputDir, filename)
    outFile="./%s/%s"%(outputDir, filename)
    inFile=open(inFile)
    outFile=open(outFile,"w")
    for line in inFile:
        outFile.write(line.upper())
    inFile.close()
    outFile.close()
    return None
    
startTime=time.time()
nofThreads=5
totalFiles=5
activeThreads=threading.activeCount()
print("Execution has started!")

for i in range(totalFiles):
    filename="test%d.txt"%(i+1)
    command=filename
    t=threading.Thread(target=task, args=(command,))
    t.start()

    print("File %s created!"%(filename))
    while True:
        if threading.activeCount()-activeThreads<=nofThreads:
            break
        time.sleep(1)

while True:
    if threading.activeCount()==activeThreads:
        break
    else:
        print("Thread number %d running.."%(threading.activeCount() - activeThreads))
        time.sleep(1)

print("All threads have runned. Execution finished!")
print("Total time taken: %f seconds"%(round(time.time()-startTime,4)))