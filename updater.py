#the following module downloads and updates wallpaper from Pexel

import arg
import os
import time
import requests 
import random
import ctypes
import platform


#argparse: Since this is a CLI app, we need to pass arguments to our app using this module
#os: We need this module to find the current working directory and full path of our wallpaper
#time: This module will be used to call our function every given minutes and also to use sleep() method
#random: To generate random number , so we can make random request url every time
#requests: We are using this module to make http request and to download the wallpaper
#ctypes: This module is to call foreign function in Python. It provides C compatible data types and allows to call DLL and shared libraries. We need this to call SystemParametersInfoW to change our wallpaper
#platform: We are using this inbuilt module to know the operating system where this code will run. Based on that we will call system function to change the wallpaper


def get_wallpaper():
    #Random number
    num = random.randint(1,99)

    #API Key
    payload = {'Authorization': 'uNerXMTjOQnoC9gnnM5HucFYwimg00wybn5IhDa244fyw24XV7SUJaz4'}

    #Query
    query = 'flower'

    #URL for Pexels
    url = 'https://api.pexels.com/v1/search?per_page=1&page=' + str(num) + '&query=' + query

    #Get response
    res = requests.get(url, headers=payload)

    #Check for response
    if res.status_code == 200:
        img_url = res.json.get('photos')[0]['src']['original']
        
        #Make request to get the image from url
        img = requests.get(img_url)

        #Write and save image locally with 'temp.jgp'
        with open('temp.jpg', 'wb') as f:
            f.write(img.content)

    else:
        print('error in making request')

def set_wallpaper():
    get_wallpaper()
    path = os.getcwd + '\\temp.jpg'
    ctypes.windll.user32.SystemParmetersInfoW(20,0,path,0)

if __name__ == "__main__":
        set_wallpaper()



