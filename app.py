import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import socket
import psutil

# 初始化OLED屏幕
i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# 清空屏幕
display.fill(0)
display.show()

# 创建图像缓冲区
image = Image.new('1', (display.width, display.height))
draw = ImageDraw.Draw(image)

# 加载字体
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "No IP"

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return f"{mem.percent}%"

try:
    while True:
        # 清空缓冲区
        draw.rectangle((0,0,display.width, display.height), outline=0, fill=0)
        
        # 获取信息
        ip = get_ip_address()
        cpu = get_cpu_usage()
        mem = get_memory_usage()
        
        # 绘制文本
        draw.text((10, 0), f"IP: {ip}", font=font, fill=255)
        draw.text((10, 15), f"CPU: {cpu}%", font=font, fill=255)
        draw.text((10, 30), f"Mem: {mem}", font=font, fill=255)
        draw.text((10, 45), "Raspberry Pi 3B+", font=font, fill=255)
        
        # 显示图像
        display.image(image)
        display.show()
        
        # 等待3秒
        time.sleep(3)

except KeyboardInterrupt:
    display.fill(0)
    display.show()
