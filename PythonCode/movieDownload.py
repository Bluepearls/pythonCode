#Writed By Python_Fucker On 24/12/2023
import mechanicalsoup
def so_movie(keyword,page):
 for i in range(1,page+1):
  browser = mechanicalsoup.StatefulBrowser()
  url = f"https://www.wo4k.com/wosearch/{keyword}----------{i}---.html"
  print(f"-----第{i}页------")
  browser.open(url)
  movies = browser.page.select('.video-info-header h3')
  years = browser.page.select('.video-info-aux')
  for movie, year in zip(movies, years):
    text = movie.text
    link = movie.find('a')['href']
    print(text + " | ", year.text.strip().replace("\n", "·"))
    link = "https://www.wo4k.com" + link
    browser.open(link)
    titles = browser.page.select('.module-row-title')
    for title in titles:
        h4 = title.select_one('h4').text
        p = title.select_one('p')
        if p is not None:
            p_text = p.text
            print(h4+" | ", p_text)
            print("--------------------------")
    print("\n······································")
#搜索
so_movie("速度与激情",2)#关键词和页数