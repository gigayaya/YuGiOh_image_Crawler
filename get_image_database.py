# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import thread

def download_imag(number):
    print('save numner: ' + str(number) + ' img')
    #set url
    referer_url = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=' + str(number) + '&request_locale=ja'
    img_url = 'https://www.db.yugioh-card.com/yugiohdb/get_image.action?type=2&cid=' + str(number) + '&ciid=1&request_locale=ja'
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
        filename = "img/" + str(number) + ".jpg"
        pic_out = file(filename,'w')
        pic_out.write(r.content)
        pic_out.close()
        time.sleep(1)


def thread_task(string, rrange, *args):
    print("round:" + str(rrange))
    end = rrange + 1
    rrange = rrange * 500
    end = end * 500
    for index in range(rrange,end):
        download_imag(index)

if __name__ == "__main__":
    #number range 4000~13500
    for i in range(8,27):
        time.sleep(1)
        thread.start_new_thread(thread_task, ("ThreadFun", i))
    while(True):
        print 'MainThread {0}'.format(thread.get_ident())
        time.sleep(1)