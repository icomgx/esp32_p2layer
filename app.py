import os
import socket
import struct
import conv
import time

ip = "0.0.0.0"
port = 715
fps = 0

def main():
    global fps
    # 1. 创建套接字 socket
    try:
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
        data = os.listdir('conv2')
        data.sort(key=lambda x: int(x[:-4]))  # 文件名按数字排序
        for img in data:
            start_time = time.perf_counter()
            recv_data = new_client_socket.recv(1024)
            # print(recv_data)
            imageCode = conv.createCode(f'conv2/{img}')
            # print(imageCode)
            d2ata = struct.pack("%dB" % (len(imageCode)), *imageCode)
            # print(len(d2ata))
        # 回送一部分数据给客户端
            new_client_socket.send(d2ata)
            del imageCode[:]
            fps += 1
            end_time = time.perf_counter()
            cost = end_time - start_time
            print(f'传输中：当前{img[:-4]}/共{len(data)} 用时{round(cost,3) * 1000 }ms')
            # time.sleep(0.05)  # 0.05秒 = 50ms   24FPS
        # 关闭套接字
        new_client_socket.close()
        tcp_server_socket.close()

        print(f'传输完成，共耗时{cost}')
    except Exception as ex:
        print(ex)
        new_client_socket.close()
        tcp_server_socket.close()
        print('重启方法')
        main()


if __name__ == "__main__":
    main()
