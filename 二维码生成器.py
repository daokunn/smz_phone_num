import qrcode
from PIL import Image, ImageDraw

def generate_qr(url, filename="qrcode.png"):
    # 创建二维码对象
    qr = qrcode.QRCode(
        version=2,  # 控制二维码大小（1~40）
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 高容错率
        box_size=10,  # 每个小方块的像素大小
        border=4  # 边框宽度
    )
    qr.add_data(url)
    qr.make(fit=True)

    # 生成二维码图像（带颜色）
    img = qr.make_image(fill_color="#0078D4", back_color="white").convert("RGB")

    # 添加圆角边框（可选美化）
    rounded = Image.new("RGB", img.size, "white")
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, img.size[0], img.size[1]], radius=20, fill=255)
    rounded.paste(img, (0, 0), mask)

    # 保存二维码
    rounded.save(filename)
    print(f"✅ 已生成二维码：{filename}")

# 示例用法
generate_qr("https://smz.daokunn.cloudns.pro")
