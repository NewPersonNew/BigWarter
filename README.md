# BigWarter
python code for study with everybody and make me get up
### 基于scrapy_redis爬虫框架，修改去重逻辑，使用布隆过滤器来提高去重上限
- 基本实现流程介绍
  - 布隆过滤器封装在py_bloomfilter.py中，基于redis.第三方依赖：mmh3--下载命令: pip install mmh3(用来实现hash的函数类库).
  - bloom_dupefilter.py 来重写scrapy_redis的去重策略.
  - settings.py配置修改，如下图，跟scrapy_redis的配置格式基本相同，不过需要把去重的类改成我们自己重写的DUPEFILTER_CLASS.
  
    ![image](https://github.com/NewPersonNew/BigWarter/blob/master/screenshots/image.png)
  
    
  - 使用爬虫流程跟scrapy_redis的操作相同，去重数据会在我们的布隆过滤器交互的redis里。
  - 我的py_bloomfilter.py跟bloom_dupefilter.py路径放置如下图：
    
    ![image](https://github.com/NewPersonNew/BigWarter/blob/master/screenshots/image1.png)
### 滑块验证码破解
- 代码hua_kuai.py
- 来自于网易验证码 
- ![image](http://necaptcha.nosdn.127.net/6346d2badb514049a16aa3c086b9b6f0.jpg)
- 执行代码返回的是滑块缺口左侧行坐标，之后可以使用自动化软件(selenium)去实现自动化滑动
