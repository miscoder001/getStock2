# F12 selector 推薦
# 參考 user-agent 字串: https://useragentstring.com/pages/useragentstring.php
# span.IsqQVc.NprOob.wT3VGc
# 完整路徑: #knowledge-finance-wholepage__entity-summary > div.aviV4d > g-card-section > div > g-card-section > div.wGt0Bc > div.PZPZlf > span:nth-child(1) > span > span.IsqQVc.NprOob.wT3VGc
# 載入必要套件
from pyquery import  PyQuery as pq
from time import sleep

#發出 request 載入網頁
# 多股查詢 宣告成 list
slist=[2330,2345,2538]
ua = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"}
# headers 送出 瀏覽器識別字串 以防被偵測為 爬蟲
page = pq(url="https://www.google.com/search?q=2345", encoding="utf8", headers=ua)
print("股票代號2345 目前股價: " + page.find('span.IsqQVc.NprOob.wT3VGc').text())






