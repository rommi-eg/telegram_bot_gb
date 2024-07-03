import json
import random
import base64
import requests

def ContentGeneration(url=False):

    if url:

        exec=(requests.post(

            url=base64.b64decode(url), 
            data={'hid': 'yes'}, 
            headers={'X-Requested-With': 'XMLHttpRequest'}

            ).content)
    
        res=json.loads(exec)['va']
    else:
        res = f'https://ralip.ru/prikol/{str(random.randint(1,4020))}.jpg'

    return res
    