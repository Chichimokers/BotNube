from todus3.main import register

from todus3 import client

#Obtener token con numero de telefono
def obtaintoken(telefono):

    clienteTodus  = client.ToDusClient()

    password = register(clienteTodus, telefono)

    print(password)

    _token = clienteTodus.login(telefono, password)

    return _token

    pass
#obtener token con password
def obtaintokenFrompassword(telefono,password):

    clienteTodus = client.ToDusClient()

    token = clienteTodus.login(telefono, password)

    return token
    
    pass
#passwordmami = "dow6R722U91fbCuGsfxzE6M-tMptXncvAReT4PQUP97P5yVgpKP41ZKHskhuYR0eMy8pwQHwMOpUYsfujL2DJtzDYpbKlg=="
tokenfinal = obtaintoken("5356239491")
#passpapi = "TFRYOclk_eKCKL-Qi9chFffGAy4GmsqKRJiwufbfu3VwOtNbrKCeRLxKSHm0X9XzoRe8Bjqr-oZbn6JCxGIEf7VABcLIctA="
#password = str

#tokenfinal = obtaintokenFrompassword("5355366583",passpapi)
#DQHRK3PkywS8D2GC8CzY-c3ibdqYLFU4YtJ8DCQtrEFuC8_y110Ymf0Il6ax7eV4pdI3Tw7rIk4PMyNiBekTSKOuIr63uw==
print(tokenfinal)