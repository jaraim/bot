import os
import sys
import shutil
import subprocess
# 下载 replit.py
def download_replit():
    if os.path.isfile('/root/replit.py'):   # 判断是否下载 replit.py
        print('replit.py is downloaded')    # 已下载
    else:
        print('replit.py is not downloaded')    # 未下载
        subprocess.run(['wget', '-O', '/root/replit.py',
                        'https://raw.githubusercontent.com/zhaojun1998/zfile/master/replit.py'])   # 下载 replit.py
        subprocess.run(['chmod', '+x', '/root/replit.py'])   # 添加执行权限
        # 后台运行 replit.py
        subprocess.Popen(
            'nohup python3 /root/replit.py 1 > /dev/null 2>&1 &', shell=True)
# 更新系统
def update_system():
    if os.path.isfile('/etc/redhat-release'):  # 判断是否为 CentOS 系统
        subprocess.run(['yum', '-y', 'update'])  # 更新系统
        subprocess.run(['yum', '-y', 'install', 'python3'])  # 安装 Python3
    elif os.path.isfile('/etc/lsb-release'):    # 判断是否为 Ubuntu 系统
        subprocess.run(['apt-get', 'update'])   # 更新系统
        subprocess.run(['apt-get', '-y', 'install', 'python3'])  # 安装 Python3
    if os.path.isfile('/usr/bin/pip3'):  # 判断是否安装 pip3
        print('pip3 is installed')     # 已安装
    else:
        print('pip3 is not installed')  # 未安装
    if os.path.isfile('/etc/redhat-release'):   # 判断是否为 CentOS 系统
        subprocess.run(['yum', '-y', 'install', 'python3-pip'])  # 安装 pip3
    elif os.path.isfile('/etc/lsb-release'):    # 判断是否为 Ubuntu 系统
        subprocess.run(['apt-get', '-y', 'install',
                       'python3-pip'])  # 安装 pip3

    if shutil.which('requests') is not None:    # 判断是否安装 requests
        print('requests is installed')        # 已安装
    else:
        print('requests is not installed')   # 未安装
        subprocess.run(['pip3', 'install', 'requests'])  # 安装 requests
# 安装依赖
def install_dependence():

    # 安装screen，screen是一个终端复用器，可以在一个终端中同时打开多个终端，可以在后台运行程序
    if shutil.which('screen') is not None:    # 判断是否安装 screen
        print('screen 已安装')        # 已安装
    else:
        print('screen is not installed')
    if os.path.isfile('/etc/redhat-release'):   # 判断是否为 CentOS 系统
        subprocess.run(['yum', '-y', 'install', 'screen'])  # 安装 screen
    elif os.path.isfile('/etc/lsb-release'):    # 判断是否为 Ubuntu 系统
        subprocess.run(['apt-get', '-y', 'install', 'screen'])  # 安装 screen
    # 显示screen安装成功
    print('screen安装成功')          
    # 安装ffmpeg 用于合并视频
    if shutil.which('ffmpeg') is not None:    # 判断是否安装 ffmpeg
        print('ffmpeg 已安装')        # 已安装
    else:
        print('ffmpeg is not installed')
    if os.path.isfile('/etc/redhat-release'):
        subprocess.run(['yum', '-y', 'install', 'epel-release'])
        subprocess.run(['yum', '-y', 'install', 'ffmpeg'])
    elif os.path.isfile('/etc/lsb-release'):
        subprocess.run(['apt-get', '-y', 'install', 'ffmpeg'])
    # 显示ffmpeg安装成功
    print('ffmpeg安装成功')
    # 判断是否安装Supervisor，如果未安装则安装，如果已安装则不安装
    if shutil.which('supervisord') is not None:    # 判断是否安装 Supervisor
            print('supervisord已安装')        # 已安装
    else:
            print('supervisord is not installed')
            if os.path.isfile('/etc/redhat-release'):   # 判断是否为 CentOS 系统
                # 安装 Supervisor
                subprocess.run(['yum', '-y', 'install', 'supervisor'])
            elif os.path.isfile('/etc/lsb-release'):    # 判断是否为 Ubuntu 系统
                # 安装 Supervisor
                subprocess.run(['apt-get', '-y', 'install', 'supervisor'])
            # 显示 Supervisor 安装成功
            print('supervisor安装成功')
# 创建 screen窗口，如果已存在则不创建
subprocess.run(['screen', '-dmS', 'replit'])    # 创建 screen 窗口
#标记推流
def start_push(url, mp4dir):
    # 后台screen 窗口运行ffmpeg，播放目录下所有视频文件
    subprocess.run(['screen', '-S', 'replit', '-X', 'stuff',
                    'ffmpeg -re -i ' + mp4dir + ' -c copy -f flv ' + url + ' \n'])  # 后台运行 ffmpeg
    print('推流成功')
#开始循环推流
def start():
    # 选项输入数字选择，1 推流地址/推流码 2 播放目录 3 更改推流地址 4 更改推流码 5 退出
    print('1 推流地址/推流码 2 播放目录 3 更改推流地址 4 更改推流码 5 退出')
    option = input('请输入选项：')
    if option == '1':
        url = input('请输入推流地址/推流码：')
        if url == '':
            print('推流地址/推流码不能为空')
            exit()
        print('推流地址/推流码设置成功')
    elif option == '2':
        mp4dir = input('请输入播放目录：')
        if mp4dir == '':
            print('播放目录不能为空')
            exit()
        print('播放目录设置成功')
        # 判断播放目录是否存在
        if os.path.exists(mp4dir):
            print('目录存在')
        #跳到def start_push(url, mp4dir)标记推流
            start_push(url, mp4dir) # 开始推流
        else:
            print('目录不存在')
            exit()
    elif option == '3':
        url = input('请输入推流地址：')
        if url == '':
            print('推流地址不能为空')
            exit()
        print('推流地址设置成功')
    elif option == '4':
        url = input('请输入推流码：')
        if url == '':
            print('推流码不能为空')
            exit()
        print('推流码设置成功')
    elif option == '5':
        exit()  # 退出程序
# 后台运行Supervisor，检测replit.py是否运行，如果未运行则重启replit.py
subprocess.Popen('nohup supervisord -c /etc/supervisord.conf > /dev/null 2>&1 &',
                shell=True)    # 后台运行 Supervisor
with open('/etc/supervisord.conf', 'w') as f:  # 添加 Supervisor 配置文件
    f.write('[program:replit]\n')  # 添加程序名称
    f.write('command=python3 /root/replit.py\n')  # 添加程序运行命令
    f.write('autostart=true\n')  # 添加自动启动
    f.write('autorestart=true\n')  # 添加自动重启
    f.write('startsecs=10\n')  # 添加启动延迟
    f.write('startretries=3\n')  # 添加启动重试次数
# 显示开始菜单： 1 开始循环推流 2 停止循环推流 3 推流状态 4 下载文件 5 安装依赖 6.安装更新系统 0 退出
print('1 开始循环推流 2 停止循环推流 3 推流状态 4 下载文件 5 安装依赖 6.安装更新系统 0 退出')
option = input('请输入选项：')
if option == '1':
    start() # 开始循环推流
elif option == '2':
    subprocess.run(['screen', '-S', 'replit', '-X', 'stuff', 'exit\r']) # 停止循环推流
    print('已停止') 
elif option == '3':
    subprocess.run(['screen', '-r', 'replit']) # 显示推流状态
elif option == '4':
    download_replit() # 下载文件
elif option == '5':
    install_dependence() # 安装依赖
elif option == '6':
    update_system() # 安装更新系统
elif option == '0':
    exit()
else:
    print('输入错误')
    exit()  # 退出程序
