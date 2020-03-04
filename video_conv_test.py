import numpy

import videoCut
import conv
import os
import base64

videos_src_path = "video/"
# video_formats = [".MP4", ".MOV"]          我的数据集都是.mp4所以不需要进行分类判断
frames_save_path = "videoCut/"
width = 128
height = 64
time_interval = 1

# videoCut.video2frame(videos_src_path, frames_save_path, width, height, time_interval)
# data = os.listdir('videoCut/badapple')
# for dat in data:
#     conv.conv3(f'videoCut/badapple/{dat}', f'conv2/{dat}')
# data2 = os.listdir('twconv')
# for dat2 in data2:
#     conv.conv4(f'twconv/{dat2}', f'twconv2/{dat2}')
# data3 = os.listdir('twconv2')
# for dat3 in data3:
#     conv.conv3(f'twconv2/{dat3}', f'twconv3/{dat3}')


# data = os.listdir('conv2')
# for dat in data:
#     res = conv.createCode(f'conv2/{dat}')
#     d2ta = open(f'conv2/code/{dat}.txt', 'w')
#     d2ta.write(str(res))
#     d2ta.close()
#     del res[:]
#
# data = open('conv2/code/323.bmp.txt', 'r')
# res = data.read()
# data.close()
# print(res)

# res = conv.fileH2xToList('conv2/code/323.bmp.txt')
# for r2es in res:
#     print(r2es)

# res = conv.createCode(f'conv2/233.bmp')
# res = conv.fileH2xToList('code/323.bmp.txt')
# # print(type(res), len(res))

d3ta = {}
data = os.listdir('conv2')
d3ta.update({'fc_len': str(len(data))})
for dat in data:
    res = conv.createCode(f'conv2/{dat}')
    d3ta.update({str(dat[:-4]): str(res)})
    del res[:]
d2ta = open(f'test.fc2', 'w')
d2ta.write(str(base64.b64encode(str(d3ta).encode('utf-8'))))
d2ta.close()
