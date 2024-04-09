# import os
# os.getcwd()

import random as r, string as s, shutil, os, time

inputDIR='InputDirectory'
totalFiles=5
fileSize=5

try:
    shutil.rmtree("./%s/"%(inputDIR))
    os.mkdir(inputDIR)
except:
    os.mkdir(inputDIR)

def task(filename):
    itr=50
    filename="./%s/%s"%(inputDIR,filename)
    while True:
        fp=open(filename,"a")
        for j in range(itr):
            for k in range(itr):
                string=" ".join(r.sample(s.ascii_letters,50))
                fp.write(string + "\n" + string + "\n" + string + "\n" + string + "\n" + string + "\n")
        fp.close()
        if os.path.getsize(filename)>=fileSize:
            break
    return None

startTime=time.time()
print("Execution has started!")
for i in range(totalFiles):
    filename="test%d.txt"%(i+1)
    task(filename)
    if i%5==0:
        print("File %s created!"%(filename))
print("\nTotal time taken is %f seconds"%(round(time.time()-startTime,4)))
print("Ending execution.")
