import requests
import os
from math import trunc

url = "http://ftp.uo.edu.cu/Windows/IDE%20Programaci%C3%B3n/Visual_Basic_6/Portable%20-%20Microsoft%20Visual%20Basic%206.0%20-%20SPANISH.exe"

chunk_size = 64 * 1024

response = requests.get(url, stream = True)

file = open("./vscode.exe", "wb")

total = int(response.headers["Content-Length"])

for chunk in response.iter_content(chunk_size):
    
    file.write(chunk)

    current = os.path.getsize("./vscode.exe")

    done = ((current / total) * 100)

    progress_bar = "{0}{1} {2}\n".format("█" * trunc(done / 5), "▒" * trunc((100 - done) / 5), trunc(done), "%")

    print(progress_bar)
