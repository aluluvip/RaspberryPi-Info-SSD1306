#!/bin/bash

# 设置目标主机信息
HOST="raspberrypi.local"
USER="admin"
PASS="19941024"
REMOTE_DIR="/home/admin/workspace/pi_info"

# 创建临时expect脚本
cat > /tmp/sftp_script.exp << 'EOL'
#!/usr/bin/expect -f

set timeout -1
set host [lindex $argv 0]
set user [lindex $argv 1]
set pass [lindex $argv 2]
set remote_dir [lindex $argv 3]

# 启动sftp会话
spawn sftp $user@$host

# 处理密码提示
expect {
    "*password:" { send "$pass\r" }
    "*yes/no*" {
        send "yes\r"
        expect "*password:" { send "$pass\r" }
    }
}

# 等待sftp提示符
expect "sftp>"

# 切换到远程目录
send "cd $remote_dir\r"
expect "sftp>"

# 上传所有文件
send "put -r *\r"
expect "sftp>"

# 退出sftp
send "bye\r"
expect eof
EOL

# 设置expect脚本权限
chmod +x /tmp/sftp_script.exp

# 执行expect脚本
/tmp/sftp_script.exp "$HOST" "$USER" "$PASS" "$REMOTE_DIR"

# 清理临时文件
rm /tmp/sftp_script.exp

echo "部署完成！"