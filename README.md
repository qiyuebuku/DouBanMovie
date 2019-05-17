
# 豆瓣电影爬虫

- 使用scrapy开发，获取豆瓣电影前250名电影的播放地址和下载地址
- 获取多个播放地址和一个电影的下载地址，并会将结果存入到mongodb当中 



用来干啥
----------------

* 整个爬虫本身并没有什么用，纯粹是为了好玩
* 整个爬虫是基于一个模块来做的，Moie_scratcher 
* 他会根据你传入的视频地址，给你返回这个视频的下载地址和免登陆的播放地址
* 支持爱奇艺、优酷、腾讯视频、乐视……
* 致于用这个模块具体可以做什么，自行脑补


###### 例子
```
url = MovieScrathcer.movie_watch_on_url('https://www.iqiyi.com/v_19rsiwm8tk.html#vfrm=19-9-0-1')
print(url) 
# http://jx.aeidu.cn/index.php?url=https://www.iqiyi.com/v_19rsiwm8tk.html#vfrm=19-9-0-1

download_url = MovieScrathcer.movie_download_on_url('https://www.iqiyi.com/v_19rsiwm8tk.html#vfrm=19-9-0-1')
print(download_url)
# http://vwecam.tc.qq.com/1097_52897fe74f974075b6ef051630dfdbbb.f20.mp4?ptype=http&vkey=4A821EDCB4D742C959D2B7D24AD56455A8233A0715A1C474209BE53E5A0DC774593237F66DC691A3FA0606762D99A02887D213524E8E099D
```

部分截图
----------------
播放视频
![Image text](https://github.com/qiyuebuku/img-folder/blob/master/DouBanMovie/%E6%89%B9%E6%B3%A8%202019-05-17%20144121.png)
下载视频
![Image text](https://github.com/qiyuebuku/img-folder/blob/master/DouBanMovie/%E6%89%B9%E6%B3%A8%202019-05-17%20144210.png)


