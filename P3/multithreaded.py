# import os
# os.getcwd()

import shutil, os, time, threading
from PIL import Image
inputDir='sampleDirectory'
outputDir = 'greyedDirectory'
try:
    shutil.rmtree("./%s/"%(outputDir))
    os.mkdir(outputDir)
except:
    os.mkdir(outputDir)

def task(filename):
    inFile="./%s"%(inputDir)
    outFile="./%s"%(outputDir)
    image_path=os.path.join(inFile, filename)
    output_path=os.path.join(outFile, filename)
    image = Image.open(image_path)
    grayscale_image = image.convert('L')
    grayscale_image.save(output_path)
    return None
     
startTime=time.time()
nofThreads=5
totalFiles=5
activeThreads=threading.activeCount()
print("Execution has started!")

for i in range(totalFiles):
    filename="image%d.jpg"%(i+1)
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