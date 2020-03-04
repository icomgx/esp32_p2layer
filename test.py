import conv


res = conv.flTodic('badapple.fc')
fc_len = int(res['fc_len'])
print(f'文件长度：{fc_len}')
for dat in range(fc_len):
    print(res[str(dat)])



