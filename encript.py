
import json
import base64

from json.decoder import JSONDecoder

import cryptocode

def encriptar(mensjaeaencriptar,username,password):

    final = ""

    jsons = json.loads(mensjaeaencriptar)

    jsons["username"] = username

    jsons["password"] = password    

    jsons = json.encoder.JSONEncoder().encode(jsons)

    jsonstring = JSONDecoder().decode(jsons)

    #final = cryptocode.encrypt(str(jsonstring),"SystemCrahsed404*")
    final = str(jsonstring)

    final = final.encode('ascii')

    final = base64.b64encode(final)

    return final

    pass
def desencriptar(mensajadesencriptar):

    pass