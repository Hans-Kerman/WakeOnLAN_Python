#! /home/buttercat/codefield/socket_python/WakeOnLAN_Python/.venv/bin/python
from socket import *

# 255.255.255.255表示向任何网段发送广播消息
address = ('255.255.255.255', 8)

# 创建流式socket
s = socket(AF_INET, SOCK_DGRAM)

# 设置socket属性
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

default_mac = "BCFCE7169D21"

default_mac = default_mac*16
default_mac = "FFFFFFFFFFFF" + default_mac

message = bytes.fromhex(default_mac)

# 发送广播消息
s.sendto(message, address)

print(' send ok !')

# 关闭socket
s.close()

