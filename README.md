# 我的Flask面试项目

使用python搭建一个后台服务，并部署到linux系统上 需要实现几个接口功能 
1. 公告信息获取接口（需要可以编辑公告信息）
2. 用户订单号生成(订单号保证唯一)
3. 用户文件上传和用户文件下载接口(一个用户只允许保存一个文件，新文件会覆盖旧文件) 暂未实现
4. 用户游戏兑换码接口(生成和领取)


## 项目环境python3.9
```shell
pip install -r ./requirements.txt
```


## 服务器部署
```shell
docker build -t puppets/flaskproject:1.0 .
docker run -it  -p 5000:5000 --name myflask puppets/flaskproject:1.0
```

## 服务器页面
1. http://127.0.0.1:5000/order 
2. http://127.0.0.1:5000/file/upload
3. http://127.0.0.1:5000/file/download
4. http://127.0.0.1:5000/code


