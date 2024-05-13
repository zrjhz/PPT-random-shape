from PIL import Image
import numpy as np
import os

def convertImg2bin(img_path,img_name):
    # 读取图像
    image = Image.open(img_path+img_name)
    image = image.resize((800,480))
    # 调整图像尺寸为宽度和高度为偶数的大小
    width, height = image.size
    if width % 2 != 0:
        width -= 1
    if height % 2 != 0:
        height -= 1
    image = image.resize((width, height))

    # 转换为RGB565格式
    image_rgb565 = np.array(image, dtype=np.uint16)
    image_rgb565 = ((image_rgb565[..., 0] >> 3) << 11) | ((image_rgb565[..., 1] >> 2) << 5) | (image_rgb565[..., 2] >> 3)

    img_name = img_name.split(".")[0]
    # 保存为二进制文件
    image_rgb565.tofile(img_path+img_name+".bin")


dirs = os.listdir("./")
for dir in dirs:
    if os.path.isfile(dir) and (".bin" not in str.lower(dir)) and (".jpg" in str.lower(dir) or ".png" in str.lower(dir) or ".bmp" in str.lower(dir) or ".png" in str.lower(dir) or ".jpeg" in str.lower(dir)):
        print(dir)
        convertImg2bin("./",dir)
