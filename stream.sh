#!/bin/bash
#后台运行
nohup ./stream.sh > /dev/null 2>&1 &


# 读取用户推流地址
echo "推流地址"
read -p "输入你的推流地址:" url
# 读取用户视频存目录
echo "视频存目录"
read -p "输入你的视频存放目录 (格式仅支持mp4,并且要绝对路径,例如/opt/video):" folder

if [ -z "$url" ]  # 判断url是否为空
then
    echo "url is empty" # url为空，退出
    exit 1
fi

if [ -z "$folder" ] # 判断folder是否为空
then
    echo "folder is empty"  # folder为空，退出
    exit 1
fi
screen -r stream  # 进入screen
# 无限循环
while true; do
    # 读取视频目录
    video=$(ls -rt $folder | head -n 1)

    # 判断视频目录是否为空
    if [ -z "$video" ]; then
        # 视频目录为空，等待下个文件推流
        echo "视频目录为空，等待下个文件推流"
        sleep 1s
        continue
    else
        # 视频目录不为空，开始推流
        echo "视频目录不为空，开始推流"
        for video in $folder/*.mp4
        do
            if [ -f "$video" ]; then
                # 视频参数，编码，格式，推流地址
                video_param="-re -i $video -c:v libx264 -c:a aac -f flv"
                # 合并，参数，显示开始推流，等待下个文件推流
                echo "ffmpeg $video_param $url" # 显示推流命令
                ffmpeg $video_param $url
                echo "开始推流"     
                echo "等待下个文件推流"
                sleep 1s
            else
                echo "$video 没文件" #  没文件，跳过
            fi
        done
        continue
    fi
done
    
