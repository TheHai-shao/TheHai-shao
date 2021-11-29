# coding: utf-8
import requests,re,fitz,json,base64
from lxml import etree
from bs4 import BeautifulSoup
import os.path

'''
# 将PDF转化为图片
pdfPath pdf文件的路径
imgPath 图像要保存的文件夹
zoom_x x方向的缩放系数
zoom_y y方向的缩放系数
rotation_angle 旋转角度
'''

#PDF转图片
def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle):
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 逐页读取PDF
    list1 = []
    for pg in range(0, pdf.pageCount):
        dic = {}
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.writePNG(imgPath + str(pg) + ".png")
        dic["data"] = imgPath + str(pg) + ".png"
        list1.append(dic)
    num = pdf.pageCount
    dis = {}
    dis["nums"] = num
    list1.append(dis)
    pdf.close()
    print(list1)
    return list1
#图片识别
def img_down_load(sk):
    host = ''
    response = requests.get(host)
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    f = open(sk, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    access_token = response.json()['access_token']
    request_url = request_url + "?access_token=" + access_token
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
    # headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        try:
            counts = response.json()['words_result']
        except:
            counts = response.json()
        return counts


def run():
    start_url = [f'https://land.zjgtjy.cn/GTJY_ZJ/deala_js_action?resourcelb=01&dealtype=&JYLB=&JYFS=&JYZT=&RESOURCENO=&RESOURCEMC=&endDate=&ZYWZ=&zylb=01&SSXZQ=330300&currentPage={i}'for i in range(15,22)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    for k in start_url:
        resp = requests.get(url=k,headers = headers)
        """
        x_urls = "https://land.zjgtjy.cn/GTJY_ZJ/landinfo?ResourceID="  详细信息
        f_urls = 'https://land.zjgtjy.cn/GTJY_ZJ/downFileAction?rid=28648&fileType=1'  附件
        """
        resp = etree.HTML(resp.text)
        x = resp.xpath('//span[@class="boxtxt2"]/input[last()]/@onclick')
        #详细信息
        for j in x:
            list3 = []
            strs = j.replace("javascript:goRes('","").replace("','01');","")
            x_urls = "https://land.zjgtjy.cn/GTJY_ZJ/landinfo?ResourceID="+strs #详细信息
            print(x_urls)
            x_resp = requests.get(url=x_urls,headers = headers)
            so = BeautifulSoup(x_resp.text, 'lxml')
            trs = so.select('.td_line2 table tr')
            dic = {}
            for tr in trs:
                tds = tr.select('td')
                for k, v in enumerate(tds):
                    if k % 2 == 0:
                        key = tds[k].text.strip()
                        try:
                            value = re.sub(r'[\s\r\n\t]*', '', tds[k + 1].text.strip())
                            dic[key] = value
                        except:
                            flag = 1
                            name = '备注' + str(1)  # 表格中只有一行的情况
                            flag = flag + 1
                            dic[name] = key

                    else:
                        pass
            f_urls = [f'https://land.zjgtjy.cn/GTJY_ZJ/downFileAction?rid={strs}&fileType=1'] #附件
            print(f_urls)
            f_resp =  requests.get(url=f_urls[0],headers = headers)
            so = BeautifulSoup(f_resp.text, 'lxml')
            tr_lst = so.select('.xs_list_table tr')[4]
            a = re.findall(r"[\d]{20}[^_.'][^-']\d+\.[a-zA-Z]+", tr_lst.select('td a')[0]['onclick'])[0]
            print(a)
            dw_url = f'https://hz-zhongzhi.oss-cn-hzfinance.aliyuncs.com/landOldFileFolder/{a}'
            # print(dw_url)
            # print(dw_url.split('.')[-1])

            if dw_url.split('.')[-1] == 'pdf' or dw_url.split('.')[-1] == 'PDF':
                r = requests.get(dw_url)
                fo = open(dic["地块编号"], 'wb')  # 注意要用'wb',b表示二进制，不要用'w'
                fo.write(r.content)  # r.content -> requests中的二进制响应内容：以字节的方式访问请求响应体，对于非文本请求
                fo.close()
                name = dic["地块编号"]
                sk = pdf_image(dic["地块编号"], rf"E:/杭州市装配式文件/{name}", 1, 1, 0)
                ui = 0
                for u in sk:
                    try:
                        data = img_down_load(u["data"])
                    except:
                        break
                    print(data)
                    for f in data:
                        if f["words"].find("装配式")!=-1 or f["words"].find("应按照建筑工业化")!=-1:
                            dic["装配式"] = f["words"]
                            print(dic)
                            ui=1
                            break
                    if ui==1:
                        break
                os.remove(dic["地块编号"])
            elif dw_url.split('.')[-1] == 'jpg' or dw_url.split('.')[-1] == 'png':
                r = requests.get(dw_url)
                print(dw_url)
                fo = open(dic["地块编号"], 'wb')  # 注意要用'wb',b表示二进制，不要用'w'
                fo.write(r.content)  # r.content -> requests中的二进制响应内容：以字节的方式访问请求响应体，对于非文本请求
                fo.close()
                data = img_down_load(dic["地块编号"])
                print(data)
                for f in data:
                    if f["words"].find("装配式") != -1:
                        dic["装配式"] = f["words"]
                        break
                os.remove(dic["地块编号"])
            else:
                dic["装配式"] = "暂无"
            try:
                print(dic["装配式"])
            except:
                dic["装配式"] = "暂无"
            list3.append(dic)
            print(list3)

            with open('温州市数据.json', 'a', encoding="UTF-8")as f:
                for data in list3:
                    result = json.dumps(data, ensure_ascii=False) + ',\n'
                    f.write(result)
run()






