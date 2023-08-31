import requests
import re,os
import urllib.request
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36"
}
response = requests.get("https://sdmda.bupt.edu.cn/szdw/js.htm",headers=headers)
#防止中文乱码
response.encoding = requests.utils.get_encodings_from_content(response.text)
#获取网页源代码
page_content = response.text
#爬取学院、姓名、照片
all_idens = re.findall('.*? class="iden">(.*)</span>', page_content)
all_names = re.findall('.*? class="name">(.*)</span>', page_content)
all_photos = re.findall('.*? <img src="(/__local/.*?)" alt="">', page_content)
#存储照片
file_path =r'E:\professor_photo'
# 是否有这个路径
if not os.path.exists(file_path):
    # 创建路径
    os.makedirs(file_path)
i=0
for name in all_names:
    #获取图片地址
    img_url = "https://sdmda.bupt.edu.cn" + all_photos[i]
    # 获得图片后缀及名称
    file_suffix = os.path.splitext(img_url)[1]
    file_name = name
    # 拼接图片名（包含路径）
    filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
    iden = all_idens[i]
    photo = all_photos[i]
    i = i + 1
    print(iden + "," + name + "," + "教授" + "," + filename)
    # 下载图片，并保存到文件夹中
    urllib.request.urlretrieve(img_url, filename=filename)