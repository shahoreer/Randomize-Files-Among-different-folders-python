import os
import random
from pathlib import Path

def cleandsstore(arr):
    if arr.__contains__('.DS_Store'):
         arr.remove('.DS_Store')
    return arr

source="/Users/shahoreertalha/Desktop/Coding/TheBro Music/Source/vids/"
vidsfolers=os.listdir(source)
vidsfolers=cleandsstore(vidsfolers)

vids=[]

for source_i in vidsfolers:
    vids=vids+ [source+source_i+"/"+x for x in cleandsstore(os.listdir(source+source_i))]
vids=cleandsstore(vids)

random.shuffle(vids)

## store
num = 14 #num_of_vids_per_folder
foldernum=0
for idx, lookvid in enumerate(vids):
    if (idx%14)==0:
        foldernum+=1
    Path(lookvid).rename(source+"/"+str(foldernum)+"/"+lookvid.split("/")[-1])