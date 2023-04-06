#!/bin/bash
echo -e "${green} 后台开始： nohup bash stream.sh & ${font}"
echo -e "${green} 后台停止： ps -ef | grep stream.sh ${font}"

# 获取用户输入推流地址，视频地址
read -p "输入你的推流地址和推流码(rtmp协议):" url
read -p "输入你的视频存放目录 (格式仅支持mp4,并且要绝对路径,例如/opt/video):" folder
# 无限循环
while true
do        
    # 获取视频视频地址
    video=$(ls $folder/*.mp4 | shuf -n 1)
    # 获取视频参数
    video_info=$(ffprobe -v quiet -print_format json -show_format -show_streams $video)     
  # 拼接推流命令ffmpeg -re -i ' + mp4 + ' -c copy -f flv ' + url  
    ffmpeg -re -i $video -c copy -f flv $url
    sleep 1
done
