import requests
import io
from PIL import Image

url = "http://192.168.16.100:81/snapshot.cgi?loginuse=admin&loginpas=888888&res=0"
response = requests.get(url)
if response.status_code == 200:
    image_data = response.content
    image = Image.open(io.BytesIO(image_data))
    save_path = 'image.jpg'  # 保存路径和文件名
    image.save(save_path)
    print('保存成功')
else:
    print('请求失败:', response.status_code)
