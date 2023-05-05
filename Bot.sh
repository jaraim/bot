bash
#!/bin/bash
# Bot.sh

# 获取当前操作系统的名称
OS=$(uname -s)

# 检查操作系统是否为Ubuntu或CentOS
if [ "$OS" = "Linux" ]; then 
    if [ -x "$(command -v apt-get)" ]; then
        echo "当前系统为Ubuntu"
        echo "apt-get已安装"
    else
        echo "当前系统为Ubuntu" 
        echo "apt-get未安装,开始安装..."
        sudo apt-get update
        sudo apt-get install -y apt-get
    fi
else 
    if [ -x "$(command -v yum)" ]; then
        echo "当前系统为CentOS"
        echo "yum已安装"
    else
        echo "当前系统为CentOS" 
        echo "yum未安装,开始安装..."
        sudo yum update
        sudo yum install -y yum
    fi
fi

# 选项:1.环境配置脚本,2.服务部署脚本,3.机器人部署脚本
echo "请选择需要执行的脚本:"
echo "1.环境配置脚本"  
echo "2.服务部署脚本"
echo "3.机器人部署脚本"
read -p "请输入选项:" option

case $option in
    1) 
        echo "开始执行环境配置脚本..."
        !pip install -r requirements.txt 
        ;;
    2)
        echo "开始执行服务部署脚本..."
        # 服务部署代码......
        ;;
    3)
        echo "开始执行机器人部署脚本..." 
        # 机器人部署代码......
        ;;
    *)
        echo "输入错误,请重新输入!"
        ;;
esac

