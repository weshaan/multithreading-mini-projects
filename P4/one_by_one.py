# import os
# os.getcwd()

import shutil, os, time
import cv2
inputDir='inputDirectory'
outputDir = 'outputDirectory'
try:
    shutil.rmtree("./%s/"%(outputDir))
    os.mkdir(outputDir)
except:
    os.mkdir(outputDir)

def task(filename,filename2):
    inFile="./%s/%s"%(inputDir,filename)
    outFile="./%s/%s"%(outputDir,filename2)
    vid_cap=cv2.VideoCapture(inFile)
    f_width=int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Get the video properties
    f_height=int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps=int(vid_cap.get(cv2.CAP_PROP_FPS))   
    # Define codec and create VideoWriter object
    fourcc=cv2.VideoWriter_fourcc(*'mp4v') # For .mp4 format, use 'mp4v' codec
    out=cv2.VideoWriter(outFile,fourcc,fps,(f_width,f_height),isColor=False)   
    while vid_cap.isOpened(): # Read until video is completed
        ret, frame = vid_cap.read()
        if not ret:
            break
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # Convert frame to grayscale
        out.write(gray_frame)
    # Release video objects
    vid_cap.release()
    out.release()
    return None
    
startTime=time.time()
totalFiles=5;
print("Starting execution!")
for i in range(totalFiles):
     filename="image%d.wmv"%(i+1)
     filename2="image%d.mp4"%(i+1)
     task(filename,filename2)
     if i%5==0:
         print("%s processed so far..."%(filename))

print("\nTotal time taken is: %f seconds"%(round(time.time()-startTime)))
print("Execution is finished")
