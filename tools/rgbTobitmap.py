import os

import conv
import videoCut

# 使用示例 2020-03-04
# Author: iCOMgx

# 视频转换成1位图
def videoTo1bitmap():
    videos_src_path = "video/"  # 待转换的视频目录
    frames_save_path = "videoCut/"  # 转换完成的文件存放位置
    width = 128  # 图片文件的宽度
    height = 64  # 图片文件的高度
    time_interval = 1  # 切片间隔 1代表一帧一切
    # 执行切片方法 带入上面的参数
    videoCut.video2frame(videos_src_path, frames_save_path, width, height, time_interval)
    data = os.listdir('videoCut/视频名字')  # 循环切片图片转换为灰度图像
    for dat in data:
        conv.conv3(f'videoCut/badapple/{dat}', f'conv/{dat}')  # 转换成灰度图像
    data2 = os.listdir('conv')  # 循环图片二值化
    for dat2 in data2:
        conv.conv4(f'conv/{dat2}', f'conv1/{dat2}')  # 二值化操作
    data3 = os.listdir('conv1')  # 循环二值化完成的图片转为1位图
    for dat3 in data3:
        conv.conv3(f'conv1/{dat3}', f'conv2/{dat3}')  # 转换1位图操作


# 从1位图转换为字码文件
def bitToCodeFile():
    data = os.listdir('conv2') # 从1位图开始循环转换
    for dat in data:
        res = conv.createCode(f'conv2/{dat}')  # 转换为字码
        d2ta = open(f'code/{dat}.txt', 'w')  # 打开文件
        d2ta.write(str(res))  # 写入文件
        d2ta.close()  # 关闭
        del res[:]  # 清空数组


# 从1位图转换到.fc文件 字码集合
def bitToFC():
    d3ta = {}  # 定义一个字典来存储数据
    data = os.listdir('conv2')  # 获取一位图
    d3ta.update({'fc_len': str(len(data))})  # 获取所有帧数添加到字典
    for dat in data:  # 开始循环
        res = conv.createCode(f'conv2/{dat}')  # 1位图转换到字码
        d3ta.update({str(dat[:-4]): str(res)})  # 每一帧的字码存储到字典
        del res[:]  # 清空数组
    d2ta = open(f'test.fc', 'w')  # 打开文件
    d2ta.write(str(d3ta))  # 写入文件
    d2ta.close()  # 关闭
