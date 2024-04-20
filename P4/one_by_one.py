# import os
# os.getcwd()

import shutil, os, time
inputDir='inputDirectory'
outputDir = 'outputDirectory'
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
totalFiles=5;
print("Starting execution!")
for i in range(totalFiles):
     filename="test%d.txt"%(i+1)
     task(filename)
     if i%5==0:
         print("%s processed so far..."%(filename))

print("\nTotal time taken is: %f seconds"%(round(time.time()-startTime)))
print("Execution is finished")
