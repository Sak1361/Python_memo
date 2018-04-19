import requests

headers = {
    'Content-Type': 'audio/flac',
}

params = (
    ('continuous', 'true'),
    ('model', 'ja-JP_BroadbandModel'),
)

path = open('/home/fuchigami/Downloads/voice.flac', 'rb').read()
res = requests.post('https://stream.watsonplatform.net/speech-to-text/api/v1/recognize', headers=headers, params=params, data=path, auth=('53f2651e-a0f3-4f56-b80b-48be1a01ea3c', 'fwrQj8UqHIZi'))

print(res.json())