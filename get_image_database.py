# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import thread


def download_imag(number):
    global img_flag,succes_flag
    print('save numner: ' + str(number) + ' img, img_flag = ' + str(img_flag))
    #set url
    referer_url = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=' + str(number) + '&request_locale=ja'
    img_url = 'https://www.db.yugioh-card.com/yugiohdb/get_image.action?type=2&cid=' + str(number) + '&ciid='+str(img_flag)+'&request_locale=ja'
    print(img_url)
    #set request
    s = requests.Session()
    s.headers.update({'referer': referer_url})
    r = s.get(img_url)
    #try search error message
    soup = BeautifulSoup(r.content,"html.parser")
    noscript = soup.find_all('noscript')
    #set error message
    try:
        message = noscript[0].string
    except:
        message = 'aava'
    #if no error message, save img
    if(message[0] != 'J'):
        img_flag+=1
        if(number<10000):
            number = "%05d" % int(number)
        filename = "img/" + str(number) + '_' + str(img_flag) + ".jpg"
        pic_out = file(filename,'w')
        pic_out.write(r.content)
        pic_out.close()
        time.sleep(1)
    else:
        print("ok")
        succes_flag = False
        img_flag = 1

def download_all(number):
    global succes_flag
    succes_flag = True
    while(succes_flag):
        download_imag(number)

if __name__ == "__main__":
    succes_flag = True
    img_flag = 1
    #number range 4000~13500
    for i in range(4007,13500):
        download_all(i)
    

