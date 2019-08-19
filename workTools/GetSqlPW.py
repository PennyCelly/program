# -*- coding: utf-8 -*-
"""
Created on 2017-03-15 07:42:58

@author: codegay
"""

import os
import configparser
import base64


def decode(base64str):
    tmp = base64.b64decode(base64str)
    return bytearray([(b<<1&255)|(b>>7) for b in tmp]).decode("utf8")


sqlyogini = os.environ.get('APPDATA')+"\\SQLyog\\sqlyog.ini"
print("sqlyogini文件路径:", sqlyogini)
ini = configparser.ConfigParser()
ini.read(sqlyogini, encoding='utf8')

connections = [r for r in ini.sections() if 'name' in ini.options(r) and ini.get(r, 'password')]

for c in connections:
    name = ini.get(c, 'name')
    host = ini.get(c, 'host')
    user = ini.get(c, 'user')
    port = ini.get(c, 'port')
    b64pass = ini.get(c, 'password')
    b64ssh_pwd = ini.get(c, 'SshPwd')
    ssh_Host = ini.get(c, 'SshHost')
    ssh_Port = ini.get(c, 'SshPort')
    ssh_User = ini.get(c, 'SshUser')
    ssh_flag = ini.get(c, 'SSH')
    password = decode(b64pass)
    ssh_Pwd = decode(b64ssh_pwd)
    if ssh_flag == '0':
        print('名称：'+name, '主机地址：'+host, '端口号：'+port, '用户名：'+user, sep='\n')
        print('数据库连接密码', password)
        print('----------------------------------------------------------------------------------')
    elif ssh_flag != '0':
        print('名称:' + name, '主机地址:' + host, '端口号:' + port, '用户名:' + user, '数据库连接密码:' + password,
              '隧道IP:' + ssh_Host, '隧道用户名:' + ssh_User,
              '隧道端口号:' + ssh_Port, '隧道密码:'+ssh_Pwd, sep='\n')
        print('----------------------------------------------------------------------------------')
