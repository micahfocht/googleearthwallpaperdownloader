from urllib.request import urlretrieve
import os
import threading

count = 0
threads = []
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def download(url,path):
    try:
        urlretrieve(url,path)
        print (bcolors.OKCYAN + "Downloaded: " + url + bcolors.ENDC)
    except Exception as e:
        print (bcolors.WARNING + "Unable to download: " + url + bcolors.ENDC)

while (count<20000):
    count +=1 
    url= "https://www.gstatic.com/prettyearth/assets/full/"
    path = "Wallpapers/"
    if not os.path.exists(path):
        os.mkdir(path)
    url = url + f"{count:04}" + ".jpg"
    path = path + f"{count:04}" + ".jpg"
    if os.path.isfile(path) is False:
        if(len(threads) > 100):
            for x in range(10):
                threads.pop().join()
        thread = threading.Thread(target=download, args=(url, path))
        thread.start()
        threads.append(thread)

for thread in threads:
    thread.join()

