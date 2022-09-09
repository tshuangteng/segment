import cv2
import os

img_path = ""

# 压缩图片为webp格式
webp_file_path = img_path.replace('jpg', 'webp')

try:
    img = cv2.imread(img_path)
    cv2.imwrite(webp_file_path, img, [cv2.IMWRITE_WEBP_QUALITY, 80])
except Exception as e:
    print(f'图片压缩异常: {e}')
    webp_file_path = ''

# 压缩成功后 删除jpg图片
if os.path.exists(img_path) and webp_file_path:
    os.remove(img_path)
else:
    webp_file_path = img_path
