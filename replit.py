import os   # 导入 os 模块    #pip3 install os
import sys  # 导入 sys 模块    #pip3 install sys 
import shlex    # 导入 shlex 模块    #pip3 install shlex
import shutil   # 导入 shutil 模块    #pip3 install shutil
import logging  # 导入 logging 模块   #pip3 install logging
import subprocess   # 导入 subprocess 模块    #pip3 install subprocess
from datetime import datetime   # 导入 datetime 模块    #pip3 install datetime
from pyrtmp import PyRTMP   # 导入 PyRTMP 模块 #pip3 install pyrtmp
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
    # 安装python3
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

    # 安装wget，wget是一个网络下载工具，可以从网络上下载文件到本地
    if shutil.which('wget') is not None:    # 判断是否安装 wget
        print('wget 已安装')        # 已安装
    else:
        print('wget is not installed')
    if os.path.isfile('/etc/redhat-release'):   # 判断是否为 CentOS 系统
        subprocess.run(['yum', '-y', 'install', 'wget'])  # 安装 wget
    elif os.path.isfile('/etc/lsb-release'):    # 判断是否为 Ubuntu 系统
        subprocess.run(['apt-get', '-y', 'install', 'wget'])  # 安装 wget
    # 检测wget是否安装成功，如果安装成功则显示安装成功，如果安装失败则显示安装失败
    if shutil.which('wget') is not None:    # 判断是否安装 wget
        print('wget安装成功')        # 已安装
    else:
        print('wget安装失败')        # 未安装

     #检测python是否安装,如果没有安装则安装python3
if os.path.isfile('/usr/bin/python3'):
    print('python3 已安装') #已安装  
else:
    print('python3 is 未安装')   #未安装 
    if os.path.isfile('/etc/redhat-release'):
        subprocess.run(['yum', '-y', 'install', 'python3'])
    elif os.path.isfile('/etc/lsb-release'):
        subprocess.run(['apt-get', '-y', 'install', 'python3'])
#检测pip3是否安装，如果没有安装则安装pip3
if os.path.isfile('/usr/bin/pip3'):
    print('pip3 已安装')#已安装
else:
    print('pip3 is 未安装')  #未安装
    if os.path.isfile('/etc/redhat-release'):
        subprocess.run(['yum', '-y', 'install', 'python3-pip'])
    elif os.path.isfile('/etc/lsb-release'):
        subprocess.run(['apt-get', '-y', 'install', 'python3-pip'])
#检测pyrtmp是否安装 ,如果没有安装则安装pyrtmp       
if os.path.isfile('/usr/local/lib/python3.6/dist-packages/pyrtmp.py'):
    print('pyrtmp 已安装')#已安装
else:
    print('pyrtmp is 未安装')  #未安装
    subprocess.run(['pip3', 'install', 'pyrtmp'])
   

    # 安装screen，screen是一个终端复用器，可以在一个终端中同时打开多个终端，可以在后台运行程序
    if shutil.which('screen') is not None:    # 判断是否安装 screen
        print('screen 已安装')        # 已安装
    else:
        print('screen is not installed')
    if os.path.isfile('/etc/redhat-release'):   # 判断是否为 CentOS 系统
        subprocess.run(['yum', '-y', 'install', 'screen'])  # 安装 screen
    elif os.path.isfile('/etc/lsb-release'):    # 判断是否为 Ubuntu 系统
        subprocess.run(['apt-get', '-y', 'install', 'screen'])  # 安装 screen
    # 检测screen是否安装成功，如果安装成功则显示安装成功，如果安装失败则显示安装失败
    if shutil.which('screen') is not None:    # 判断是否安装 screen
        print('screen安装成功')        # 已安装
    else:
        print('screen安装失败')        # 未安装
            
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
    # 检测ffmpeg是否安装成功，如果安装成功则显示安装成功，如果安装失败则显示安装失败   
    if shutil.which('ffmpeg') is not None:    # 判断是否安装 ffmpeg
        print('ffmpeg安装成功')        # 已安装
    else:
        print('ffmpeg安装失败')        # 未安装
        #从https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-4.0.3-64bit-static.tar.xz下载ffmpeg
        subprocess.run(['wget', '-O', '/root/ffmpeg-4.0.3-64bit-static.tar.xz', 'https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-4.0.3-64bit-static.tar.xz'])
        #解压ffmpeg
        subprocess.run(['tar', '-xvf', '/root/ffmpeg-4.0.3-64bit-static.tar.xz'])
        #移动ffmpeg到/usr/bin
        subprocess.run(['mv', '/root/ffmpeg-4.0.3-64bit-static/ffmpeg', '/usr/bin/ffmpeg'])
        #移动ffprobe到/usr/bin
        subprocess.run(['mv', '/root/ffmpeg-4.0.3-64bit-static/ffprobe', '/usr/bin/ffprobe'])
        #移动ffplay到/usr/bin
        subprocess.run(['mv', '/root/ffmpeg-4.0.3-64bit-static/ffplay', '/usr/bin/ffplay'])
        #删除ffmpeg-4.0.3-64bit-static.tar.xz
        subprocess.run(['rm', '-rf', '/root/ffmpeg-4.0.3-64bit-static.tar.xz'])
        #删除ffmpeg-4.0.3-64bit-static
        subprocess.run(['rm', '-rf', '/root/ffmpeg-4.0.3-64bit-static'])
        #检测ffmpeg是否安装成功，如果安装成功则显示安装成功，如果安装失败则显示安装失败
        if shutil.which('ffmpeg') is not None:    # 判断是否安装 ffmpeg
            print('ffmpeg安装成功')        # 已安装
        else:    
            print('ffmpeg安装失败')        # 未安装

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
            # 判断是否安装 Supervisor，如果安装成功则显示安装成功，如果安装失败则显示安装失败
            if shutil.which('supervisord') is not None:    # 判断是否安装 Supervisor
                print('supervisord安装成功')        # 已安装    
            else:
                print('supervisord安装失败')        # 未安装
    # 判断是否安装pyrtmp,如果未安装则安装，如果已安装则不安装
    if shutil.which('pyrtmp') is not None:    # 判断是否安装 pyrtmp
            print('pyrtmp已安装')        # 已安装
    else:
            print('pyrtmp is not installed')
            # 安装 pyrtmp
            subprocess.run(['pip', 'install', 'pyrtmp'])
            # 判断是否安装 pyrtmp，如果安装成功则显示安装成功，如果安装失败则显示安装失败
            if shutil.which('pyrtmp') is not None:    # 判断是否安装 pyrtmp
                print('pyrtmp安装成功')        # 已安装
            else:
                print('pyrtmp安装失败')        # 未安装

# 创建 screen窗口，如果已存在则不创建
subprocess.run(['screen', '-dmS', 'replit'])    # 创建 screen 窗口
#screen窗口推流

def screen_push(url, mp4dir):
    # 后台screen 窗口运行ffmpeg，播放目录下所有视频文件
    subprocess.run(['screen', '-S', 'replit', '-X', 'stuff',
                    'ffmpeg -re -i ' + mp4dir + ' -c copy -f flv ' + url + ' \n'])  # 后台运行 ffmpeg
    print('推流成功')   # 推流成功

#开始ffmpeg推流
def start_push(url, mp4dir):
    video_files = [f for f in os.listdir(mp4dir) if f.endswith('.mp4')]
    if not video_files:
        logging.error('No video files found in {}'.format(mp4dir))
        return

    for file in video_files:
        filepath = os.path.join(mp4dir, file)
        logging.info('Pushing video {}'.format(filepath))

        ffmpeg_command = 'ffmpeg -re -i "{}" -c:v libx264 -preset:v superfast -tune:v zerolatency ' \
                         '-c:a aac -b:a 128k -f flv "{}"'.format(filepath, url)

        args = shlex.split(ffmpeg_command)

        with subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            try:
                while process.poll() is None:
                    line = process.stderr.readline()
                    if not line:
                        break

                    logging.info(line.decode('utf-8').strip())

            except Exception as e:
                logging.error('Error pushing stream: {}'.format(e))

        print('推流已结束')
    
#开始PyRTMP推流
def start_push_pyrtmp(url, mp4dir):
    # 后台screen 窗口运行PyRTMP,获取所有 .mp4 和 .flv 文件
    video_files = [f for f in os.listdir(mp4dir) if f.endswith('.mp4')]
    if not video_files:
        logging.error('No video files found in {}'.format(mp4dir))
        return

    rtmp = PyRTMP(url)
    if not rtmp.connect():
        logging.error('Failed to connect to RTMP server')
        return

    try:
        for file in video_files:
            filepath = os.path.join(mp4dir, file)
            logging.info('Pushing video {}'.format(filepath))

            st = os.stat(filepath)
            file_size = st.st_size

            with open(filepath, 'rb') as f:
                chunk_size = 1024 * 1024
                timestamp = None

                while True:
                    data = f.read(chunk_size)

                    if not data:
                        break

                    frame_type = 0x01
                    data_type = 0x09
                    stream_id = 0x01
                    ts = int(datetime.now().timestamp() * 1000)

                    # 为第一帧设置时间戳
                    if timestamp is None:
                        timestamp = ts

                    header = (frame_type << 4) | data_type

                    rtmp.set_chunk_size(chunk_size)
                    rtmp.set_peer_bandwidth(chunk_size * 8, 2)
                    rtmp.send_packet(header, stream_id, timestamp, ts, data)

                    timestamp += 200

                    if file_size < chunk_size:
                        remaining = chunk_size - file_size
                        padding = bytearray(remaining)
                        rtmp.send_packet(0x02, stream_id, ts, ts, padding)

                    file_size -= chunk_size

    except Exception as e:
        logging.error('Error pushing stream: {}'.format(e))

    rtmp.close()

    print('推流已结束')
#开始循环推流
def start():
    url = ''
    mp4dir = ''
    # 选项输入数字选择，1 推流地址/推流码 2 播放目录 3 更改推流地址 4 更改推流码 5 ffmpeg推流 6 PyRTMP推流 7 screen窗口推流 0 退出
    print('选项输入数字选择，1 推流地址/推流码 2 播放目录 3 更改推流地址 4 更改推流码 5 ffmpeg推流 6 PyRTMP推流 7 screen窗口推流 0 退出')   
    # 输入选项
    choose = input('输入选项：')
    if choose == '1':  # 1 推流地址/推流码
            url = input('输入推流地址/推流码：')
            print('推流地址/推流码：' + url)
    elif choose == '2':  # 2 播放目录
            mp4dir = input('输入播放目录：')
            print('播放目录：' + mp4dir)
    elif choose == '3':  # 3 更改推流地址
            url = input('输入推流地址：')
            print('推流地址：' + url)
    elif choose == '4':  # 4 更改推流码
            code = input('输入推流码：')
            url = url.split('/')[0] + '/' + code
            print('推流地址/推流码：' + url)
    elif choose == '5':  # 5 ffmpeg推流
        # 跳到start_push开始ffmpeg推流
        start_push(url, mp4dir) # 开始ffmpeg推流
    elif choose == '6':  # 6 PyRTMP推流
        # 跳到start_push_pyrtmp开始PyRTMP推流
        start_push_pyrtmp(url, mp4dir) # 开始PyRTMP推流
    elif choose == '7':  # 7 screen窗口推流
        # 跳到start_push_screen开始screen窗口推流
        screen_push(url, mp4dir) # 开始screen窗口推流 
    elif choose == '0':  # 0 退出   
        exit()
    else:
        print('输入错误')
    start() # 重新开始循环推流

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
