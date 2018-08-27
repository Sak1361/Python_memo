#curl -X POST -u 53f2651e-a0f3-4f56-b80b-48be1a01ea3c:fwrQj8UqHIZi
#  --header "Content-Type: audio/flac"
#  --data-binary @/home/fuchigami/Downloads/voice.flac 
# "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true&model=ja-JP_BroadbandModel"

import os.path
import sys

path = input("where is file:")#/home/fuchigami/Downloads/voice.flac
#name = os.path.dirname(os.path.abspath(__name__))
#joined_path = os.path.join(name, path)
#data_path = os.path.normpath(joined_path)

while True:
    print("select language number ",end="")
    lang = input("japanese:1 English:2\n")
    if(lang=="1"):
        lang = "ja-JP_BroadbandModel"
        break
    elif(lang=="2"):
        lang = "en-US_BroadbandModel"
        break
    else:
        continue

cmd = 'curl -X POST -u 53f2651e-a0f3-4f56-b80b-48be1a01ea3c:fwrQj8UqHIZi\
 --header "Content-Type: audio/flac"\
 --data-binary @{0}\
 "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true&model=\
{1}" -o result.txt'.format(path,lang)

req = os.system(cmd)
#sys.stdout = open("Speech_to_text.txt","w")

print(req)

data = open("result.txt","r").read()
lines = data.split('\n')

for line in lines:
    print (line)
    
#sys.stdout.close()
#sys.stdout =sys.__stdout__
#open("Speech_to_text.txt","r").read()