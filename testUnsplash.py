# _*_ coding: UTF-8 _*_

# Python 爬虫 - unsplash 图片

from GetPicUrls import *
from ImgDownad import *

PicUrls = GetPicUrls("/Users/liupei/Desktop/0000-downTemp3")
# urlPath = PicUrls.getUnslpashBmw("bmw")
urlPath = PicUrls.getUnslpashBmw("benz")
PicUrls.downloadAll(urlPath)

# ImgDownalod("/Users/liupei/Desktop/0000-downPic1").downloadAll(urls)

# imgHeader = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "accept-encoding": "gzip, deflate, br",
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# }
# cookie = {
#     "ugid": "ee8ce13a0d95c89ab9439e2f7c711dc35146126",
#     "_ga": "GA1.2.271331607.1543837929",
#     "_gid": "GA1.2.382353724.1543837929"
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}  # 给请求指定一个请求头来模拟chrome浏览器
# web_url = 'https://unsplash.com/napi/search/photos'
# paramss = {
#     "query": "bmw",
#     "per_page": "200",
#     "page": "1",
# }
#
# # session
# page = requests.Session()
# page.headers = imgHeader
# print("*** 开始获取网页")
# resp = page.get(web_url, params=paramss)
# print("*** 获取网页完成")
# # print("resp = ",resp.text)
#
# respJson = json.loads(resp.text)
# results = respJson["results"]
# imgUrls = []
# for item in results:
#     tempUrl = item["urls"]["thumb"]  # raw small regular full thumb
#     description = item["description"]
#     imgUrls.append({"name": description + ".jpeg", "url": tempUrl})
#
# # all_a = BeautifulSoup(resp.text, 'lxml').find('div', id='gridMulti')
# # print("*** 使用bs4解析html")
# #
# # urls = []
# # for div1 in all_a:
# #     # print("*** 循环 - 第1层", div1)
# #     for div2 in div1:
# #         # print("*** *** 第2层", div2)
# #         img2 = div2.find("img")
# #         name = img2["alt"]
# #         name = name.replace(" ", "_")
# #         img2Url = img2["src"]
# #         # print("  第2层", img2)
# #         # 去掉图片链接里的宽高
# #         lastIndex = img2Url.index("&w")
# #         tempUrl = img2Url[0:lastIndex]
# #         print("*** *** name = ", name, "\n url = ", tempUrl)
# #         urls.append({"name": name, "url": tempUrl})
#
# print("\n urls = ", imgUrls)
# saveStr = json.dumps(imgUrls)
# print(saveStr)
# print(type(saveStr))
#
# disName = "/Users/liupei/Desktop/0000-downTemp2"
# fileName = "unsplash_bmw_urls"
# isExists = os.path.exists(disName)
# print("*** download *** 检查目录是否存在...")
# if not isExists:
#     print("创建名为", disName, "的文件夹")
#     os.makedirs(disName)
# else:
#     print("文件夹已存在，不用创建")
#
# os.chdir(disName)
# fileName = fileName + ".json"
#
# with open(fileName, "w", encoding="utf-8") as f:
#     f.write(json.dumps(saveStr, indent=4))
#
# # f = open(fileName, "ab")
# # print("*** download *** 打开文件 ...")
# # f.write(saveStr)
# # print("*** download *** 文件写入 ...")
# # f.close()
# # print("*** download *** 文件关闭 ...")
#
#
# # for item in imgUrls:
# # 下载图片并保存到目录下
# # dp = DownloadPic(tempUrl, "/Users/liupei/Desktop/0000-downTemp2", name).download()
