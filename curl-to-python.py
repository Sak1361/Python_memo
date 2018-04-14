#curl -X POST -u 53f2651e-a0f3-4f56-b80b-48be1a01ea3c:fwrQj8UqHIZi
#  --header "Content-Type: audio/flac"
#  --data-binary @/home/fuchigami/Downloads/voice.flac 
# "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true&model=ja-JP_BroadbandModel"

import os.path
place = input("where is file(Absolute):")#/home/fuchigami/Downloads/voice.flac
lang = input("select language:")
if(lang=="japanese"):
    lang = "ja-JP_BroadbandModel"
elif(lang=="english"):
    lang = "en-US_BroadbandModel"
else:
    print("write correctry!")
    exit()

cmd = 'curl -X POST -u 53f2651e-a0f3-4f56-b80b-48be1a01ea3c:fwrQj8UqHIZi\
 --header "Content-Type: audio/flac"\
 --data-binary @{0}\
 "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true&model=\
{1}"'.format(place,lang)

req = os.system(cmd)
print(req)