# 树莓派OLED系统信息显示器

这是一个基于树莓派和OLED显示屏的系统信息监控项目。它可以实时显示树莓派的IP地址、CPU使用率、内存使用情况等系统信息。

## 功能特点

- 实时显示IP地址
- 监控CPU使用率
- 显示内存使用情况
- 显示设备型号信息
- 自动刷新显示（每3秒更新一次）

## 硬件要求

- 树莓派 3B+（其他型号树莓派也可能兼容）
- SSD1306 OLED显示屏（128x64像素）
- I2C接口连接

## 依赖库

```bash
pip3 install adafruit-circuitpython-ssd1306
pip3 install Pillow
pip3 install psutil
```

## 安装步骤

1. 确保树莓派已启用I2C接口
   ```bash
   sudo raspi-config
   # 进入Interface Options -> I2C -> 启用
   ```

2. 连接OLED显示屏
   - VCC 连接到 3.3V
   - GND 连接到 Ground
   - SDA 连接到 GPIO2 (SDA)
   - SCL 连接到 GPIO3 (SCL)

3. 安装所需依赖
   ```bash
   pip3 install -r requirements.txt
   ```

4. 运行程序
   ```bash
   python3 app.py
   ```

## 使用说明

程序运行后，OLED显示屏将自动显示以下信息：
- 第一行：当前IP地址
- 第二行：CPU使用率
- 第三行：内存使用情况
- 第四行：设备型号

显示内容每3秒自动更新一次。按Ctrl+C可以终止程序运行。

## 注意事项

- 确保OLED显示屏正确连接到I2C接口
- 运行程序需要root权限（因为需要访问I2C设备）
- 如果显示不正常，请检查I2C连接和地址设置

## 许可证
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
