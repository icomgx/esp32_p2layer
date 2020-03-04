# esp32_p2layer
## 基于esp32的播放器
## B站主页 https://space.bilibili.com/23106193 有想法和建议欢迎私信我
## 开发工具：pycharm 环境：Anaconda3（python 3.7.4）  
## 使用库： pillow, opencv-python, numpy  
## 注意 图片和字码文件都已打包 请解压后使用    
##  
## 目录结构：
### ESP32_BadApple 下位机程序存放目录    
### conv2/ 转换完成的1位图目录
### code/ 转换成字码的文件目录   
### video/ 待转换的视频目录    
### videoCut/ 视频切片完成的目录  
### tools/ 视频转换工具目录
#### rgbTobitmap.py 视频转换方法示例
### app.py 程序主入口 -使用1位图播放   
### app2.py 程序主入口 -使用字码文件播放 
### app3.py 程序主入口 -使用.fc文件播放 
### config.py 程序配置  
### badapple.fc badapple 30帧的字码集合文件
### conv.py 转换使用的模块
### videoCut.py 视频切片用模块 
### 
## 2020-03-04： 
### 完成创建，注释添加
