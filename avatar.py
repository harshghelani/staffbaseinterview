import json
import requests
import os
#Define
head = {'Authorization':'Basic NjE0YTdmZmM3NWFlYjQ3YmM3MzQ0YmVkOllOcEokbkRJXkppZyRwZTFWNWRKfWUtbSFxbjs7K3MzeFZhezU0OWRmQ2xoUlRLTiRCc31NVEV4aHJNM3coSSg='}
paths = os.listdir("avatars")
media_url = 'https://backend.staffbase.com/api/media'
url_set = []
#Uploading the images
for i in range(len(paths)):
  path = paths[i]
  response = requests.post(media_url,headers=head,files={"type":"image","file":open("avatars/{0}".format(path),"r+b")})
  if response.status_code == 200:
    upload_data = json.loads(response.content.decode('utf-8'))
    url_set.append(upload_data['resourceInfo']['url'])
    print("{0}/{1} Uploaded".format(i+1,len(paths)))
  else:
    print("!!ERROR!! in Uploading {0} of {1}".format(i+1,len(paths)))

#Updating Profiles
ids = [path[:-4] for path in paths]
for i in range(len(ids)):
  api_url = 'https://backend.staffbase.com/api/users/{0}'.format(ids[i])
  avatar_update = {"avatar":url_set[i]}
  reset = {"avatar": "None"}
  response = requests.put(api_url,headers=head,json=avatar_update)
  if response.status_code == 200:
    print("{0}/{1} Done".format(i+1,len(ids)))
  else:
    print("!!ERROR!! in Uploading for {0}.".format(ids[i]))
