# full_link

一个全链路监控、展示的项目，前端使用了antv G6，但是研究不深，简单使用

每10s从es抓取做近10s内的数据，将数据存入orm中，在展示到前端。前端每10s刷新一下。

```py
nohup python utils/dingshi.py &
```

做了两个前端：
url： http://ip/
[active](https://github.com/syklinux/full_link/blob/master/static/1.png)

url2: http://ip/index/
[active](https://github.com/syklinux/full_link/blob/master/static/2.png)
