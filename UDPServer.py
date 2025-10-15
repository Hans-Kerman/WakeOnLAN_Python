# -*- coding: UTF-8 -*-
from socket import *
import sys

default_mac = "BCFCE7169D21"

if len(sys.argv) > 2:
    print("too many arguments!")
    sys.exit(1)

if (len(sys.argv) == 2) and str(sys.argv[1]) in ["-h","--help"]:
    print ("输入目标12位mac地址")
elif (len(sys.argv) == 2 ):
    default_mac = "".join(char.upper() if char.isalpha() else char for char in sys.argv[1] if char.isalnum())
    if len(default_mac) != 12:
        print('请输入正确的mac地址')
        sys.exit(1)

# 255.255.255.255表示向任何网段发送广播消息
address = ('172.16.76.255', 9)

# 创建流式socket
s = socket(AF_INET, SOCK_DGRAM)

# 设置socket属性
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

source = default_mac
default_mac = default_mac*16
default_mac = "FFFFFFFFFFFF" + default_mac

message = bytes.fromhex(default_mac)

# 发送广播消息
s.sendto(message, address)

print(' send ok ! '+str(source)+' is booted. ')

# 关闭socket
s.close()

