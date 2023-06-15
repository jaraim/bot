#!/bin/bash
# 获取当前操作系统的名称
OS=$(uname -s)
# 检查操作系统是否为Ubuntu或CentOS
if [ "$OS" = "Linux" ]; then
    if [ -x "$(command -v apt-get)" ]; then
        echo "当前系统为Ubuntu"
        echo "apt-get已安装"
    else
        echo "当前系统为Ubuntu"
        echo "apt-get未安装，开始安装..."
        sudo apt-get update
        sudo apt-get install -y apt-get   
    fi 
else 
    if [ -x "$(command -v yum)" ]; then
        echo "当前系统为CentOS"
        echo "yum已安装"
    else
        echo "当前系统为CentOS"
        echo "yum未安装，开始安装..."
        sudo yum update
        sudo yum install -y yum
    fi  
fi

  # 检查Python 3是否已安装
if [ -x "$(command -v python3)" ]; then
    echo "Python 3已经安装"
else
    echo "Python 3未安装。正在安装..."
    if [ -x "$(command -v apt-get)" ]; then
      sudo apt-get update
      sudo apt-get install -y python3
    else
      sudo yum update
      sudo yum install -y python3
    fi
fi

  # 检查pip3是否已安装
if [ -x "$(command -v pip3)" ]; then
    echo "pip3已经安装"
else
    echo "pip3未安装。正在安装..."
    if [ -x "$(command -v apt-get)" ]; then
      sudo apt-get update
      sudo apt-get install -y python3-pip
      python3 -m pip install --upgrade pip
    else
      sudo yum update
      sudo yum install -y python3-pip
      python3 -m pip install --upgrade pip
    fi
fi
# 检查Python 3和pip3是否安装成功
echo "Python 3和pip3安装完成"
python3 --version
pip3 --version
