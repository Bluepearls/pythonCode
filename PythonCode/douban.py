import urllib.request
url="https://erebor.douban.com/?unit=dale_movie_subject_search_bottom&bid=nLFzpPG6piY&crtr=8%3A%E5%AD%A4%E6%B3%A8%E4%B8%80%E6%8E%B7%7C3%3A%2Fmovie%2Fsubject_search%3Fsearch_text%3D%25E5%25AD%25A4%25E6%25B3%25A8%25E4%25B8%2580%25E6%258E%25B7%26amp%3Bcat%3D1002&ts=1693473429934&callback=erebor_5AFFFB88D4F74E41A234DE0F54CD389C"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

request= urllib.request.Request(url=url,headers=headers)

response=urllib.request.urlopen(request)

content=response.read().decode('utf-8')
#print(content)

fp=open("douban.json","w",encoding="utf-8")
fp.write(content)
