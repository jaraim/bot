#!/bin/bash

#!/bin/bash

# 获取当前操作系统的名称
OS=$(uname -s)

# 检查操作系统是否为Ubuntu
if [ "$OS" = "Linux" ] && [ -x "$(command -v apt-get)" ]; then
  echo "当前系统为Ubuntu"
  echo "apt-get已安装"
else
  if [ "$OS" = "Linux" ]; then
    echo "当前系统为Ubuntu"
    echo "apt-get未安装，开始安装..."
    sudo apt-get update
  else
    echo "当前系统不是Ubuntu"
  fi
fi

# 检查操作系统是否为CentOS
if [ "$OS" = "Linux" ] && [ -x "$(command -v yum)" ]; then
  echo "当前系统为CentOS"
  echo "yum已安装"
else
  if [ "$OS" = "Linux" ]; then
    echo "当前系统为CentOS"
    echo "yum未安装，开始安装..."
    sudo yum update
  else
    echo "当前系统不是CentOS"
  fi
fi
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
