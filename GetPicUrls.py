# _*_ coding: UTF-8 _*_

# Python 爬虫 - unsplash 图片

import requests
import os
import json
from ImgDownad import *


class GetPicUrls:
    # d

    def __init__(self, saveDir):
        self.saveDir = saveDir

    def getUnslpashBmw(self, query):
        imgUrls = []
        pageCount = 30
        page = 1
        query = query
        for i in range(0, 20):
            page = i + 1
            result = self.get("https://unsplash.com/napi/search/photos", {"query": query,
                                                                          "per_page": pageCount,
                                                                          "page": page})
            results = result["results"]
            print("unslpash_bmw results len = ", len(results))

            if len(results) == 0:
                break
            else:
                for item in results:
                    tempUrl = item["urls"]["raw"]  # raw small regular full thumb
                    name = tempUrl[tempUrl.find("photo"):tempUrl.find("?")]
                    imgUrls.append({"name": name + ".jpeg", "url": tempUrl})

        self.saveDir += ("/" + query)
        self.checkDir(self.saveDir)
        os.chdir(self.saveDir)
        saveStr = json.dumps(imgUrls)
        fileName = "unplash_bmw.json"
        return self.save(saveStr, fileName)

    def get(self, url, params):
        resp = requests.get(url, params=params)
        print("resp type = ", type(resp))
        print("resp.url = ", resp.url)
        return resp.json()

    def save(self, jsonObj, fileName):
        # 保存文件
        print("fileName = ", fileName, "\njsonObj = ", jsonObj)
        with open(fileName, "w", encoding="utf-8") as f:
            f.write(jsonObj)
        return os.getcwd() + "/" + fileName

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

    def downloadAll(self, urlsPath):
        with open(urlsPath, "r", encoding="utf-8") as f:
            ImgDownalod(self.saveDir).downloadAll(json.loads(f.read()))
