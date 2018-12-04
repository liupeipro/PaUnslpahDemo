# _*_ coding: UTF-8 _*_

# Python 图片下载器

import os
import json
import requests

imgHeader = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}


class ImgDownalod:
    # 图片下载器，允许下载单个，也允许下载多个，后期会加入线程及网络优化

    def __init__(self, saveDir):
        # 文件本地保存目录
        self.saveDir = saveDir
        pass

    def download(self, url, fileName):
        # 下载单个图片
        # 2-下载图片
        resp = self.requestImg(url)
        print("resp type = ", type(resp))
        # 文件保存本地
        self.save(resp, fileName)
        pass

    def downloadAll(self, urls):
        # 下载全部链接图片
        print("将要下载", len(urls), "张图片")
        self.saveDir += "/downloads"
        # 1-新建目录
        self.checkDir(self.saveDir)
        os.chdir(self.saveDir)
        for item in urls:
            print("开始下载：url=", item["url"], "，name=", item["name"])
            self.download(item["url"], item["name"])
        pass

    def save(self, jsonObj, fileName):
        # 保存文件
        print("保存文件", fileName)
        with open(fileName, "wb") as f:
            f.write(jsonObj)

    def requestImg(self, url):
        # 网络请求图片，返回 resp.text
        # page = requests.Session
        # page.headers = imgHeader
        resp = requests.get(url, headers=imgHeader)
        print("url = ", resp.url)
        return resp.content

    def checkDir(self, dir):
        print("checkDir dir = ", dir)
        isExists = os.path.exists(dir)
        if not isExists:
            os.makedirs(dir)
            print("新建名为", dir, "的文件夹")
        else:
            print(dir, "文件已存在，无需新建")
            self.deleteDir(dir)

    def deleteDir(self, path):
        if os.path.exists(path):
            if os.path.isdir(path):
                # 该路径是目录
                for item in os.listdir(path):
                    tempPath = path + "/" + item
                    self.deleteDir(tempPath)
                else:
                    pass
            else:
                # 该路径是文件，而不是目录，直接删除
                os.remove(path)
                pass
        else:
            # 文件不存在
            pass
