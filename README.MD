# 抖音网页版协议 👋

## [快手请移步👉](https://github.com/YunzhiYike/kuaishou-live)

## 🧪私有化抖音弹幕服务
> 背景：考虑到开发语言各有不同所以对协议的拆解二开需要花费很多的时间，亦或者说对于萌新同学来讲上手程度太高
> 为此，我们给大家提供了免费的抖音直播推送服务。当然我们也可以支持定制化服务部署（收费）～～

### 接入教程视频 (不懂接入的👀看这里)
[【抖音直播弹幕协议开发（支持所有编程语言开发）！！！】]( https://www.bilibili.com/video/BV1nK411z7uh/?share_source=copy_web&vd_source=71e28910aae780b1b2052c3052b8a2e8)

### 服务地址
> websocket地址：ws://42.193.254.253:9502/dy

### websocket连接测试
![img_1.png](img_1.png)

## 🐂功能
- [X] 直播
- [ ] 短视频
- [ ] 待定.........

## ⛽️ 鼓励一下～
> 逆向是一个很枯燥的活，开源更不容易～～请动动您的小手给个`start`吧～

## [💰 自营代刷社区👈](http://www.kk123.ml)


## 💻 逆向技术
1. 谷歌浏览器 （抓包分析工具）
2. PyCharm  （编写代码）
3. protobuf （谷歌发明的一种通信协议）
4. Charles （抓包分析工具）

## ☕️ 轻松一下（作品展）
> 打个广告🪧～～ 需要直播监控的可以📮联系 `wuaiyiyun2022@163.com`
> 承接 Web、小程序、爬虫、网络代刷、建站、嵌入式、QQ 微信机器人开发等等 
> 擅长语言 `PHP` `Golang` `Python` `Java` `易语言`

![img.png](img.png)

## 使用说明📖
> 运行前请重新生成一下protobuf文件，因为机器系统不一样同时protobuf版本也不一样所以不能拿来直接用～
```shell

protoc -I . --python_out=. dy.proto

```

## 安装websocket依赖
```bash
pip install websocket-client
```

## 方法列表🚗
| 方法名称                | 类型       | 参数说明                                    | 说明        |
|---------------------|----------|-----------------------------------------|-----------|
| dy.parseLiveRoomUrl | `直播` | `url`：电脑网页版直播地址  | `启动抖音客户端` |


## 逆向视频教程
1. [【快手直播间弹幕采集协议分析第一课】](https://www.bilibili.com/video/BV1ZR4y1o7Ab/?share_source=copy_web&vd_source=71e28910aae780b1b2052c3052b8a2e8) 

> 本协议仅供学习参靠请勿非法用途，否则后果自负，与作者无关！

