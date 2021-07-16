import requests
import re
import os
import time

"""
下载完毕，我们现在看一下图片，就不一一看了，谢谢大家观看。
"""

def kings():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    respones = requests.get(url='https://pvp.qq.com/web201605/herolist.shtml', headers=headers)
    respones.encoding = respones.apparent_encoding
    #print(respoes.text)
    hero_url = re.findall(r'href="(herodetail/.*?.shtml)" target="_blank"', respones.text)
    hero_names = re.findall(r'alt="(.*?)">', respones.text)

    hero_names = hero_names[:93]
    hero_url = hero_url[:93]
    # print(hero_names)
    for j in hero_names:
        s = hero_names.index(j)
        hero_name = j
        url = 'https://pvp.qq.com/web201605/'+hero_url[s]
        print(hero_name)
        #print(hero_url)
        time.sleep(1)
        imgurl(url, hero_name)

def imgurl(url, hero_name):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    respones = requests.get(url=url, headers=headers)
    respones.encoding = respones.apparent_encoding
    # print(respoes.text)
    names = re.findall(r'data-imgname="(.*?)"', respones.text)
    img = re.findall(r'(//game.gtimg.cn/.*?)1.jpg', respones.text)
    img_name = names[0].split('|')
    print(img_name)
    # print(img[0])

    path = "D:\\pycharm\\潮汐\\王者荣耀皮肤\\" + hero_name
    if not os.path.exists(path):
        os.mkdir(path)

    for i in img_name:
        print(i)
        img_url = 'http:' + img[0] + str(img_name.index(i)+1) + '.jpg'
        print(img_url)
        responess = requests.get(url=img_url, headers=headers).content
        with open(path + "\\" + i + ".jpg", mode="wb") as f:
            f.write(responess)
            print(i + "下载完成")
            time.sleep(1)

if __name__ == "__main__":
    kings()
