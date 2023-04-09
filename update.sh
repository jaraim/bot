#!/bin/bash
# 检测系统类型，是否安装，已安装则跳过，未安装则安装
if  command -v apt &> /dev/null 
then
    PKG_MANAGER="apt"   # apt是Debian和Ubuntu的包管理器
elif command -v yum &> /dev/null
then
    PKG_MANAGER="yum"   # yum是CentOS和RedHat的包管理器
elif command -v pacman &> /dev/null
then
    PKG_MANAGER="pacman"    # pacman是Arch Linux的包管理器
else
    echo "未知的系统类型"
    exit 1
fi
#显示系统类型，更新系统
echo "系统类型：$PKG_MANAGER"
sudo $PKG_MANAGER update

# 检查Python3和pip3是否已安装，已安装则跳过，未安装则安装
if command -v python3 &> /dev/null
then
    echo "Python3已安装"
else
    echo "Python3未安装，正在安装"
    sudo $PKG_MANAGER install python3
fi
if command -v pip3 &> /dev/null
then
    echo "pip3已安装"
else
    echo "pip3未安装，正在安装"
    sudo $PKG_MANAGER install python3-pip
fi
