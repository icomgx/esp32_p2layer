import os
import cv2

# videos_src_path = "video/"
# # video_formats = [".MP4", ".MOV"]
# frames_save_path = "videoCut/"
# width = 128
# height = 64
# time_interval = 1


def video2frame(video_src_path, frame_save_path, frame_width, frame_height, interval):
    """
    将视频按固定间隔读取写入图片
    :param video_src_path: 视频存放路径
    :param formats:　包含的所有视频格式
    :param frame_save_path:　保存路径
    :param frame_width:　保存帧宽
    :param frame_height:　保存帧高
    :param interval:　保存帧间隔
    :return:　帧图片
    """
    videos = os.listdir(video_src_path)

    # def filter_format(x, all_formats):      无需判断所以这部分代码也就不需要了
    #     if x[-4:] in all_formats:
    #         return True
    #     else:
    #         return False
    #
    # videos = filter(lambda x: filter_format(x, formats), videos)

    for each_video in videos:
        # print "正在读取视频：", each_video
        print("正在读取视频：", each_video)    # 我的是Python3.6

        each_video_name = each_video[:-4]
        os.mkdir(frame_save_path + each_video_name)
        each_video_save_full_path = os.path.join(frame_save_path, each_video_name) + "/"

        each_video_full_path = os.path.join(video_src_path, each_video)

        cap = cv2.VideoCapture(each_video_full_path)
        frame_index = 0
        frame_count = 0
        if cap.isOpened():
            success = True
        else:
            success = False
            print("读取失败!")

        while success:
            success, frame = cap.read()

            print("---> 正在读取第%d帧:" % frame_index, success)      # 我的是Python3.6

            if frame_index % interval == 0 and success:     # 如路径下有多个视频文件时视频最后一帧报错因此条件语句中加and success
                resize_frame = cv2.resize(frame, (frame_width, frame_height), interpolation=cv2.INTER_AREA)
                # cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_index, resize_frame)
                cv2.imwrite(each_video_save_full_path + "%d.bmp" % frame_count, resize_frame)
                frame_count += 1

            frame_index += 1

    cap.release()
