# Jayvee's API计划
## 这是什么？
本项目的主要作用是将之前的各项目可复用的功能抽离出来，做成Web API供其他项目或有需求的人使用。

## 目前包含哪些API？
### 网易云音乐的歌曲搜索解析服务
最大的作用就是能够提取出外链MP3地址了
#### Method：**POST**
#### URL：``/api/music``
#### Params：
1. ``song_name`` (*required*): 要搜索的歌曲名字
2. ``limit`` (*optional*): 返回结果的最大条数，不填则为5


#### 示例：
```json
{"song_name":"晴天","limit":3}
```

#### 返回：
```json
{
  "results": [
    {
      "songid": 186016,
      "artistname": "周杰伦",
      "picurl": "http://p3.music.126.net/947AzONsSKh3QV9b0c4DOA==/7990151000765600.jpg?param=250y250",
      "songurl": "http://music.163.com/m/song/186016",
      "song_name": "晴天",
      "albumname": "叶惠美",
      "songtitle": "晴天\n周杰伦-叶惠美",
      "mp3url": "http://m2.music.126.net/U2CxR3MGaqD-DHlsCYgksg==/3291937813618641.mp3"
    },
    {
      "songid": 30394763,
      "artistname": "刘瑞琦",
      "picurl": "http://p4.music.126.net/obZy1mbYWFJtbyr26Q6Smg==/7749357952693832.jpg?param=50y50",
      "songurl": "http://music.163.com/m/song/30394763",
      "song_name": "晴天",
      "albumname": "再次寻找周杰伦",
      "songtitle": "晴天\n刘瑞琦-再次寻找周杰伦",
      "mp3url": "http://m2.music.126.net/oxP2XaJFDscDuGhGnO7beA==/7768049650386454.mp3"
    },
    {
      "songid": 185956,
      "artistname": "周杰伦",
      "picurl": "http://p3.music.126.net/_Nx3XhOMw7Mjq8xul5aHpA==/114349209289616.jpg?param=50y50",
      "songurl": "http://music.163.com/m/song/185956",
      "song_name": "晴天(Live) - live",
      "albumname": "2004无与伦比演唱会",
      "songtitle": "晴天(Live) - live\n周杰伦-2004无与伦比演唱会",
      "mp3url": "http://m2.music.126.net/pv4J9ecXl2Dd7DxVeTK1AQ==/7831821325731355.mp3"
    }
  ]
}
```

---

### 摘要/关键句子提取服务 
#### Method：**POST**
#### URL：``/api/textrank``
#### Params:
1. ``sentences`` (*required*): 数组形式的句子
2. ``topk`` （*optional*）: 关键句的结果数，不填则为5

#### 示例：
```json
{
    "sentences":
        ["传了两个月的中国公司要收购 AC 米兰的事情终于有了一个确切的消息，拥有 AC 米兰俱乐部股权的 Fininvest 公司官方正式确认正在和一家来自中国的企业商谈俱乐部股权出售事宜。",
        "可惜的是，Fininvest 公司并没有透露是哪家中国公司正在洽谈收购事宜。",
        "同时，他们也只是表示一切都还在洽谈当中，这意味着最终能不能达成收购目前看来还是一个未知数。",
        "AC 米兰一直是中国资本“最爱”的俱乐部之一。",
        "2014 年 4 月的时候，当时就有意大利媒体报道称，哇哈哈集团正在考虑收购 AC 米兰，不过这一说法随后被哇哈哈董事长宗庆后否认。",
        "2015 年 11 月，AC 米兰老板贝卢斯科尼访华，并称就美丽之冠绿卡收购 AC 米兰一定数量的股权一事达成了合作意向，然而这件事也就此没了下文。"],
    "topk":3
}
```

#### 返回：
```json
{
  "results": [
    {
      "score": 0.20442235821195812,
      "origin_index": 0,
      "sent": "传了两个月的中国公司要收购 AC 米兰的事情终于有了一个确切的消息，拥有 AC 米兰俱乐部股权的 Fininvest 公司官方正式确认正在和一家来自中国的企业商谈俱乐部股权出售事宜。"
    },
    {
      "score": 0.18655841055166694,
      "origin_index": 5,
      "sent": "2015 年 11 月，AC 米兰老板贝卢斯科尼访华，并称就美丽之冠绿卡收购 AC 米兰一定数量的股权一事达成了合作意向，然而这件事也就此没了下文。"
    },
    {
      "score": 0.18133286777399693,
      "origin_index": 4,
      "sent": "2014 年 4 月的时候，当时就有意大利媒体报道称，哇哈哈集团正在考虑收购 AC 米兰，不过这一说法随后被哇哈哈董事长宗庆后否认。"
    }
  ]
}
```