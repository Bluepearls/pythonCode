

# (1) 请求对象的定制
# （2）获取网页的源码
# （3）下载


# 需求 下载的前十页的图片
# https://sc.chinaz.com/tupian/qinglvtupian.html   1
# https://sc.chinaz.com/tupian/qinglvtupian_page.html

import urllib.request
from lxml import etree

def create_request(page):
    if(page == 1):
        url = 'https://sc.chinaz.com/ppt'
    else:
        url = 'https://sc.chinaz.com/ppt/index_' + str(page) + '.html'

    headers = {
        'Cookie':'cz_statistics_visitor=9c15e4f5-04f7-5665-77c9-9dba4bba6d8e; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1693806784; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1693813072',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    request = urllib.request.Request(url = url, headers = headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
   # print(content)
    return content


def down_load(content):
#     下载图片
    # urllib.request.urlretrieve('图片地址','文件的名字')
    tree = etree.HTML(content)

    #name_list = tree.xpath('//div[@class="moer-img-box clearfix"]/img/@alt')
    #print(name_list)
    # 一般设计图片的网站都会进行懒加载
    src_list = tree.xpath('//div[@class="moer-img-box clearfix"]/img/@data-original')

    for i in range(len(src_list)):
        #name = name_list[i]
        src = src_list[i]
        url = 'https:' + src

        print(url)

        urllib.request.urlretrieve(url=url,filename='./powerpoint/' + str(i) + '.pptx')




if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page,end_page+1):
        # (1) 请求对象的定制
        request = create_request(page)
        # （2）获取网页的源码
        content = get_content(request)
        
        #print(content)
        # （3）下载
        down_load(content)
