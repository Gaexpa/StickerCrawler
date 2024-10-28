<h1>介紹</h1>
因為注意到Steam要找特定貼紙價格，有時候載入會很久，就想說作一個爬蟲監看

這是一個抓Steam市集貼紙價格的python爬蟲，每隔1小時更新，運作時會是在最底層的視窗，也就是所有視窗都會遮蓋他，因為我預想他是一個桌面小程式

![截圖](/screenShots/0.png)
---
**StickerCrawler.py**：建立連線、使用BeautifulSoup和reqests爬資料

**CrawlerGUI.py**：使用QtGui套件建立視窗，顯示價格

使用 pyinstaller打包成.exe檔(放在\dist\)
