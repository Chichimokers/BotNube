import os 
from cleanname import CleanName
paths = os.path.dirname(os.path.abspath(__file__))
def EstasPermitiado(update):

    whitelist = open(paths+"/whitelist.txt","r")

    Lista = whitelist.readlines()

    for allowed in Lista:

        limpio = CleanName(allowed)

        if(update.message.chat.username == limpio):

            return True

    
    return False   

    pass
def AreAdmin(update):

    adminlist  = open(paths+"/admin.txt","r")

    Lista  = adminlist.readlines()

    for admins in Lista:
        
        if(update.message.chat.username == admins):

            return True

        else:

            return False
    pass
