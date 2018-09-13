# BigWarter
python code for study with everybody and make me get up
### 基于scrapy_redis爬虫框架，修改去重逻辑，使用布隆过滤器来提高去重上限
- 基本实现流程介绍
  - 布隆过滤器封装在py_bloomfilter.py中，基于redis,第三方依赖：mmh3--下载命令: pip install mmh3(用来实现hash库).
  - bloom_dupefilter.py 来重写scrapy_redis的去重策略.
  - settings.py配置修改，
