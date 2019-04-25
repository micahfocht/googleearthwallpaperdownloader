import wget
import os
count = 0
while (count<10000):
    count +=1 
    url= "https://www.gstatic.com/prettyearth/assets/full/"
    path = "/Users/micahfocht/Documents/Wallpapers/"
    if count > 999:
        number = str(count)
    elif count < 10:
        number = "000" + str(count)
    elif count < 100:
        number = "00" + str(count)
    elif count < 1000:
        number = "0" + str(count)
    url = url + number + ".jpg"
    path = path + number + ".jpg"
    if os.path.isfile(path) is False:
        try:
                wget.download(url, path)
        except:
           print("Error. File " + number + " Does not exist")
