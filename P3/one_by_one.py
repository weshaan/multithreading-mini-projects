# import os
# os.getcwd()

import shutil, os, time
from PIL import Image
inputDir='inputDirectory'
outputDir = 'outputDirectory'
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
totalFiles=5;
print("Starting execution!")
for i in range(totalFiles):
     filename="image%d.jpg"%(i+1)
     task(filename)
     if i%5==0:
         print("%s processed so far..."%(filename))

print("\nTotal time taken is: %f seconds"%(round(time.time()-startTime)))
print("Execution is finished")
