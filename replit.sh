#!/bin/bash
#检测wget有没有安装，没有就安装
if [ ! -x "$(command -v wget)" ]; then
  echo 'Error: wget is not installed.' >&2
  echo 'Installing wget...'
  sudo apt-get install wget
fi  
#下载replit.py
wget https://raw.githubusercontent.com/jaraim/bot/main/replit.py
#运行replit.py
python3 replit.py
