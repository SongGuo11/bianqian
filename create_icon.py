from PIL import Image, ImageDraw
import os

def create_simple_icon():
    # 创建一个32x32的图像
    img = Image.new('RGB', (32, 32), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 绘制一个简单的便笺图标
    # 便笺的背景（黄色）
    draw.rectangle([2, 2, 30, 30], fill=(255, 255, 200), outline=(0, 0, 0))
    
    # 便笺的边缘线
    for i in range(6, 30, 4):
        draw.line([6, i, 26, i], fill=(200, 200, 200), width=1)
    
    # 便笺的顶部折叠角
    draw.polygon([(20, 2), (30, 2), (30, 12)], fill=(200, 200, 150))
    draw.line([(20, 2), (30, 12)], fill=(0, 0, 0), width=1)
    
    # 保存为ICO文件
    img.save('icons/notes_icon.ico', format='ICO')
    print("图标文件已创建: icons/notes_icon.ico")

if __name__ == "__main__":
    # 检查是否安装了Pillow库
    try:
        from PIL import Image, ImageDraw
        create_simple_icon()
    except ImportError:
        print("未安装Pillow库，将创建一个空的图标文件")
        # 创建一个空的图标文件
        with open('icons/notes_icon.ico', 'w') as f:
            f.write("")
        print("已创建空图标文件: icons/notes_icon.ico")