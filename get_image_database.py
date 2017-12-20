# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import thread


def download_imag(number):
    global img_flag,succes_flag
    print('save numner: ' + str(number) + ' img, img_flag = ' + str(img_flag))

    requests.packages.urllib3.disable_warnings()
    URL = "https://www.db.yugioh-card.com/yugiohdb/card_search.action?request_locale=ja&ope=2&cid=" + str(number)
    res = requests.get(str(URL), verify=False, cookies=None)
    content = res.content
    soup = BeautifulSoup(content.decode('utf-8','ignore'),"html.parser")
    #--parse image enc--
    tmp_soup = str(soup)
    start = tmp_soup.find('&enc')
    image_enc = tmp_soup[start:start+27]
    #-------------------

    #set url
    referer_url = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=' + str(number) + '&request_locale=ja'
    img_url = 'https://www.db.yugioh-card.com/yugiohdb/get_image.action?type=2&cid=' + str(number) + '&ciid='+str(img_flag)+'&request_locale=ja' + image_enc
    print(img_url)
    #set request
    s = requests.Session()
    s.headers.update({'referer': referer_url})
    r = s.get(img_url)
    #try search error message
    soup = BeautifulSoup(r.content,"lxml")
    noscript = soup.find_all('noscript')
    #set error message
    try:
        message = noscript[0].string
    except:
        message = 'aava'
    #if no error message, save img
    if(message[0] != 'J'):
        if(number<10000):
            number = "%05d" % int(number)
        filename = "img/" + str(number) + '_' + str(img_flag) + ".jpg"
        pic_out = file(filename,'w')
        pic_out.write(r.content)
        pic_out.close()
        img_flag+=1
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
    #number range 4007~14000
    for i in range(4007,14000):
        download_all(i)
    

