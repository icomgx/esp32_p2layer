import os
import socket
import struct
import conv
import time

ip = "0.0.0.0"
port = 715
totaltime = 0
avg_frame = 0

def main():
    global fps, totaltime, avg_frame
    # 1. 创建套接字 socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定本地信息 bind
    tcp_server_socket.bind((ip, port))
    # 3. 让默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128)
    print("启动TCP服务器\r\n" + f'启动在{ip}:{port}上')
    # 4. 等待客户端的链接 accept
    print("等待客户端的链接\r\n")
    new_client_socket, client_addr = tcp_server_socket.accept()
    print(f'当前链接：{client_addr}')
    # 接收客户端发送过来的请求
    # recv_data = new_client_socket.recv(1024)
    # print(recv_data)
    data = os.listdir('code')
    data.sort(key=lambda x: int(x[:-8]))  # 文件名按数字排序
    for img in data:
        start_time = time.perf_counter()
        recv_data = new_client_socket.recv(1024)
        # print(recv_data)
        imageCode = conv.fileH2xToList(f'code/{img}')
        # print(imageCode)
        d2ata = struct.pack("%dB" % (len(imageCode)), *imageCode)
        # print(len(d2ata))
        # 回送一部分数据给客户端
        new_client_socket.send(d2ata)
        del imageCode[:]
        end_time = time.perf_counter()
        cost = end_time - start_time
        totaltime += round(cost, 3) * 1000
        avg_frame += round((1000 / (round(cost,3) * 1000)), 1)
        print(f'传输中：当前{img[:-8]}帧/共{len(data)}帧，用时{round(cost,2) * 1000 }ms '
              f'约等于{round((1000 / (round(cost,3) * 1000)), 2)}FPS')
    # time.sleep(0.05)  # 0.05秒 = 50ms   24FPS
    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()
    print(f'传输完成 共耗时{totaltime}ms|平均帧率{round((avg_frame / len(data)), 2)}FPS')


if __name__ == "__main__":
    main()
