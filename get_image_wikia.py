# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def download_imag(number):
    print('Try to download: ' + str(number))
    #set url
    img_url = 'http://yugioh.wikia.com/wiki/' + str(number)

    try:
        #parse url and get img url
        s = requests.Session()
        r = s.get(img_url)
        soup = BeautifulSoup(r.content,"html.parser")
        get_class = soup.find(attrs={'class' :'cardtable-cardimage'})
        download_url = get_class.findAll('img')[0].get('src')

        print('start download')

        #download image
        download_s = requests.Session()
        download_r = download_s.get(download_url)
        filename = "img/" + str(number) + ".jpg"
        pic_out = file(filename,'w')
        pic_out.write(download_r.content)
        pic_out.close()
        
        print('download complete')

    except:
        print('something wrong')
    
while (True):
    get_input = raw_input(">>> Input: ")
    download_imag(get_input)